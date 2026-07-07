from tools import *

PAGE = Page(blocks=(
    PageBlockTypeWriter(parts=(
        Paragraph(text=("Dear Deitrich,",)),
        Paragraph(text=("""
            I've been studying the ancient ring for over five years, yet it feels as if I haven't made any progress.
            The only significant achievement since its discovery has been translating the hieroglyphs on the cover stone.
        """,)),
        # From https://en.wikipedia.org/wiki/Stargate_%28film%29
        # r:n:p-rnp-t:Z2-I8:V20-r:q-b-H-w-W15-N1:N25-p-w-r:a-C1-m-i-t:n-N8
        # m-x-m-t-S20-Aa18-n:f-q:r-s-T19-A24-Q6:A55-f:n-D&t-tA:r-G21-H-H-ra:N23
        # s-sbA-b-O32-n:Z2-s-b-A-sbA:ra-Z2:f

        # MdC script
        #   https://oraec.github.io/corpus/mdc_to_unicode_converter.html
        #   https://www.leskoff.com/s01775-0

        # LiteralParagraph(text=("""
        #     𓂋𓈖𓊪 𓆳 𓏏𓏥 𓆐𓎆 𓂋𓈎 𓃀 𓎛 𓅱 𓏁 𓇯𓈉 𓊪 𓅱 𓂋𓂝 𓁚 𓅓 𓇋 𓏏𓈖 𓇶
        #     𓅓 𓐍 𓅓 𓏏 𓋩 𓐠 𓈖𓆑 𓈎𓂋 𓋴 𓌟 𓂡 𓊭𓁀 𓆑𓈖 𓆓𓏏 𓇾𓂋 𓅘 𓎛 𓎛 𓇳𓈇
        #     𓋴 𓇼 𓃀 𓊀 𓈖𓏥 𓋴 𓃀 𓄿 𓇼𓇳 𓏥𓆑
        # """,)),  # linearized
        # LiteralParagraph(text=("""
        #     𓂋𓐰𓈖𓐰𓊪𓆳𓏏𓐰𓏥𓆐𓐰𓎆𓂋𓐰𓈎𓃀𓎛𓅱𓏁𓇯𓐰𓈉𓊪𓅱𓂋𓐰𓂝𓁚𓅓𓇋𓏏𓐰𓈖𓇶
        #     𓅓𓐍𓅓𓏏𓋩𓐠𓈖𓐰𓆑𓈎𓐰𓂋𓋴𓌟𓀜𓊭𓐰𓁀𓆑𓐰𓈖𓆓𓐳𓏏𓇾𓐰𓂋𓅘𓎛𓎛𓇳𓐰𓈇
        #     𓋴𓇼𓃀𓊀𓈖𓐰𓏥𓋴𓃀𓄿𓇼𓐰𓇳𓏥𓐰𓆑
        # """,)),  # with stacking characters
        Image(
            relative_path="cover-stone-hieroglyphs-1-1-years.png",
            alternative_text="𓂋𓈖𓊪 𓆳 𓏏𓏥 𓆐𓎆\n/\n𓂋𓐰𓈖𓐰𓊪𓆳𓏏𓐰𓏥𓆐𓐰𓎆",
        ),
        Image(
            relative_path="cover-stone-hieroglyphs-1-2-sky.png",
            alternative_text="𓂋𓈎 𓃀 𓎛 𓅱 𓏁 𓇯𓈉 𓊪 𓅱\n/\n𓂋𓐰𓈎𓃀𓎛𓅱𓏁𓇯𓐰𓈉𓊪𓅱",
        ),
        Image(
            relative_path="cover-stone-hieroglyphs-1-3-ra.png",
            alternative_text="𓂋𓂝 𓁚 𓅓 𓇋 𓏏𓈖 𓇶\n/\n𓂋𓐰𓂝𓁚𓅓𓇋𓏏𓐰𓈖𓇶",
        ),
        Image(
            relative_path="cover-stone-hieroglyphs-2-1-buried.png",
            alternative_text="𓅓 𓐍 𓅓 𓏏 𓋩 𓐠 𓈖𓆑 𓈎𓂋 𓋴 𓌟 𓂡 𓊭𓁀 𓆑𓈖\n/\n𓅓𓐍𓅓𓏏𓋩𓐠𓈖𓐰𓆑𓈎𓐰𓂋𓋴𓌟𓀜𓊭𓐰𓁀𓆑𓐰𓈖",
        ),
        Image(
            relative_path="cover-stone-hieroglyphs-2-2-forever.png",
            alternative_text="𓆓𓏏 𓇾𓂋 𓅘 𓎛 𓎛 𓇳𓈇\n/\n𓆓𓐳𓏏𓇾𓐰𓂋𓅘𓎛𓎛𓇳𓐰𓈇",
        ),
        Image(
            relative_path="cover-stone-hieroglyphs-3-1-stargate.png",
            alternative_text="𓋴 𓇼 𓃀 𓊀 𓈖𓏥 𓋴 𓃀 𓄿 𓇼𓇳 𓏥𓆑\n/\n𓋴𓇼𓃀𓊀𓈖𓐰𓏥𓋴𓃀𓄿𓇼𓐰𓇳𓏥𓐰𓆑",
        ),
        Paragraph(text=("""
            The text mentions Ra - the god of the Sun - burying his "doorway to heaven" long ago.
            Therefore, the ring's name must be "Doorway to Heaven."
        """,)),
    )),
    PageBlock(parts=(
        Paragraph(text=("""
            So they called it "Doorway to Heaven," and we call it "Door to Heaven."
            Close enough, I suppose.
            I guess our translation is a bit more precise - half a century later.
        """,), comment=(
            LiteralParagraph(text=("""
            Langford translation from
            SG1 s01e11 Torment of Tantalus:
            doorway to heaven
        """,)),
            HorizontalLine(),
            LiteralParagraph(text=("""
            Partial translation by Dr. Myers:
            time million sky Ra sun god
            coffin forever to eternity
            his door to heaven
        """,)),
            HorizontalLine(),
            LiteralParagraph(text=("""
            Jackson's final translation:
            million years into the sky is Ra Sun God
            sealed and buried for all time
            his Stargate
            """,)),
            HorizontalLine(),
            ParagraphLink(
                text="Wikipedia - Stargate (film) - Production",
                link="https://en.wikipedia.org/wiki/Stargate_(film)#Production",
            ),
            LiteralParagraph(text=("""
                literal translation of the text from Wikipedia:
                years million in sky this Ra as Aten (=sun disk)
                sealed buried enduringly and repeatedly
                door his to stars
            """,)),
            HorizontalLine(),
            ParagraphLink(
                text="steemit.com - @laylahsophia - EGYPTOLOGY: The Perception of Egypt in Movies, Part# 1 - 'In which Museum is the Stargate on Display?'",
                link="https://steemit.com/steemstem/@laylahsophia/egyptology-the-perception-of-egypt-in-movies-part-1-in-which-museum-is-the-stargate-on-display"
            ),
            LiteralParagraph(text=("""
                literal translation of the text from @laylahsophia:
                million times up in the sky is Ra in the sun disk
                by being sealed (and) buried for all time to eternity
                his gate of the stars
            """,)),
            HorizontalLine(),
            ParagraphLink(
                text="YouTube - EgyptologyLessons - Stargate Movie Hieroglyphs - Translation",
                link="https://youtu.be/8_r-jB7tDlk"
            ),
            LiteralParagraph(text=("""
                literal translation of the text from EgyptologyLessons:
                years 100'000*10 in this sky, Ra in the sun disk
                by his sealed and his burial forever to eternity
                his gate of the stars
            """,)),
        )),
    )),
    PageBlockTypeWriter(parts=(
        Paragraph(text=("""
            Unfortunately, we still cannot decipher the other set of symbols.
            The hieroglyphic text contains two names: Ra and "Doorway to Heaven".
            We attempted to match them to the name in the cover stone's cartouche, but without success.
        """,)),
        Paragraph(text=("""
            I know this is an important discovery, but without progress, it remains just an "unknown artifact" - something to hang on a wall and speculate about.
            What's worse, securing access to advanced equipment or collaborating with respected colleagues is becoming nearly impossible as our funding dries up.
        """,)),
        Paragraph(text=("""
            My daughter Catherine and I have been living in the same warehouse where we store all the artifacts.
            To help with our financial situation, she even took her first part-time job - cataloging items at the Cairo Museum.
            I've also been picking up odd jobs to bring in extra money.
            Just last week, I translated some Hebrew inscriptions for a French archeologist.
        """,), comment=(
            Paragraph(text=("Must have been Rene Belloq himself.",)),
            ParagraphLink(
                text="Wikipedia - Rene Belloq",
                link="https://en.wikipedia.org/wiki/List_of_Indiana_Jones_characters#Ren%C3%A9_Belloq",
            ),
        )),
        Paragraph(text=("""
            A few months after moving into this warehouse, I had a dream.
            In the dream, I was walking through the warehouse at night, as I sometimes do when I can't sleep.
            Suddenly, the ring began shaking and glowing, and a man jumped through it.
            He did a few rolls on the ground, looked at me, and then disappeared behind some crates.
            The dream felt so real and vivid that I wouldn't have thought it was a dream if it hadn't been so bizarre.
        """,), comment=(
            Paragraph(text=("Cameron Mitchell, the time traveler from SG: Continuum.",)),
        )),
        Paragraph(text=("""
            I cannot bear the thought of losing the chance to study this ring - it is my life's work.
            It is precious to me.
            That's why I'm reaching out to you.
        """,), comment=(
            Paragraph(text=("But this ring with its 6.7 meters diameter does not fit in any filthy pocketses.",)),
        )),
        Paragraph(text=("""
            You mentioned that the German government recently established the Ahnenerbe Institute, and that they're actively seeking ancient artifacts.
            While I deeply disagree with the path my fatherland has taken, this could be the only way to secure the money I need to continue my research.
        """,)),
        Paragraph(text=("""
            I no longer have any contacts in Germany - except for you.
            Could you try to arrange funding through the new institute?
            If you help with the paperwork, I'll make sure you receive your share.
            We could even propose a hypothesis about the Aryan race occupying Egypt before the Egyptian culture, if that's what it takes to persuade them.
        """,)),
        Paragraph(text=("""
            I'm desperate, and I trust you to understand why.
        """,)),
        LiteralParagraph(text=("""
            With kindest regards,
            Paul Langford
        """,)),
    )),
    # PageBlock(block_type=PageBlockType.QUOTATION, parts=(
    #     Paragraph(text=("𓂋𓐰𓈖𓐰𓊪𓆳𓏏𓐰𓏥𓆐𓐰𓎆𓂋𓐰𓈎𓃀𓎛𓅱𓏁𓇯𓐰𓈉𓊪𓅱𓂋𓐰𓂝𓁚𓅓𓇋𓏏𓐰𓈖𓇶",)),
    #     Paragraph(omit_space_before=True, text=("𓅓𓐍𓅓𓏏𓋩𓐠𓈖𓐰𓆑𓈎𓐰𓂋𓋴𓌟𓀜𓊭𓐰𓁀𓆑𓐰𓈖𓆓𓐳𓏏𓇾𓐰𓂋𓅘𓎛𓎛𓇳𓐰𓈇",)),
    #     Paragraph(omit_space_before=True, text=("𓋴𓇼𓃀𓊀𓈖𓐰𓏥𓋴𓃀𓄿𓇼𓐰𓇳𓏥𓐰𓆑",)),
    # ))  # with stacking characters
    PageBlock(parts=(
        Paragraph(text=("""
            Ahnenerbe - the Ancestral Heritage organization.
            Those were dark days filled with desperate actions.
        """,)),
        Paragraph(text=("""
            Ending a war is far more complex than it seems.
            It might appear straightforward - one side wins, the other loses and pays reparations.
            But even in defeat, the losing side remains: its people, economy, and society still exist, often scarred by war's aftermath.
            And a peace built on perceived injustice cannot endure.
            If the consequences of defeat feel unfair or punitive, resentment festers, and the foundations of lasting peace crumble.
        """,)),
        Paragraph(text=("""
            The aftermath of World War I (called just "the Great War" by that time) left Germany deeply humiliated by the Treaty of Versailles.
            It was inevitable that someone - perhaps an artist, attuned to the emotions of the people - would emerge to restore national pride.
            Yet, rather than fostering self-love, nationalism took a darker turn: fueling hatred towards others, racism, and the rise of Nazism.
        """,)),
        Paragraph(text=("""
            Adolf Hitler rose to power in the early 1930s by exploiting Germany's economic despair after the Great War and the Great Depression.
            Appointed Chancellor in 1933, he used propaganda, legal maneuvers, and violent suppression of opponents to consolidate absolute control.
            Central to Nazi ideology was the myth of the Aryan "master race" (and Germans being descendants of Aryans), which Hitler promoted to justify German dominance, territorial expansion, and the persecution of nations deemed "inferior."
            To lend pseudoscientific credibility to these racial theories, the SS founded the Ahnenerbe in 1935,
            a research organization that conducted global expeditions to "prove" Aryan supremacy through archaeology and history,
            though its findings were largely fabricated or distorted for propaganda purposes.
        """,)),
    )),
    PageBlock(parts=(
        HorizontalLine(),
        Paragraph(text=("""
            Anyway, I'm not writing any more summaries or access-restriction recommendations for now - until I find out what is going on here.
            Otherwise, I might also end up rewriting all of them later.
        """,)),
    )),
))


def main():
    PAGE.render(filename=__file__)


if __name__ == "__main__":
    main()
