from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, Iterator

from tools.basic_printables import Printable
from tools.html_builder import new_tag, HtmlTag
from tools.markdown_params import MarkDownParams


@dataclass(frozen=True)
class Table(Printable):
    header: tuple[str, ...]
    items: tuple[tuple[str, ...], ...]

    def __post_init__(self):
        header_length = len(self.header)
        for index, row in enumerate(self.items):
            if len(row) == header_length:
                continue
            raise ValueError(
                f"Length of row #{index} is {len(row)}."
                + f" That does not match the length of header which is {header_length}."
            )

    @classmethod
    def new_table_without_header(cls, items: tuple[tuple[str, ...], ...]):
        return cls(header=tuple([""] * len(items[0])), items=items)

    def header_is_empty(self) -> bool:
        for item in self.header:
            if item:
                return False
        return True

    def get_widths(self) -> list[int]:
        widths: list[int] = [len(h) for h in self.header]
        for row in self.items:
            for index, item in enumerate(row):
                widths[index] = max(widths[index], len(item))
        return widths

    def get_html(self) -> HtmlTag:
        result = new_tag("table")
        if not self.header_is_empty():
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
        return result

    @staticmethod
    def get_markdown_row(row: Iterable[str], widths: list[int]) -> str:
        return "| " + " | ".join(
            item.ljust(width)
            for item, width in zip(row, widths)
        ) + " |"

    def get_markdown(self, markdown_params: MarkDownParams, first_line_special_prefix: str | None) -> Iterator[str]:
        widths = self.get_widths()
        if not self.header_is_empty():
            yield self.get_markdown_row(self.header, widths)
            yield self.get_markdown_row(
                [" "] * len(self.header), widths
            ).replace(" ", "-")
        for row in self.items:
            yield self.get_markdown_row(row, widths)
