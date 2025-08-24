from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Iterator

from tools.html_builder import new_tag, HtmlTag
from tools.markdown_params import MarkDownParams


class Printable(ABC):
    @abstractmethod
    def get_html(self) -> HtmlTag:
        raise NotImplementedError()

    @abstractmethod
    def get_markdown(self, markdown_params: MarkDownParams, first_line_special_prefix: str | None) -> Iterator[str]:
        raise NotImplementedError()


@dataclass(frozen=True)
class Paragraph(Printable):
    text: tuple[str, ...]
    is_literal: bool = False

    @classmethod
    def from_strings(cls, *text: str) -> Paragraph:
        return cls(tuple(text))

    def get_html(self) -> HtmlTag:
        result = new_tag("p")
        for item in self.text:
            result.append(item)
        return result

    def get_markdown(self, markdown_params: MarkDownParams, first_line_special_prefix: str | None) -> Iterator[str]:
        for item_index, item in enumerate(self.text):
            yield from markdown_params.get_formated_markdown_line(
                item_index, item, first_line_special_prefix, self.is_literal
            )


@dataclass(frozen=True)
class HeadLine(Printable):
    text: str
    level: int = 1

    def __post_init__(self):
        if self.level <= 0:
            raise ValueError(f"{self.__class__.__name__} expects level {self.level} > 0.")

    def get_html(self) -> HtmlTag:
        result = new_tag(f"h{self.level}")
        result.append(self.text)
        return result

    def get_markdown(self, markdown_params: MarkDownParams, first_line_special_prefix: str | None) -> Iterator[str]:
        underline: str | None = None
        prefix: str = ""
        match self.level:
            case 1:
                underline = "="
            case 2:
                underline = "-"
            case _:
                if not markdown_params.is_monospace:
                    prefix = "#" * self.level + " "
        result = prefix + self.text
        yield result
        if underline is not None:
            yield underline * len(result)


@dataclass(frozen=True)
class HorizontalLine(Printable):

    def get_html(self) -> HtmlTag:
        return new_tag("hr")

    def get_markdown(self, markdown_params: MarkDownParams, first_line_special_prefix: str | None) -> Iterator[str]:
        width = markdown_params.break_lines_before or 8
        yield "-" * width
