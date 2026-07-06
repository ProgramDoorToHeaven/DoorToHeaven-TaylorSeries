"""
Nuclear bomb research:
https://en.wikipedia.org/wiki/Manhattan_Project
Britain - project Tube Alloys - started 1941, later absorbed by the US Manhattan Project
US - Manhattan Project - 1942-1946
First nuclear bomb detonation: 1945-07-16 (Trinity test, White Sands Proving Ground, New Mexico)
Hiroshima and Nagasaki: 1945-08

The war:
D-Day in Normandy:    1944-06
Surrender of Germany: 1945-05
Surrender of Japan:   1945-09

So the experiments are probably from the first half of 1945.

--------------------------------

SG-1 01x11 Torment of Tantalus:

DANIEL: This was transferred from film of experiments done on the gate in 1945
DANIEL: Yes, just like you could have told me there were experiments done on the gate in 1945.

DANIEL: There's no conclusion to the file. There's no summary; no notes. No reason to explain why they gave up.

CATHERINE: Thousands of Stargates. Planetary shifts. Didn't anyone think that I might be interested?
# That means they analyzed the Abydos cartouche and compensated for the stellar drift AFTER Catherine was out of the SG project.
# The cartouche is introduced in Children of Gods?

CATHERINE: My father worked on the research team that worked on the gate during the war. Actually, they didn't know what
it was then. But President Roosevelt was like that, curious. They suspected the gate was a weapon, could be used as one.
Nothing ever came of it...

DANIEL:
The Pentagon has recently been declassifying old materials. They ran across a number of file boxes that dealt with the
old experiments and they sent them to us.

ERNEST:
We get as far as entering the fifth symbol and then the whole room starts to shake. Today, one of the generators
exploded from the feedback.

CATHERINE: Are you using alternating or direct current to charge it?
ERNEST: Alternating…I think. Why?
CATHERINE: Try using direct. It might prevent the charge from bouncing back to the generator...

DANIEL:
Sooo, you didn't know the government kept the files from the original experiments.
CATHERINE:
I had my father's notes. He told me that was everything they had. Do you know how many administrations I had to petition
to get this program started up again? Forty years had passed. The information was classified and buried. I never asked
for any files, because I thought I had them. General West never offered, because he probably didn't know they existed.
DANIEL:
So, you don't know that they turned the gate on in 1945.

ERNEST:
There must be over a hundred million possible combinations. If it's merely a combination lock used to turn it on, why 39
symbols? Why not six?
LANGFORD:
What are you saying?
ERNEST:
They're not combinations. They're destinations, and we just found one.
LANGFORD:
A doorway to heaven can mean any number of different things. It could simply mean that anyone who passes through there
will die... For example.

CATHERINE: No. I never knew they turned it on. My father never told me. It wasn't in his notes, either.

LANGFORD: There was an accident today. An explosion in the lab.

CATHERINE: My father must have lied to me. He said Ernest died in an accident. An explosion.

CATHERINE: Not Abydos?
DANIEL: No. Another planet with similar coordinates.…And, we can go there.

O'NEILL: ... she used to run the entire program and is responsible for most of our current knowledge about the gate.

CARTER: It seems the planet in question is close to Abydos, so it uses many of the same points in space as locators,
which explains why the team in '45 could coincidentally dial in without compensating for planetary shift. But Sir, the
planet in question is not on the cartouche we found on Abydos.

Addresses are supposed to be similar ("it uses many of the same points in space as locators").
The first 2 glyphs are the same (shown on-screen by Daniel to Catherine)
PLANET     = GLYPHS
---------- - -----------------------
ABYDOS     = 027 007 015 032 012 030 = https://stargate.fandom.com/wiki/Abydos
HELIOPOLIS = 027 007 ??? ??? ??? ??? = https://stargate.fandom.com/wiki/Heliopolis
@ time 11:35-11:39, it seems like Glyph 15 is #3 on the next paper
@ time 41:43, the Abydos address is unsuccessfully dialed on-screen

--------------------------------

SG-1 02x21 1969:
CATHERINE:
When the war ended, my father and I were told never to speak of it again. It is simply…locked away.
Some old armory in Washington, D.C., gathering dust. But it's pointless. The military won't even acknowledge its
existence.
"""

from tools import *

PAGE = Page(blocks=(
    PageBlock(parts=(
        Paragraph(text=("""
            I've been sifting through Egyptian artifacts,
            while some of my colleagues got assigned to similarly ancient UFO cases.
            Youssef, for instance, currently has evidence related to the 1947 Roswell incident on his desk -
            it's a shame that he can't tell me whether it actually happened.
            Our boss seems to have run out of meaningful work for us.
        """,)),
        Paragraph(text=("""
            Yesterday, I was tasked with convincing our research department to transfer footage from old 16mm films to VHS.
            Today, my job was to watch and label all of it.
            I skimmed through about half on fast-forward.
            Without timestamps or date labels - just a wall clock in the background - it's hard to piece together a timeline.
            I'm assuming the footage on each tape is in chronological order, but who knows?
        """,), comment=(
            Paragraph(text=("""
                Fun fact: The camera used in Torment of Tantalus 0:00:40 is probably Bolex H16.
            """,)),
            ParagraphLink(text="Wikipedia - Bolex", link="https://en.wikipedia.org/wiki/Bolex"),
            Paragraph(text=("""
            Daniel: There's no conclusion to the file. There's no summary; no notes. No reason to explain why they gave up.
        """,)),
        )),
        Paragraph(text=("""
            Honestly, it doesn't matter.
            Most of the videos are painfully dull:
            men in lab coats or uniforms flipping switches, triggering the occasional power malfunction, and endlessly spinning an artifact.
            The only mildly interesting detail is that the inner circle of the artifact rotates - but then again, it's round, so why wouldn't it?
        """,), comment=(
            Paragraph(text=("""
                Hammond:
                "What? It has to spin, it's round!
                Spinning is so much cooler than not spinning.
                I'm the general, I want it to spin. Now!"
            """,)),
        )),
        Paragraph(text=("""
            I think I'll skip the rest.
            They believed it could be weaponized - after all,
            it allegedly killed a Nazi in 1939 and wiped the memories of the Langfords.
            So, they hooked it up to electrical cables and tried to replicate the experiment from Egypt.
            Unsuccessfully, it seems.
        """,)),
        Paragraph(text=("""
            Later that summer, the first nuclear bomb tests took place.
            And since those went rather better than the artifact experiments,
            the bomb won out as the ultimate tool of fear and war-ending intimidation.
        """,)),
    )),
    PageBlock(block_type=PageBlockType.QUOTATION, parts=(
        HeadLine(level=1, text="Archive content summary"),
        Table.new_nid_table_for_document_summary(
            document_name='Filmed "Door to Heaven" experiments',
            document_author="Prof. Paul Langford; Dr. Ernest Littlefield",
            year=1945, month="xx",
        ),
        Paragraph(text=("""
            In 1945, Prof. Langford and Dr. Littlefield
            conducted unsuccessful experiments with the "Door to Heaven" artifact.
            This box contains recordings of said experiments transferred from 16 mm films to VHS.
        """,)),
        Paragraph(text=("""
            The research was commissioned by president Roosevelt but was ultimately abandoned after a period of no progress,
            particularly following Dr. Ernest Littlefield's fatal accident.
        """,)),
    )),
))


def main():
    PAGE.render(filename=__file__)


if __name__ == "__main__":
    main()
