from __future__ import annotations

from dataclasses import dataclass
from typing import Iterator

from tools.basic_printables import Printable
from tools.html_builder import HtmlTag
from tools.logger_getter import get_logger
from tools.markdown_params import MarkDownParams
from tools.page_block_type import PageBlockType

LOGGER = get_logger(__name__)


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
            if self.block_type.value.is_markdown_code_block:
                contents.extend(part.get_html_monospace())
            else:
                contents.extend(part.get_html())
        yield from self.block_type.get_html_tag(contents)

    def get_markdown(
            self,
            markdown_params: MarkDownParams = MarkDownParams(),
            first_line_special_prefix: str | None = None,
    ) -> Iterator[str]:
        block_type = self.block_type.value
        markdown_params = markdown_params.add_prefix(block_type.markdown_each_line_prefix)
        is_inside_block = False
        for part_index, part in enumerate(self.parts):
            if (part_index != 0) and (not part.omit_space_before):
                yield markdown_params.line_prefix.rstrip()  # space between parts
            markdown_params_for_part = markdown_params
            is_monotype = self.block_type.value.is_markdown_code_block
            breaks_block = is_monotype and part.breaks_markdown_code_block()
            if breaks_block:
                if is_inside_block and block_type.markdown_end:
                    LOGGER.warning(f"Block {self.block_type} is broken by {part}. This might look ugly.")
                    yield block_type.markdown_end
                    is_inside_block = False
            else:
                if is_monotype:
                    markdown_params_for_part = markdown_params_for_part.set_monospace(self.break_lines)
                if not is_inside_block and block_type.markdown_start:
                    yield block_type.markdown_start
                    is_inside_block = True
            yield from part.get_markdown(markdown_params_for_part, first_line_special_prefix=first_line_special_prefix)
        if is_inside_block and block_type.markdown_end:
            yield block_type.markdown_end
            # is_inside_block = False


@dataclass(frozen=True)
class PageBlockTypeWriter(PageBlock):
    block_type: PageBlockType = PageBlockType.TYPEWRITER
    break_lines: int = 80
