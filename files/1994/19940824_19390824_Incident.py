"""
Warehouse Dist. No5 Cairo, Egypt = telegram address from SGO
August 22 '39 = date from a telegram
They dial in the evening, spend approx 1.5 days on Abbydos, return August 24-ish

Well, I guess they were lucky.
Whatever it was they were working on ended up killing that Nazi [Heinrich, burnt wound on his chest],
and, apparently, wiped both of their memories.
The doctor did seem convinced that the memory loss was genuine.
that cable that we intercepted from Berlin, suggests these Germans are keen to acquire whatever this thing is.
You're certain you never encountered our missing British officer, Captain James Beal?
What about Wasif Alabu Khan. [Egyptian soldier]
He isn't the type to simply go AWOL.
If you can remember anything, please contact the British Embassy when you arrive in the States.
Apparently the Germans have been funding them for years...
"""

from tools import *

PAGE = Page(blocks=(
    # SGO:Catherine 00:03:16
    PageBlockTypeWriter(parts=(
        HeadLine(level=1, text="BRITISH INTELLIGENCE REPORT"),
        LiteralParagraph(text=("""
            Date:             24 August 1939
            Classification:   CONFIDENTIAL
            From:             British Intelligence, Field Operative
            To:               Director of Naval Intelligence, London
        """,)),
        # HorizontalLine(),
        HeadLine(level=2, text="Incident Summary"),
        Paragraph(text=("""
            On August 24, 1939, British operatives encountered a highly unusual and concerning situation involving German nationals, a missing British officer, and a huge ring artefact.
            The following details have been compiled from intercepted communications, field reports, and witness testimony.
        """,)),
        # HorizontalLine(),
        HeadLine(level=2, text="Key Findings"),
        HeadLine(level=3, text="Fatality of a German soldier"),
        ListOfItems(items=(
            Paragraph(text=("""
                A German soldier, partially identified as Schutzstaffel Obersturmführer Heinrich (last name unknown),
                was found deceased with severe burns on the right side of his chest.
                The cause of death appears linked to an experiment with the artifact.
                The damage was likely caused by an electrical current, since the ring was connected to a car generator via cables.
            """,)),
            Paragraph(text=("""
                Unfortunately, he had his ID documents in the shirt pocket which was burned.
                Only a part of his dog tag remained readable.
            """,)),
        )),
        HeadLine(level=3, text="Missing British and Egyptian personnel"),
        ListOfItems(items=(
            Paragraph(text=("""
                Captain James Beal, a British officer, remains unaccounted for.
                He was stationed in a nearby outpost.
                His whereabouts and potential involvement in the incident are unknown.
            """,)),
            Paragraph(text=("""
                Wasif Alabu Khan, an Egyptian soldier, is also missing.
                His disappearance is considered highly irregular, as he is not known to be the type to go AWOL.
            """,)),
        )),
        HeadLine(level=3, text="Memory loss among German researchers"),
        ListOfItems(items=(
            Paragraph(text=("""
                Two German researchers involved in the incident (prof. Paul Langford and his daughter Catherine Langford)
                exhibited genuine memory loss covering the last two days, as confirmed by a medical professional.
                The suspected cause is the psychological shock triggered by the German soldier’s death.
            """,)),
            Paragraph(text=("""
                The researchers were unable to provide further details regarding the experiment or the artifact.
                They discovered it 10 years ago on the Giza plateau, and have been researching it since then without any significant progress.
                They couldn't recall why it had been connected to the electrical source.
            """,)),
        )),
        HeadLine(level=3, text="Intercepted German communication"),
        ListOfItems(items=(
            Paragraph(text=("""
                A cable intercepted from Berlin indicates that German authorities are actively seeking to acquire the artifact.
                The urgency and tone of the communication suggest its strategic importance.
            """,)),
        )),
        HeadLine(level=3, text="German funding of foreign operations"),
        ListOfItems(items=(
            Paragraph(text=("""
                Evidence suggests that German authorities have been funding foreign archeological and research operatives in this area for years.
            """,)),
        )),
        # HorizontalLine(),
        HeadLine(level=2, text="Recommendations"),
        NumberedList(items=(
            Paragraph(text=("""
                Immediate investigation:
                A full inquiry must be launched to locate Captain Beal and Wasif Alabu Khan, and to determine their connection to the incident.
                The German embassy in Cairo must be contacted regarding the death of one of their soldiers.
            """,)),
            Paragraph(text=("""
                Artifact recovery:
                The artifact remains at the incident site.
                Immediate action is required to secure and transport it to the United States as a priority.
                Given the escalating tensions in Europe and the German interest in acquiring the artifact, its recovery must be treated with the utmost urgency to prevent it from being compromised.
            """,)),
            Paragraph(text=("""
                Monitor German Activity:
                Increased surveillance of German communications and operatives is recommended to track their movements and intentions.
            """,)),
            Paragraph(text=("""
                Collaboration with Allies:
                Coordinate with Egyptian authorities and other allies to gather additional intelligence on German-funded operations in the region.
            """,)),
        )),
        # HorizontalLine(),
        HeadLine(level=2, text="Conclusion"),
        Paragraph(text=("""
            The incident suggests the existence of a dangerous experimental German project, with potential implications for British and Allied security.
            The disappearance of British and Egyptian personnel, combined with German efforts to recover the artifact, underscores the urgency of this matter.
        """,)),
        Paragraph(text=("""
            All operatives are instructed to report any further developments immediately to the British Embassy or relevant intelligence channels.
        """,)),
    )),
    PageBlock(parts=(
        Paragraph(text=("""
            
        """,)),
    )),
))


def main():
    PAGE.render(filename=__file__)


if __name__ == "__main__":
    main()
