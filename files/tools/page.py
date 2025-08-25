from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
import os
import sys
from typing import Iterable, Iterator

from tools.basic_printables import Printable
from tools.html_builder import build_html, html_to_string, HtmlTag, new_tag
from tools.markdown_params import MarkDownParams


@dataclass(frozen=True)
class PageBlockTypeItem:
    html_tag: str
    html_classes: tuple[str, ...] = ()
    markdown_start: str | None = None
    markdown_end: str | None = None
    markdown_each_line_prefix: str = ""

    def get_html_tag(self, contents: Iterable[HtmlTag | str]) -> HtmlTag:
        result = new_tag(self.html_tag)
        result.extend(contents)
        wrapper = new_tag("div", class_=self.html_classes)
        wrapper.append(result)
        return wrapper


class PageBlockType(Enum):
    THOUGHTS = PageBlockTypeItem(
        html_tag="div", html_classes=("thoughts",),
    )
    MONOTYPE = PageBlockTypeItem(
        html_tag="pre", html_classes=("typewriter",),
        markdown_start="```", markdown_end="```",
    )
    QUOTATION = PageBlockTypeItem(
        html_tag="div", html_classes=("quotation",),
        markdown_each_line_prefix="> ",
    )

    def get_html_tag(self, contents: Iterable[HtmlTag | str]) -> HtmlTag:
        return self.value.get_html_tag(contents)


@dataclass(frozen=True)
class PageBlock(Printable):
    parts: tuple[Printable, ...] = tuple()
    block_type: PageBlockType = PageBlockType.THOUGHTS
    break_lines: int | None = None

    def __post_init__(self):
        if not self.parts:
            raise ValueError("Empty block.")

    def get_html(self) -> HtmlTag:
        contents: list[HtmlTag | str] = []
        for part_index, part in enumerate(self.parts):
            if (part_index != 0) and (not part.omit_space_before):
                contents.extend("\n")
            part_encoded: Iterable[HtmlTag | str]
            if self.block_type is PageBlockType.MONOTYPE:
                markdown_params = MarkDownParams().set_monospace(self.break_lines)
                part_encoded = (
                    line + "\n"
                    for line in part.get_markdown(markdown_params, first_line_special_prefix=None)
                )
            else:
                part_encoded = (part.get_html(),)
            contents.extend(part_encoded)
        return self.block_type.get_html_tag(contents)

    def get_markdown(
            self,
            markdown_params: MarkDownParams = MarkDownParams(),
            first_line_special_prefix: str | None = None,
    ) -> Iterator[str]:
        block_type = self.block_type.value
        markdown_params = markdown_params.add_prefix(block_type.markdown_each_line_prefix)
        if block_type.markdown_start:
            yield block_type.markdown_start
        for part_index, part in enumerate(self.parts):
            if (part_index != 0) and (not part.omit_space_before):
                yield markdown_params.line_prefix.rstrip()  # space between parts
            markdown_params_for_part = markdown_params
            if self.block_type is PageBlockType.MONOTYPE:
                markdown_params_for_part = markdown_params_for_part.set_monospace(self.break_lines)
            yield from part.get_markdown(markdown_params_for_part, first_line_special_prefix=first_line_special_prefix)
        if block_type.markdown_end:
            yield block_type.markdown_end


@dataclass(frozen=True)
class PageBlockTypeWriter(PageBlock):
    block_type: PageBlockType = PageBlockType.MONOTYPE
    break_lines: int = 80


@dataclass(frozen=True)
class Page(Printable):
    blocks: tuple[PageBlock, ...] = tuple()

    def __post_init__(self):
        if not self.blocks:
            raise ValueError("Empty page.")

    def get_html(self) -> HtmlTag:
        result = new_tag("div", class_="page")
        for block in self.blocks:
            result.append(block.get_html())
        return result

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
