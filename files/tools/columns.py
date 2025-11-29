from __future__ import annotations

from dataclasses import dataclass
from typing import Iterator, Literal

from tools.basic_printables import Printable
from tools.headline import HeadLine
from tools.html_builder import new_tag, HtmlTag
from tools.markdown_params import MarkDownParams


@dataclass(frozen=True)
class Column:
    content: tuple[Printable, ...]
    headline: str = ""

    def get_headline_object(self, level: int = 2) -> HeadLine | None:
        if not self.headline:
            return None
        return HeadLine(
            text=self.headline,
            level=level,
        )


@dataclass(frozen=True)
class Columns(Printable):
    spacing: Literal["columns-1-2"] | None = None
    columns: tuple[Column, ...] = ()

    @property
    def classes(self) -> list[str]:
        result = ["columns"]
        if self.spacing is not None:
            result.append(self.spacing)
        return result

    def get_html(self) -> Iterator[HtmlTag]:
        columns_div = new_tag("div", class_=self.classes)
        for column in self.columns:
            column_div = new_tag("div", class_="column")
            columns_div.append(column_div)

            headline = column.get_headline_object()
            if headline is not None:
                column_div.extend(headline.get_html())

            for content in column.content:
                column_div.extend(content.get_html())
        yield columns_div

    def get_markdown(
            self,
            markdown_params: MarkDownParams = MarkDownParams(),
            first_line_special_prefix: str | None = None,
    ) -> Iterator[str]:
        width = markdown_params.break_lines or 8
        for i, column in enumerate(self.columns):
            if i != 0:
                yield ""
                yield "-" * width
                yield ""

            headline = column.get_headline_object()
            if headline is not None:
                yield from headline.get_markdown(markdown_params, first_line_special_prefix)
                yield ""

            for content in column.content:
                yield from content.get_markdown(markdown_params, first_line_special_prefix)
