from dataclasses import dataclass
from typing import Iterator

from tools.basic_printables import Printable
from tools.html_builder import HtmlTag, new_tag
from tools.link import OptionalLink
from tools.markdown_params import MarkDownParams


@dataclass(frozen=True)
class MenuList(Printable):
    items: tuple[OptionalLink, ...] = ()

    def get_html(self) -> Iterator[HtmlTag]:
        result = new_tag("ul")
        for item in self.items:
            for tag in item.get_html():
                li = new_tag("li")
                li.append(tag)
                result.append(li)
        yield result

    def get_markdown(
            self, markdown_params: MarkDownParams, first_line_special_prefix: str | None,
    ) -> Iterator[str]:
        markdown_params_with_prefix = markdown_params.add_prefix("  ")
        for item in self.items:
            yield from item.get_markdown(markdown_params_with_prefix, "* ")


def get_year_menu_item(
        year: int | str,
        current_year: str,
        year_link_prefix: str = "../",
) -> OptionalLink:
    year = str(year)
    return OptionalLink(
        text=year,
        link="" if year == current_year else f"{year_link_prefix}{year}/README.md",
        replace_readme_index=True,
    )


def get_document_menu_item(
        document: str,
) -> OptionalLink:
    return OptionalLink(
        text=document,
        link=f"./{document}/README.md",
        replace_readme_index=True,
    )
