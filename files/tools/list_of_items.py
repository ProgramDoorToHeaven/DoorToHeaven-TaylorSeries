from __future__ import annotations

from dataclasses import dataclass
from types import MethodType
from typing import Callable, Iterator

from tools.basic_printables import Paragraph, Printable
from tools.html_builder import new_tag, HtmlTag
from tools.markdown_params import MarkDownParams


@dataclass(frozen=True)
class ListOfItems(Printable):
    items: tuple[Paragraph, ...] = ()
    html_ordered: str | None = None
    index_to_prefix: Callable[[ListOfItems, int], str] = lambda self, index: "-"
    max_prefix_length: Callable[[ListOfItems], int] = lambda self: 1

    def __post_init__(self):
        if not self.items:
            raise ValueError("Empty list.")

    # bind function to class instance
    @property
    def translate_enumeration_to_prefix(self):
        return MethodType(self.index_to_prefix, self)

    # bind function to class instance
    @property
    def get_max_prefix_length(self):
        return MethodType(self.max_prefix_length, self)

    def get_markdown_prefix(self, index: int) -> str:
        prefix = self.translate_enumeration_to_prefix(index)
        to_length = self.get_max_prefix_length() + 1
        return prefix.ljust(to_length)

    def get_html(self) -> Iterator[HtmlTag]:
        if self.html_ordered is None:
            result = new_tag("ul")
        else:
            result = new_tag("ol", type=self.html_ordered)
        for item in self.items:
            tag = new_tag("li")
            tag.extend(item.get_html())
            result.append(tag)
        yield result

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
    index_to_prefix: Callable[[NumberedList, int], str] = (
        lambda self, index: self.prefix_format.format(index + 1)
    )
    max_prefix_length: Callable[[NumberedList], int] = lambda self: len(self.prefix_format.format(len(self.items)))


@dataclass(frozen=True)
class LetteredList(ListOfItems):
    html_ordered: str = "a"
    prefix_format: str = "{})"
    index_to_prefix: Callable[[LetteredList, int], str] = (
        lambda self, index: self.prefix_format.format(ord(self.html_ordered) + index)
    )
    max_prefix_length: Callable[[LetteredList], int] = lambda self: len(self.prefix_format.format("a"))

    def __post_init__(self):
        max_length = ord("z") - ord("a") + 1
        if len(self.items) > max_length:
            raise ValueError(
                f"List length supported only up to {max_length} (a-z)."
                + f" Got {len(self.items)} instead."
            )
