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
    # SGO:Catherine 00:03:16
    PageBlockTypeWriter(parts=(
        LiteralParagraph(strip_spaces_from_line_starts_according_to_line=3, text=("""
              TRANSCONTINENTAL COMMUNICATION COMPANY, LTD.

            81236                 BERLIN N°1    CAIRO, EGYPT
            8 22 39    Charge     AUG 22 '39    W.F.GALTZ
            18:30      7 Ø DM
            ----------------------------------------------------
            TO Receiver's Name:  DOCTOR PAUL LANGFORD
                       Address: WAREHOUSE DIST.No5 CAIRO, EGYPT

            THIS TELEGRAM WILL BE CHARGED AT FULL RATE
            ----------------------------------------------------
            Doctor Langford --

            I regret to inform that our contacts in
            Germany have not come through as
            we had hoped.

            This will be my last missive.
            Goodbye dear friend.

                                    -- Deitrich
        """,)),
    )),
    PageBlock(parts=(
        Paragraph(text=("""
            I’ve rarely encountered telegrams in my life.
            Around 1880, by the time I went to primary school, they were replaced by the more modern fax machine.
            Fax usage has been growing steadily, but the rise of internet-based e-mail was even more rapid.
            Today, both are used in roughly equal measure.
        """,)),
    )),
))


def main():
    PAGE.render(filename=__file__)


if __name__ == "__main__":
    main()
