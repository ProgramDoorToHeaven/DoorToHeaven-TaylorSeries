from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Iterator

from tools.html_builder import new_tag, HtmlTag
from tools.markdown_params import MarkDownParams


@dataclass(frozen=True)
class Printable(ABC):
    omit_space_before: bool = False

    @staticmethod
    def breaks_markdown_code_block() -> bool:
        return False

    @abstractmethod
    def get_html(self) -> Iterator[HtmlTag]:
        raise NotImplementedError()

    def get_html_monospace(self) -> Iterator[HtmlTag]:
        return self.get_html()

    @abstractmethod
    def get_markdown(self, markdown_params: MarkDownParams, first_line_special_prefix: str | None) -> Iterator[str]:
        raise NotImplementedError()


@dataclass(frozen=True)
class HorizontalLine(Printable):

    def get_html(self) -> Iterator[HtmlTag]:
        yield new_tag("hr")

    def get_markdown(self, markdown_params: MarkDownParams, first_line_special_prefix: str | None) -> Iterator[str]:
        width = markdown_params.break_lines or 8
        yield "-" * width
