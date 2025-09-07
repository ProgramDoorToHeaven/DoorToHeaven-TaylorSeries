from __future__ import annotations

from dataclasses import dataclass
from functools import cached_property
from typing import Iterable, Iterator

from tools import LiteralParagraph
from tools.basic_printables import Printable
from tools.html_builder import new_tag, HtmlTag
from tools.markdown_params import MarkDownParams


@dataclass(frozen=True)
class Table(Printable):
    header: tuple[str, ...] = ()
    items: tuple[tuple[str, ...], ...] = ()

    def __post_init__(self):
        if self.number_of_columns <= 0:
            raise ValueError("Table without columns.")
        if not self.items:
            raise ValueError("Table without rows.")
        for index, row in enumerate(self.items):
            if len(row) == self.number_of_columns:
                continue
            raise ValueError(
                f"Length of row #{index} is {len(row)}."
                + f" That does not match the number of columns which is {self.number_of_columns}."
            )
        if self.number_of_columns != len(self.header):
            raise ValueError(
                f"Length of header is {len(self.header)}."
                + f" That does not match the number of columns which is {self.number_of_columns}."
            )

    @classmethod
    def new_table_without_header(cls, items: tuple[tuple[str, ...], ...]) -> Table:
        return cls(header=tuple([""] * len(items[0])), items=items)

    @classmethod
    def new_nid_table_for_document_summary(
            cls,
            document_name: str,
            document_author: str,
            year: str | int,
            month: str | int,
            day: str | int = "xx",
    ) -> Table:
        return cls.new_table_without_header(items=(
            ("Document", document_name),
            ("Date", f"{year}-{month:0>2}-{day:0>2}"),
            ("Author", document_author),
        ))

    @cached_property
    def number_of_columns(self) -> int:
        return len(self.header)

    @cached_property
    def header_is_empty(self) -> bool:
        for item in self.header:
            if item:
                return False
        return True

    @cached_property
    def widths(self) -> list[int]:
        widths: list[int] = [len(h) for h in self.header]
        for row in self.items:
            for index, item in enumerate(row):
                widths[index] = max(widths[index], len(item))
        return widths

    def get_html(self) -> Iterator[HtmlTag]:
        result = new_tag("table")
        if not self.header_is_empty:
            header = new_tag("thead")
            row = new_tag("tr")
            for item in self.header:
                tag = new_tag("th")
                tag.append(item)
                row.append(tag)
            header.append(row)
            result.append(header)
        body = new_tag("tbody")
        for items_row in self.items:
            row = new_tag("tr")
            for item in items_row:
                tag = new_tag("td")
                tag.append(item)
                row.append(tag)
            body.append(row)
        result.append(body)
        yield result

    def get_html_monospace(self) -> Iterator[HtmlTag]:
        markdown = self.get_markdown(
            markdown_params=MarkDownParams(),
            first_line_special_prefix=None,
        )
        table = LiteralParagraph(
            strip_first_line_if_empty=False,
            strip_last_line_if_empty=False,
            strip_spaces_from_line_starts_according_to_line=None,
            text=tuple(
                line
                for index, line in enumerate(markdown)
                if (not self.header_is_empty) or (index not in (0, 1))
            ),
        )
        yield from table.get_html()

    def get_markdown_row(self, row: Iterable[str]) -> str:
        return "| " + " | ".join(
            item.ljust(width)
            for item, width in zip(row, self.widths)
        ) + " |"

    def get_markdown_header_separator(self) -> str:
        return self.get_markdown_row([" "] * self.number_of_columns).replace(" ", "-")

    def get_markdown(self, markdown_params: MarkDownParams, first_line_special_prefix: str | None) -> Iterator[str]:
        yield markdown_params.line_prefix + self.get_markdown_row(self.header)
        yield markdown_params.line_prefix + self.get_markdown_header_separator()
        for row in self.items:
            yield markdown_params.line_prefix + self.get_markdown_row(row)
