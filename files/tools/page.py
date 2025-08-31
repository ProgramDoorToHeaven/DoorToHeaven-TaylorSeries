from __future__ import annotations

from dataclasses import dataclass
import os
import sys
from typing import  Iterator

from tools.basic_printables import Printable
from tools.html_builder import build_html, html_to_string, HtmlTag, new_tag
from tools.markdown_params import MarkDownParams
from tools.page_block import PageBlock



@dataclass(frozen=True)
class Page(Printable):
    blocks: tuple[PageBlock, ...] = ()

    def __post_init__(self):
        if not self.blocks:
            raise ValueError("Empty page.")

    def get_html(self) -> Iterator[HtmlTag]:
        page = new_tag("div", class_="page")
        for block in self.blocks:
            page.extend(block.get_html())
        wrapper = new_tag("div", class_="page-wrapper")
        wrapper.append(page)
        yield wrapper

    def get_markdown(
            self,
            markdown_params: MarkDownParams | None = None,
            first_line_special_prefix: str | None = None,
    ) -> Iterator[str]:
        for block_index, block in enumerate(self.blocks):
            if block_index != 0:
                yield ""  # space between blocks
            yield from block.get_markdown()

    def render(self, filename: str | None = None) -> None:
        if not filename:
            main_script = sys.argv[0]
            filename = os.path.abspath(main_script)
        extension_py = ".py"
        if filename.endswith(extension_py):
            filename = filename[:-len(extension_py)]
        with open(filename + ".md", encoding="utf-8", mode="w") as f:
            f.writelines((
                line + "\n"
                for line in self.get_markdown()
            ))
        with open(filename + ".html", encoding="utf-8", mode="w") as f:
            main_div = self.get_html()
            whole_html = build_html(main_div)
            f.write(html_to_string(whole_html))
