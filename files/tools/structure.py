from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass, replace
from enum import Enum
from typing import Callable, Iterable, Iterator

from bs4 import BeautifulSoup, Tag  # pip install beautifulsoup4
from bs4.element import AttributeValueList  # pip install beautifulsoup4

SOUP = BeautifulSoup(features="html.parser")


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
        if is_literal or (self.break_lines_before is None):
            yield from line.splitlines(keepends=False)
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
            yield self.get_line_prefix(index, first_line_special_prefix) + line
        for line in iterator:
            yield self.line_prefix + line


class Printable(ABC):
    @abstractmethod
    def get_html(self) -> Tag:
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

    def get_html(self) -> Tag:
        result = SOUP.new_tag("p")
        for item in self.text:
            result.append(item)
        return result

    def get_markdown(self, markdown_params: MarkDownParams, first_line_special_prefix: str | None) -> Iterator[str]:
        for item_index, item in zip(self.text):
            yield from markdown_params.get_formated_markdown_line(
                item_index, item, first_line_special_prefix, self.is_literal
            )


@dataclass(frozen=True)
class Header(Printable):
    text: str
    level: int = 1

    def __post_init__(self):
        if self.level <= 0:
            raise ValueError(f"{self.__class__.__name__} expects level {self.level} > 0.")

    def get_html(self) -> Tag:
        result = SOUP.new_tag(f"h{self.level}")
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
class ListOfItems(Printable):
    items: tuple[Paragraph, ...]
    html_ordered: str | None = None
    enumeration_to_prefix: Callable[[ListOfItems, int], str] = lambda self, index: "-"
    max_prefix_length: Callable[[ListOfItems], int] = lambda self: 1

    def get_markdown_prefix(self, index: int) -> str:
        prefix = self.enumeration_to_prefix(index)
        to_length = self.max_prefix_length() + 1
        return prefix.ljust(to_length)

    def get_html(self) -> Tag:
        if self.html_ordered is None:
            result = SOUP.new_tag("ul")
        else:
            result = SOUP.new_tag("ol", type=self.html_ordered)
        for item in self.items:
            tag = SOUP.new_tag("li")
            tag.append(item.get_html())
            result.append(tag)
        return result

    def get_markdown(self, markdown_params: MarkDownParams, first_line_special_prefix: str | None) -> Iterator[str]:
        for item_index, item in enumerate(self.items):
            item_prefix = self.get_markdown_prefix(item_index)
            prefix_length = len(item_prefix)
            item_prefix_next_line = " " * prefix_length
            yield from item.get_markdown(markdown_params.add_prefix(item_prefix_next_line), item_prefix)


@dataclass(frozen=True)
class NumberedList(ListOfItems):
    html_ordered: str = "1"
    prefix_format: str = "{})"
    enumeration_to_prefix: Callable[[NumberedList, int], str] = (
        lambda self, index: self.prefix_format.format(index + 1)
    )
    max_prefix_length: Callable[[NumberedList], int] = lambda self: len(self.prefix_format.format(len(self.items)))


@dataclass(frozen=True)
class LetteredList(ListOfItems):
    html_ordered: str = "a"
    prefix_format: str = "{})"
    enumeration_to_prefix: Callable[[LetteredList, int], str] = (
        lambda self, index: self.prefix_format.format(ord(self.html_ordered) + index)
    )
    max_prefix_length: Callable[[LetteredList], int] = lambda self: len(self.prefix_format.format("a"))

    def __post_init__(self):
        max_length = ord("z") - ord("a") + 1
        if len(self.items) > max_length:
            raise ValueError(
                f"{self.__class__.__name__} supports only lists up to length {max_length}."
                + f" Got {len(self.items)} instead."
            )


@dataclass(frozen=True)
class Table(Printable):
    header: tuple[str, ...]
    items: tuple[tuple[str, ...]]

    def __post_init__(self):
        header_length = len(self.header)
        for index, row in enumerate(self.items):
            if len(row) == header_length:
                continue
            raise ValueError(
                f"Length of row #{index} is {len(row)}."
                + f" That does not match the length of header which is {header_length}."
            )

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

    def get_html(self) -> Tag:
        result = SOUP.new_tag("table")
        if not self.header_is_empty():
            header = SOUP.new_tag("thead")
            row = SOUP.new_tag("tr")
            for item in self.header:
                tag = SOUP.new_tag("th")
                tag.append(item)
                row.append(tag)
            header.append(row)
            result.append(header)
        body = SOUP.new_tag("tbody")
        for items_row in self.items:
            row = SOUP.new_tag("tr")
            for item in items_row:
                tag = SOUP.new_tag("td")
                tag.append(item)
                row.append(tag)
            body.append(row)
        result.append(body)
        return result

    @staticmethod
    def get_markdown_row(row: Iterable[str], widths: list[int]) -> str:
        return "| " + " | ".join(
            item.rjust(width)
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


@dataclass(frozen=True)
class HorizontalLine(Printable):

    def get_html(self) -> Tag:
        return SOUP.new_tag("hr")

    def get_markdown(self, markdown_params: MarkDownParams, first_line_special_prefix: str | None) -> Iterator[str]:
        width = markdown_params.break_lines_before or 8
        yield "-" * width


@dataclass(frozen=True)
class DocumentBlockTypeItem:
    html_tag: str
    html_classes: tuple[str, ...] = ()
    markdown_start: str | None = None
    markdown_end: str | None = None
    markdown_each_line_prefix: str = ""

    def get_html(self) -> Tag:
        result = SOUP.new_tag(self.html_tag)
        result["class"] = AttributeValueList(self.html_classes)
        return result


class DocumentBlockType(Enum):
    NORMAL = DocumentBlockTypeItem(
        html_tag="div",
    )
    MONOTYPE = DocumentBlockTypeItem(
        html_tag="pre",
        markdown_start="```", markdown_end="```",
    )
    QUOTATION = DocumentBlockTypeItem(
        html_tag="div", html_classes=("quotation",),
        markdown_each_line_prefix="> ",
    )

    def get_html(self) -> Tag:
        return self.value.get_html()


@dataclass(frozen=True)
class DocumentBlock(Printable):
    parts: tuple[Paragraph | ListOfItems | HorizontalLine, ...]
    block_type: DocumentBlockType = DocumentBlockType.NORMAL
    break_lines_before_chars: int | None = None

    def get_html(self) -> Tag:
        result = self.block_type.get_html()
        for part in self.parts:
            part_encoded: Iterable[Tag | str]
            if self.block_type is DocumentBlockType.MONOTYPE:
                markdown_params = MarkDownParams(is_monospace=True, break_lines_before=self.break_lines_before_chars)
                part_encoded = part.get_markdown(markdown_params, first_line_special_prefix=None)
            else:
                part_encoded = (part.get_html(),)
            result.extend(part_encoded)
        return result

    def get_markdown(self, markdown_params: MarkDownParams, first_line_special_prefix: str | None) -> Iterator[str]:
        for part_index, part in enumerate(self.parts):
            if part_index != 0:
                yield ""  # space between parts
            block_type = self.block_type.value
            if block_type.markdown_start:
                yield block_type.markdown_start
            markdown_params_for_part = markdown_params.add_prefix(block_type.markdown_each_line_prefix)
            yield from part.get_markdown(markdown_params_for_part, first_line_special_prefix=None)
            if block_type.markdown_end:
                yield block_type.markdown_end


@dataclass(frozen=True)
class Document(Printable):
    blocks: tuple[DocumentBlock]
