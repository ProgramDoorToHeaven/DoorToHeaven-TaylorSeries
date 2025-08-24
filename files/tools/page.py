from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Iterable, Iterator

from basic_printables import Printable
from html_builder import HtmlTag, new_tag
from markdown_params import MarkDownParams


@dataclass(frozen=True)
class PageBlockTypeItem:
    html_tag: str
    html_classes: tuple[str, ...] = ()
    markdown_start: str | None = None
    markdown_end: str | None = None
    markdown_each_line_prefix: str = ""

    def get_html(self) -> HtmlTag:
        return new_tag(self.html_tag, class_=self.html_classes)


class PageBlockType(Enum):
    NORMAL = PageBlockTypeItem(
        html_tag="div",
    )
    MONOTYPE = PageBlockTypeItem(
        html_tag="pre",
        markdown_start="```", markdown_end="```",
    )
    QUOTATION = PageBlockTypeItem(
        html_tag="div", html_classes=("quotation",),
        markdown_each_line_prefix="> ",
    )

    def get_html(self) -> HtmlTag:
        return self.value.get_html()


@dataclass(frozen=True)
class PageBlock(Printable):
    parts: tuple[Printable, ...]
    block_type: PageBlockType = PageBlockType.NORMAL
    break_lines_before_chars: int | None = None

    def get_html(self) -> HtmlTag:
        result = self.block_type.get_html()
        for part in self.parts:
            part_encoded: Iterable[HtmlTag | str]
            if self.block_type is PageBlockType.MONOTYPE:
                markdown_params = MarkDownParams(is_monospace=True, break_lines_before=self.break_lines_before_chars)
                part_encoded = part.get_markdown(markdown_params, first_line_special_prefix=None)
            else:
                part_encoded = (part.get_html(),)
            result.extend(part_encoded)
        return result

    def get_markdown(
            self,
            markdown_params: MarkDownParams = MarkDownParams(),
            first_line_special_prefix: str | None = None,
    ) -> Iterator[str]:
        for part_index, part in enumerate(self.parts):
            if part_index != 0:
                yield ""  # space between parts
            block_type = self.block_type.value
            if block_type.markdown_start:
                yield block_type.markdown_start
            markdown_params_for_part = markdown_params.add_prefix(block_type.markdown_each_line_prefix)
            yield from part.get_markdown(markdown_params_for_part, first_line_special_prefix=first_line_special_prefix)
            if block_type.markdown_end:
                yield block_type.markdown_end


@dataclass(frozen=True)
class Page(Printable):
    blocks: tuple[PageBlock, ...]

    def get_html(self) -> HtmlTag:
        result = new_tag("div")
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
