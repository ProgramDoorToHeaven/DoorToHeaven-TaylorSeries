from tools import *
from tools.columns import Column, Columns
from tools.menu import MenuList, get_year_menu_item
from tools.runner import run, DocumentsSelector


def get_year_menu_column(
        current_year: str,
        year_link_prefix: str = "../"
):
    return Column(
        headline="By years",
        content=(
            MenuList(items=(
                get_year_menu_item(1994, current_year, year_link_prefix),
                # get_year_menu_item(1997, current_year, year_link_prefix),
                # get_year_menu_item(1998, current_year, year_link_prefix),
            )),
        ),
    )


PAGE = Page(can_go_back=False, blocks=(
    Columns(
        spacing="columns-1-2",
        columns=(
            get_year_menu_column("", "./"),
            Column(
                content=(
                    PageBlock(parts=(
                        HeadLine(level=1, text="N.I.D. IS"),
                        Table(
                            header=("", ""),
                            items=(
                                ("User logged in", "Taylor Jones"),
                                ("N.I.D. division", "Military projects oversight"),
                                ("National security clearance", "Top secret"),
                                ("NATO security clearance", "NATO CTS"),
                                ("", ""),
                                ("Current agenda", "Program \"Door To Heaven\""),
                                ("Agenda classification", "Top secret - do not obtain copies"),
                                ("", ""),
                            ),
                        ),
                        Paragraph(text=("Welcome to the Program \"Door To Heaven\" agenda home page.",)),
                        Paragraph(text=("""
                            This section of the N.I.D. IS contains all accessible information
                            about the government's "Door To Heaven" program that you are authorized to view.
                    """,)),
                    )),
                ),
            ),
        )
    ),
    PageBlock(parts=(
        HeadLine(level=2, text="Tip of the day:"),
        HeadLine(level=3, text="Naming conventions"),
        Paragraph(text=("""
            It is required from all employees to follow these document naming conventions.
        """,)),
    )),
    PageBlock(block_type=PageBlockType.MONOSPACE_MODERN, parts=(
        LiteralParagraph(text=(r"""
            YYYYMMDD_YYYYMMDD_Document_name
            ^        ^        ^
            |        |         \___ Any human-friendly label.
            |         \____________ The date in the YYYYMMDD format when the document was
            |                        created. Can be omitted if it is reasonably close to
            |                        the date when the document was received and there is
            |                        no risk of ambiguity. Can be approximate if the
            |                        precise date is not known.
             \_____________________ The date in the YYYYMMDD format when the document was
                                     received by the N.I.D.
        """,)),
    )),
))


def main():
    PAGE.render(filename=__file__)
    run(DocumentsSelector())


if __name__ == "__main__":
    main()
