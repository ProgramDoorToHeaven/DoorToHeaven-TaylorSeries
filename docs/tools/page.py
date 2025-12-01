from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import sys
from typing import Iterator

from tools.basic_printables import Printable
from tools.columns import Columns
from tools.html_builder import build_html, html_to_string, HtmlTag, new_tag
from tools.link import Link
from tools.markdown_params import MarkDownParams
from tools.page_block import PageBlock

BACK_LINK = Link(
    text="⬅️ Back",  # Some don't work on some platforms: ←🡐⇦⬅⇽⇐🔙⬅️
    link="../index.html",
)


@dataclass(frozen=True)
class Page(Printable):
    blocks: tuple[PageBlock | Columns, ...] = ()
    can_go_back: bool = True

    def __post_init__(self):
        if not self.blocks:
            raise ValueError("Empty page.")

    def get_html(self) -> Iterator[HtmlTag]:

        page = new_tag("div", class_="page")
        if self.can_go_back:
            page.extend(BACK_LINK.get_html())
        else:
            page.append(new_tag("span", class_="line-height"))

        for block in self.blocks:
            page.extend(block.get_html())

        if self.can_go_back:
            page.extend(BACK_LINK.get_html())
        else:
            page.append(new_tag("span", class_="line-height"))

        wrapper = new_tag("div", class_="page-wrapper")
        wrapper.append(page)
        yield wrapper

    def get_markdown(
            self,
            markdown_params: MarkDownParams = MarkDownParams(),
            first_line_special_prefix: str | None = None,
    ) -> Iterator[str]:
        if self.can_go_back:
            yield from BACK_LINK.get_markdown(markdown_params, first_line_special_prefix)
        for block in self.blocks:
            yield ""  # space between blocks
            yield from block.get_markdown()
        yield ""  # space between blocks
        if self.can_go_back:
            yield from BACK_LINK.get_markdown(markdown_params, first_line_special_prefix)

    def render(self, filename: str | None = None) -> None:
        file_path = Path(filename) if filename else Path(sys.argv[0]).absolute()
        dir_path = file_path.parent

        tools_depth: int = 0
        dir_parent = dir_path
        while not (dir_parent / "tools").is_dir():
            dir_parent = dir_parent.parent
            tools_depth += 1

        with open(dir_path / "README.md", encoding="utf-8", mode="w") as f:
            f.writelines((
                line + "\n"
                for line in self.get_markdown()
            ))
        with open(dir_path / "index.html", encoding="utf-8", mode="w") as f:
            main_div = self.get_html()
            whole_html = build_html(main_div, tools_depth)
            f.write(html_to_string(whole_html))
