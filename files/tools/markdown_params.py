from __future__ import annotations

from dataclasses import dataclass, replace
from typing import Iterator


@dataclass(frozen=True)
class MarkDownParams:
    is_monospace: bool = False
    break_lines_before: int | None = None
    line_prefix: str = ""

    def __post_init__(self):
        minimum_width = 20
        if (self.break_lines_before is not None) and (self.break_lines_before - len(self.line_prefix) < minimum_width):
            raise ValueError(
                f"Minimum width is {minimum_width}."
                + f" Got {self.break_lines_before}-{len(self.line_prefix)} instead."
            )

    def add_prefix(self, prefix: str) -> MarkDownParams:
        return replace(
            self,
            line_prefix=prefix + self.line_prefix,
        )

    def set_monospace(self, break_lines_before: int | None) -> MarkDownParams:
        return replace(
            self,
            is_monospace=True,
            break_lines_before=break_lines_before,
        )

    def get_line_prefix(self, index: int, first_line_special_prefix: str | None) -> str:
        if index > 0:
            return self.line_prefix
        if index < 0:
            raise ValueError(f"Negative index {index} not expected.")
        if first_line_special_prefix is None:
            return self.line_prefix
        if len(first_line_special_prefix) != len(self.line_prefix):
            raise ValueError(
                f"Length of first line prefix {len(first_line_special_prefix)} !="
                + f" length of other lines prefix {len(self.line_prefix)}."
            )
        return first_line_special_prefix

    @staticmethod
    def _generate_words(line: str) -> Iterator[str]:
        for section in line.splitlines(keepends=False):
            for word in section.split():
                word = word.strip()
                if len(word) == 0:
                    continue
                yield word

    def _generate_lines(self, line: str, is_literal: bool = False) -> Iterator[str]:
        line=line.strip()
        if is_literal or (self.break_lines_before is None):
            for row in line.splitlines(keepends=False):
                yield row.strip()
            return

        prefix_length = len(self.line_prefix)
        result = ""
        for word in self._generate_words(line):
            if len(result) + len(word) > self.break_lines_before - prefix_length:
                if result == "":
                    raise ValueError(
                        f"Word '{word}' is too long."
                        + f" It does not fit on an empty line of length {self.break_lines_before}-{prefix_length}"
                    )
                yield result.strip()
                result = ""
            result += f"{word} "
        if result != "":
            yield result.strip()

    def get_formated_markdown_line(
            self,
            index: int,
            line: str,
            first_line_special_prefix: str | None,
            is_literal: bool = False,
    ) -> Iterator[str]:
        iterator = self._generate_lines(line, is_literal)
        first_line = next(iterator, None)
        if first_line is not None:
            yield self.get_line_prefix(index, first_line_special_prefix) + first_line
        for row in iterator:
            yield self.line_prefix + row
