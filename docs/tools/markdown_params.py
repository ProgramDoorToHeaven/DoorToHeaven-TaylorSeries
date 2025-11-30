from __future__ import annotations

from dataclasses import dataclass, replace
import re
import textwrap
from typing import Iterator


@dataclass(frozen=True)
class MarkDownParams:
    is_monospace: bool = False
    break_lines: int | None = None
    line_prefix: str = ""

    def __post_init__(self):
        minimum_width = 20
        if (self.break_lines is not None) and (self.break_lines - len(self.line_prefix) < minimum_width):
            raise ValueError(
                f"Minimum width is {minimum_width}."
                + f" Got {self.break_lines}-{len(self.line_prefix)} instead.",
            )

    def add_prefix(self, prefix: str) -> MarkDownParams:
        return replace(
            self,
            line_prefix=prefix + self.line_prefix,
        )

    def set_monospace(self, break_lines: int | None) -> MarkDownParams:
        return replace(
            self,
            is_monospace=True,
            break_lines=break_lines,
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
                + f" length of other lines prefix {len(self.line_prefix)}.",
            )
        return first_line_special_prefix

    def _get_lines(self, line: str, is_literal: bool = False) -> str:
        if is_literal:
            return line
        line = line.strip()
        if is_literal or (self.break_lines is None):
            return '\n'.join(row.strip() for row in line.splitlines(keepends=False))
        line = line.strip()
        prefix_length = len(self.line_prefix)
        line = re.sub(r'\s+', ' ', line).strip()
        line_wrapped = textwrap.fill(line, width=self.break_lines - prefix_length)
        return line_wrapped

    def get_formated_markdown_line(
            self,
            line: str,
            first_line_special_prefix: str | None,
            is_literal: bool = False,
    ) -> Iterator[str]:
        lines = self._get_lines(line, is_literal)
        lines_prefixed = textwrap.indent(lines, self.line_prefix)
        if (first_line_special_prefix is not None) and lines_prefixed.startswith(self.line_prefix):
            # set different first line prefix
            if len(first_line_special_prefix) != len(self.line_prefix):
                raise ValueError(
                    f"Length of first line prefix {len(first_line_special_prefix)} !="
                    + f" length of other lines prefix {len(self.line_prefix)}.",
                )
            lines_prefixed = first_line_special_prefix + lines_prefixed[len(self.line_prefix):]
        yield from lines_prefixed.splitlines(keepends=False)
