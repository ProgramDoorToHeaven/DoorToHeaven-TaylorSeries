from tools import *

PAGE = Page(blocks=(
    PageBlockTypeWriter(parts=(
        HeadLine(level=1, text="Discovery and initial analysis of the circular artifacts"),
        Paragraph(is_literal=True, text=("""
            Location:              Giza Plateau, Egypt
            Date:                  September 8, 1928
            Report prepared by:    Prof. Paul Langford, Lead Archaeologist
        """,)),
        HeadLine(level=2, text="Introduction"),
        Paragraph(text=("""
            A significant archaeological discovery was made near the Great Pyramids in Giza, Egypt.
            This report details the unearthing and initial analysis of a large, circular artifact found beneath a cover stone,
            accompanied by 2 buried human bodies in ritual armor with jackal heads and decorated staffs.
        """,)),
    )),
    PageBlock(parts=(
        Paragraph(text=("""
            Ok, that might be the "Door" this program is interested in.
            But since when is our military interested in ancient history?
        """,)),
    )),
    PageBlockTypeWriter(parts=(
        HeadLine(level=2, text="Discovery"),
        Paragraph(text=("""
            While leading an archaeological expedition near the Great Pyramids, my team and I uncovered a large, circular artifact buried beneath a substantial cover stone.
            Accompanying the artifact were two remains of human bodies, which we initially hypothesized could be remnants of an ancient burial ritual or guardians of the artifact.
            The artifact itself is composed of what appears to be melted meteorite, exhibiting a metallic structure unlike any known materials from the historical or geological record.
        """,)),
    )),
    PageBlock(parts=(
        Paragraph(text=("Maybe the Air Force isn't interested in history, but rather in the material?",)),
    )),
    PageBlockTypeWriter(parts=(
        HeadLine(level=2, text="Initial Analysis"),
        HeadLine(level=3, text="Material Composition"),
        Paragraph(text=("""
            Preliminary analysis of the artifact indicates that it is composed of a unique metallic substance, potentially from a melted meteorite.
            The material exhibits unusual properties, and further study is required to fully understand its composition and potential origins.
        """,)),
        Paragraph(text=("It weighs around 30 000 kg and its diameter is 6.7 m.",)),
    )),
    PageBlock(parts=(
        Paragraph(text=("""
            That's 65 000 pounds and 22 feet in the imperial units. 
            Egypt switched to the metric system in 1891.
            And Germany (where prof. Langford was from) has been using metric since 1870s.
            The whole world went crazy and switched to this abstract system instead of the natural and relatable one.
        """,)),
        Paragraph(text=("""
            I mean scientists like the metric system because of the ease of conversion between units.
            And that is probably the reason why most of the world adopted it.
            But you usually don't need to do any unit conversions anyway.
            And in the rare occasions when 5-to-mat-oes are necessary, calculator has your back.
        """,)),
        Paragraph(text=("""
            We even had the Metric Conversion Act of 1975 as an effort to join the rest of the world. 
            It established the U.S. Metric Board, which was tasked with coordinating and planning the voluntary conversion to the metric system.
            But it was just voluntary and the general public did not feel a pressing need to change their everyday measurement habits.
            So the Board was eventually disbanded in 1982 due to lack of progress and funding.
        """,)),
        Paragraph(text=("""
            And here I am. 
            Like my colleagues before me.
            Tasked with auditing military programs, tracking their progress and suggesting changes to their funding.
            Keeping the national expenses efficient and preventing wasting of taxpayer's money. 
            So I hope the Air Force has some break through with the materials,
            and they already started experimenting with new stealth bombers or fighters made of something based on this Egyptian metallurgy.
        """,)),
    )),
    PageBlockTypeWriter(parts=(
        # Many thanks to almighty Rebet for casting his knowledge upon me https://www.youtube.com/watch?v=90An1dnvwyc
        HeadLine(level=3, text="Symbol Inscription"),
        Paragraph(text=("""
            The artifact is inscribed with a series of complex symbols arranged in a circular pattern around its perimeter.
            These symbols do not correspond to any known writing system.
            Linguists and cryptographers are currently attempting to decipher their meaning and possible significance.
        """,)),
        Paragraph(text=("""
            The cover stone's outer ring depicts the artifact with it's symbols.
            Inside the artifact depiction on the cover stone, there are early hieroglyphic inscriptions (estimated to come from the era around 3000 BCE).
            In the center, there is an ornamental cartouche with 6 of the symbols from the outer ring.
        """,)),
        Paragraph(text=("""
            We are excited by the new unknown symbols.
            They could be a writing system of an older civilization and the hieroglyphs accompanying them would typically (on similar bilingual artifacts) be their translation.
        """,)),
        Paragraph(text=("""
            None of the symbols on the artifact is used twice.
            This indicates, it could be a 39-character phonemic alphabet with one word written in the cartouche in the middle.
            Another argument for a phonemic alphabet is the fact that the symbols do not resemble the shape of aby daily use or religious items as we would expect in a logographic alphabet.
        """,)),
        Paragraph(text=("""
            The word in the cartouche in the middle of the cover stone is probably a name of a god or a king.
            At least in the hieroglyphic writing system, that is what cartouches were reserved for.
            We are hoping to match the name to some known god or king.
            This could be the key to deciphering the new writing system.
        """,)),
    )),
    PageBlock(parts=(
        Paragraph(text=("Probably not relevant, but still interesting.",)),
        Paragraph(text=("""
            In logographic writing systems - like Chinese - each symbol represents a whole word or concept, not just a sound.
            This contrasts with phonemic systems, such as Latin or Greek, where characters correspond to specific sounds, making pronunciation more predictable from the written form.
        """,)),
        Paragraph(text=("""
            English is neither of these.
            For example, in the name of "Pacific Ocean", each "C" is pronounced differently.
        """,)),
        Paragraph(text=("""
            On the other hand, Egyptian hieroglyphs were hybrid.
            They combined logographic symbols (pictures for whole words), phonemic signs (symbols for sounds), and determinatives (clarifying pictures).
            Determinatives are like adding a picture of gift, clock, or projector after "present" to specify meaning.
        """,)),
        # the first set of emojis was from 1999, so no mentions here in 1994 😢
    )),
    PageBlockTypeWriter(parts=(
        HeadLine(level=3, text="Buried guardians"),
        Paragraph(text=("""
            The two buried bodies were discovered with unhealed broken bones, suggesting they may have met a violent end.
            Their jackal masks are made of metal and they contain mechanical parts which used to move.
            This level of craftsmanship also doesn't match anything known from this age.
            The ornamental staffs are well preserved and don't have any sharp edges.
            Although they could be used as blunt weapons, their primary use was probably purely decorative or an indication of social status.
        """,)),
        Paragraph(text=("""
            The presence of the two guardians alongside the artifact suggests a possible ceremonial or protective role.
            They might have died protecting the artifact or in a brutal sacrificial ritual.
            Further investigation is needed to determine their exact nature and relationship to the artifact.
        """,)),
        HeadLine(level=2, text="Conclusion"),
        Paragraph(text=("""
            The discovery of this artifact represents a significant advancement in our understanding of ancient metallurgy and symbolism.
            Further interdisciplinary research is essential to unravel the mysteries surrounding its origin and purpose.
        """,)),
    )),
    PageBlock(block_type=PageBlockType.QUOTATION, parts=(
        HeadLine(level=1, text="Document summary"),
        Paragraph(text=("by Taylor Jones",)),
        Table.new_nid_table_for_document_summary(
            document_name="Discovery and initial analysis of the circular artifacts",
            document_author="Prof. Paul Langford",
            year=1928, month=9, day=8,
        ),
        Paragraph(text=("""
            In 1928, prof. Langford discovered a circular artefact in Egypt.
            It was made of an interesting metal.
        """,)),
        HeadLine(level=2, text="Recommendation"),
        Paragraph(text=("""
            This document probably does not need to have any access restrictions.
            The knowledge of the material might be worth protecting.
        """,)),
    )),
    PageBlock(parts=(
        Paragraph(text=("I can't imagine how keeping this artefact secret could help the national security.",)),
    )),
))


def main():
    PAGE.render()


if __name__ == "__main__":
    main()
