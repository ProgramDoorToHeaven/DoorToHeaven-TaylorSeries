from __future__ import annotations

from dataclasses import dataclass
from typing import Iterator

from tools.basic_printables import Printable
from tools.html_builder import new_tag, HtmlTag
from tools.markdown_params import MarkDownParams


@dataclass(frozen=True)
class Paragraph(Printable):
    text: tuple[str, ...] = ()

    def __post_init__(self):
        if not self.text:
            raise ValueError("Empty paragraph.")

    def get_html(self) -> Iterator[HtmlTag]:
        result = new_tag("p", omit_space_before=self.omit_space_before)
        for index, item in enumerate(self.text):
            if index != 0:
                result.append(new_tag("br"))
            result.append(item)
        yield result

    def get_markdown(
            self, markdown_params: MarkDownParams, first_line_special_prefix: str | None,
    ) -> Iterator[str]:
        for item in self.text:
            yield from markdown_params.get_formated_markdown_line(
                item, first_line_special_prefix, False,
            )


@dataclass(frozen=True)
class LiteralParagraph(Paragraph):
    strip_first_line_if_empty: bool = True
    strip_last_line_if_empty: bool = True
    strip_spaces_from_line_starts_according_to_line: int | None = 1

    def _get_html_lines(self, text: str) -> Iterator[str]:
        if self.strip_spaces_from_line_starts_according_to_line is None:
            yield text
            return
        lines = text.splitlines(keepends=False)
        length = len(lines)
        if length == 0:
            return
        if length == 1:
            yield from lines
            return

        strip_count = self.get_strip_count(lines)

        del length  # will change now
        if self.strip_first_line_if_empty and not lines[0].strip():
            del lines[0]
        if self.strip_last_line_if_empty and not lines[-1].strip():
            del lines[-1]
        for line in lines:
            if len(line) <= strip_count and not line.strip():
                yield "\n"
                continue
            yield self.strip_prefix(line, strip_count)
            yield "\n"

    @staticmethod
    def strip_prefix(line: str, strip_count: int) -> str:
        if len(line) == 0:
            return line
        if not line.startswith(" " * strip_count):
            raise ValueError(f"Expected line to start with {strip_count} spaces: {line}")
        return line[strip_count:]

    def get_strip_count(self, lines: list[str]) -> int:
        length = len(lines)
        if not (0 <= self.strip_spaces_from_line_starts_according_to_line < length):
            raise ValueError(f"Expected 0 <= {self.strip_spaces_from_line_starts_according_to_line=} < {length=}.")
        etalon_line = lines[self.strip_spaces_from_line_starts_according_to_line]
        strip_count = len(etalon_line) - len(etalon_line.lstrip())
        return strip_count

    def get_html(self) -> Iterator[HtmlTag]:
        result = new_tag("pre")
        for item in self.text:
            result.extend(self._get_html_lines(item))
        yield result

    def get_markdown(
            self, markdown_params: MarkDownParams, first_line_special_prefix: str | None,
    ) -> Iterator[str]:
        for item in self.text:
            lines = item.splitlines(keepends=False)
            strip_count = self.get_strip_count(lines)
            if self.strip_first_line_if_empty and not lines[0].strip():
                del lines[0]
            if self.strip_last_line_if_empty and not lines[-1].strip():
                del lines[-1]
            item = "\n".join(
                self.strip_prefix(line, strip_count)
                for line in lines
            )
            yield from markdown_params.get_formated_markdown_line(
                item, first_line_special_prefix, True,
            )
