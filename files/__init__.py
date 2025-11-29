from tools.columns import Column
from tools.menu import MenuList, get_year_menu_item
from tools.runner import run, DocumentsSelector


def get_year_menu_column(
        current_year: str,
):
    return Column(
        headline="By years",
        content=MenuList(items=(
            get_year_menu_item(1994, current_year),
            get_year_menu_item(1997, current_year),
            get_year_menu_item(1998, current_year),
        )),
    )


PAGE = None  # TODO

if __name__ == "__main__":
    run(DocumentsSelector())
