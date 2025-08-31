from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, Iterator

from tools.basic_printables import Printable
from tools.html_builder import HtmlTag
from tools.markdown_params import MarkDownParams
from tools.page_block_type import PageBlockType



@dataclass(frozen=True)
class PageBlock(Printable):
    parts: tuple[Printable, ...] = ()
    block_type: PageBlockType = PageBlockType.THOUGHTS
    break_lines: int | None = None

    def __post_init__(self):
        if not self.parts:
            raise ValueError("Empty block.")

    def get_html(self) -> Iterator[HtmlTag]:
        contents: list[HtmlTag | str] = []
        for part_index, part in enumerate(self.parts):
            if (part_index != 0) and (not part.omit_space_before):
                contents.extend("\n")
            part_encoded: Iterable[HtmlTag | str]
            if self.block_type is PageBlockType.TYPEWRITER:
                markdown_params = MarkDownParams().set_monospace(self.break_lines)
                part_encoded = (
                    line + "\n"
                    for line in part.get_markdown(markdown_params, first_line_special_prefix=None)
                )
            else:
                part_encoded = part.get_html()
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
            if self.block_type is PageBlockType.TYPEWRITER:
                markdown_params_for_part = markdown_params_for_part.set_monospace(self.break_lines)
            yield from part.get_markdown(markdown_params_for_part, first_line_special_prefix=first_line_special_prefix)
        if block_type.markdown_end:
            yield block_type.markdown_end


@dataclass(frozen=True)
class PageBlockTypeWriter(PageBlock):
    block_type: PageBlockType = PageBlockType.TYPEWRITER
    break_lines: int = 80
