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
            On August 24, 1939, British operatives encountered a highly unusual and concerning situation involving German nationals, a missing British officer, and a huge ring artifact.
            The following details have been compiled from intercepted communications, field reports, and witness testimony.
        """,)),
        # HorizontalLine(),
        HeadLine(level=2, text="Key Findings"),
        HeadLine(level=3, text="Fatality of a German officer"),
        ListOfItems(items=(
            Paragraph(text=("""
                A German officer, partially identified as Schutzstaffel Obersturmführer Heinrich (last name unknown),
                was found deceased with severe burns on the right side of his chest.
                The cause of death appears linked to an experiment with the artifact.
                The damage was likely caused by an electrical current, since the ring was connected to a car generator via cables.
            """,)),
            # No last name mentioned anywhere - just Heinrich
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
                Wasif Alabu Khan, an Egyptian soldier assigned to the same outpost, is also missing.
                His disappearance is considered highly irregular, as he is not known to be the type to go AWOL.
            """,)),
        )),
        HeadLine(level=3, text="Memory loss among German researchers"),
        ListOfItems(items=(
            Paragraph(text=("""
                Two German researchers involved in the incident (prof. Paul Langford and his daughter Catherine Langford)
                exhibited genuine memory loss covering the last two days, as confirmed by a medical professional.
                The suspected cause is the psychological shock triggered by the German officer’s death.
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
                A radio cable intercepted from Berlin indicates that German authorities are actively seeking to acquire the artifact.
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
                The German embassy in Cairo must be contacted regarding the death of one of their officers.
            """,)),
            Paragraph(text=("""
                Artifact recovery:
                The artifact remains at the incident site.
                Immediate action is required to secure and transport it to the United States where prof. Langford will continue his research supervised by the U.S. intelligence agencies.
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
            Now this is the first genuinely suspicious thing in this pile of documents.
        """,)),
        Paragraph(text=("""
            The Langfords' memory loss isn't just a footnote in this report.
            It's the most human detail in a file full of cold facts and bureaucratic jargon.
            Two full days - missing. Not confused, not blurred - missing.
            And the doctors agreed the gap was real.
       """,)),
        Paragraph(text=("""
            I've always been fascinated by how memory works.
            It's not a filing cabinet, neat and orderly.
            It's more like a living process - changing a little each time you recall something.
            Neuroscientists call this reconsolidation.
            When you remember, the brain temporarily opens the memory, updates it, and stores it again.
            That's why memories drift.
            It's why eyewitnesses contradict each other without lying.
            It's why childhood places feel different later - you're comparing an old internal model to a new reality.
            Your brain isn't a recorder; it's a storyteller, and it edits for coherence, for emotion, for survival.
       """,)),
        Paragraph(text=("""
            But the Langfords didn't just misremember.
            They lost time.
            That's different.
            That's not the brain editing - it's the brain deleting.
            And that doesn't happen without a cause.
        """,)),
        Paragraph(text=("""
            There are a few ways this can go down.
            Psychogenic or dissociative amnesia is one.
            Extreme stress can disrupt how the brain forms or retrieves memories.
            People can forget the moments before an accident, or whole episodes tied to emotional shock.
            It's not the brain "protecting" itself in a conscious sense - it's more that the systems responsible for recording experience can shut down under overload.
            But these cases usually involve direct personal trauma.
            The Langfords weren't harmed.
            So why would their memory systems fail this way?
        """,)),
        Paragraph(text=("""
            Then there's neurological interference:
            head injury, seizures, oxygen deprivation, certain toxins.
            Anything that disrupts the hippocampus or surrounding networks can produce blank periods.
            But the report mentions no injuries, no poisoning, no medical red flags.
            Just... a ring, a car battery, and two days that never were.
        """,)),
        HorizontalLine(),
        Paragraph(text=("""
            I keep coming back to that image: a ring structure, hooked up to a generator.
            What were they attempting?
            What outcome did they expect?
        """,)),
        Paragraph(text=("""
            The Germans didn't shy away from dangerous experiments, but this doesn't read as carelessness.
            It reads as urgency.
            They were chasing something, and they were willing to risk a man's life - and apparently their own sanity - to reach it.
        """,)),
        Paragraph(text=("""
            History has moments like this.
            Someone splits the atom for the first time.
            Someone carries out the first open-heart surgery.
            Someone looks through a telescope and realizes the Earth isn't the center of everything.
            In those moments, the world tilts.
            People witness something that doesn't fit their previous beliefs, and they're never quite the same.
        """,)),
        Paragraph(text=("""
            The Langfords saw something that didn't fit.
            Their memory systems didn't reinterpret it - they crashed.
            A hard failure, not a soft rewrite.
        """,)),
        Paragraph(text=("""
            It's disturbing, but it's human.
            Faced with something that overwhelms the machinery of memory, the brain sometimes does the simplest thing it can: it stops recording.
        """,)),
        HorizontalLine(),
        Paragraph(text=("""
            Anyway, there seems to be a way to use this artifact for killing people.
            And that explains the interest of the Air Force.
       """,)),
        Paragraph(text=("""
            I guess they succeeded moving it to the US when the war started. 
            It wouldn't land on my desk otherwise. 
            Let's see how successful they were with the research.
        """,)),
    )),
))


def main():
    PAGE.render(filename=__file__)


if __name__ == "__main__":
    main()
