from pathlib import Path

from files import get_year_menu_column
from tools.columns import Column, Columns
from tools.menu import MenuList, get_document_menu_item
from tools.page import Page
from tools.runner import run_year

year_dir = Path(__file__).parent

PAGE = Page(blocks=(
    Columns(
        spacing="columns-1-2",
        columns=(
            get_year_menu_column(year_dir.name),
            Column(
                headline="1994",
                content=MenuList(items=(
                    get_document_menu_item("19940824_19270423_Giza_excavations"),
                    get_document_menu_item("19940824_19280908_Artifacts_discovery"),
                    get_document_menu_item("19940824_19360000_Cairo_letter"),
                    get_document_menu_item("19940824_19390822_Telegram"),
                    get_document_menu_item("19940824_19390824_Incident"),
                    # get_document_menu_item("19940824_19390900_Achilles"),
                    # get_document_menu_item("19940824_19450000_Experiment"),
                )),
            ),
        )
    ),
))


def main():
    PAGE.render(filename=__file__)
    run_year(year_dir.name)


if __name__ == "__main__":
    main()
