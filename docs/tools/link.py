from dataclasses import dataclass
from functools import cached_property
from typing import Iterator

from tools.basic_printables import Printable
from tools.html_builder import HtmlTag, new_tag
from tools.markdown_params import MarkDownParams


@dataclass(frozen=True)
class Link(Printable):
    text: str = ""
    link: str = ""
    replace_readme_index: bool = False

    @cached_property
    def replaced_link(self) -> str:
        if not self.replace_readme_index:
            return self.link
        suffix_readme = "/README.md"
        if not self.link.endswith(suffix_readme):
            return self.link
        return self.link[:-len(suffix_readme)] + "/index.html"

    def get_html(self) -> Iterator[HtmlTag]:
        yield new_tag("a", self.text, href=self.replaced_link)

    def get_markdown(
            self, markdown_params: MarkDownParams, first_line_special_prefix: str | None,
    ) -> Iterator[str]:
        prefix = markdown_params.get_line_prefix(0, first_line_special_prefix)
        yield f"{prefix}[{self.text}]({self.replaced_link})"


@dataclass(frozen=True)
class OptionalLink(Link):

    @cached_property
    def is_link(self) -> bool:
        return bool(self.link)

    def get_html(self) -> Iterator[HtmlTag]:
        if self.is_link:
            yield from super().get_html()
        else:
            yield new_tag("span", self.text)

    def get_markdown(
            self, markdown_params: MarkDownParams, first_line_special_prefix: str | None,
    ) -> Iterator[str]:
        if self.is_link:
            yield from super().get_markdown(markdown_params, first_line_special_prefix)
        else:
            prefix = markdown_params.get_line_prefix(0, first_line_special_prefix)
            yield prefix + self.text
