"""
Warehouse Dist. No5 Cairo, Egypt = telegram address from SGO
August 22 '39 = date from a telegram
They dial in the evening, spend approx 1.5 days on Abbydos, return August 24-ish

Well, I guess they were lucky.
Whatever it was they were working on ended up killing that Nazi [Heinrich],
and, apparently, wiped both of their memories.
The doctor did seem convinced that the memory loss was genuine.
that cable that we intercepted from Berlin, suggests these Germans are keen to acquire whatever this thing is.
You're certain you never encountered our missing British officer, Captain James Beal?
What about Wasif Alabu Khan.
He isn't the type to simply go AWOL.
If you can remember anything, please contact the British Embassy when you arrive in the States.
Apparently the Germans have been funding them for years...

Telegram
That's a week before the war started.
"""

from tools import *

PAGE = Page(blocks=(
    PageBlockTypeWriter(break_lines=52, parts=(
        Paragraph(text=("TRANSCONTINENTAL COMMUNICATION COMPANY, LTD.",)),
        Paragraph(is_literal=True, text=("""
            81236      Words     BERLIN N°1    CAIRO, EGYPT
            8 22 39    Charge    AUG 22 '39    W.F.GALTZ
            18:30      7 Ø DM
        """,)),
        HorizontalLine(omit_space_before=True),
        Paragraph(omit_space_before=True, keep_spaces=True, text=(
            "TO Receiver's Name:  DOCTOR PAUL LANGFORD",
        )),
        Paragraph(omit_space_before=True, keep_spaces=True, text=(
            "           Address: WAREHOUSE DIST.No5 CAIRO, EGYPT",
        )),
        Paragraph(text=("THIS TELEGRAM WILL BE CHARGED AT FULL RATE",)),
        HorizontalLine(omit_space_before=True),
        Paragraph(omit_space_before=True, text=("Doctor Langford --",)),
        Paragraph(is_literal=True, text=("""
            I regret to inform that our contacts in
            Germany have not come through as
            we had hoped.
        """,)),
        Paragraph(is_literal=True, text=("""
            This will be my last missive.
            Goodbye dear friend.
        """,)),
        Paragraph(keep_spaces=True, text=("                     -- Deitrich",)),
    )),
))


def main():
    PAGE.render(filename=__file__)


if __name__ == "__main__":
    main()
