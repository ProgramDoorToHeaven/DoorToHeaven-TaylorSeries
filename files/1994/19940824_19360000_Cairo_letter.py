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
        #
        # Langford translation
        # SG1 s01e11 Torment of Tantalus
        # "doorway to heaven"
        #
        # Partial translation by Myers
        # time million sky Ra sun god
        # coffin forever to eternity
        # his door to heaven
        #
        # Jackson's final translation:
        # million years into the sky is Ra Sun God
        # sealed and buried for all time
        # his Stargate
        #
        # literal translation of the text from Wikipedia:
        # years million in sky this Ra as Aten (=sun disk)
        # sealed buried enduringly and repeatedly
        # door his to stars
        #
        # literal translation of the text from https://steemit.com/steemstem/@laylahsophia/egyptology-the-perception-of-egypt-in-movies-part-1-in-which-museum-is-the-stargate-on-display :
        # million times up in the sky is Ra in the sun disk
        # by being sealed (and) buried for all time to eternity
        # his gate of the stars
        #
        # literal translation of the text from https://www.youtube.com/watch?v=8_r-jB7tDlk :
        # years 100'000*10 in this sky, Ra in the sun disk
        # by his sealed and his burial forever to eternity
        # his gate of the stars

        # Paragraph(is_literal=True, text=("""
        #     𓂋𓈖𓊪 𓆳 𓏏𓏥 𓆐𓎆 𓂋𓈎 𓃀 𓎛 𓅱 𓏁 𓇯𓈉 𓊪 𓅱 𓂋𓂝 𓁚 𓅓 𓇋 𓏏𓈖 𓇶
        #     𓅓 𓐍 𓅓 𓏏 𓋩 𓐠 𓈖𓆑 𓈎𓂋 𓋴 𓌟 𓂡 𓊭𓁀 𓆑𓈖 𓆓𓏏 𓇾𓂋 𓅘 𓎛 𓎛 𓇳𓈇
        #     𓋴 𓇼 𓃀 𓊀 𓈖𓏥 𓋴 𓃀 𓄿 𓇼𓇳 𓏥𓆑
        # """,)),  # linearized
        # Paragraph(is_literal=True, text=("""
        #     𓂋𓐰𓈖𓐰𓊪𓆳𓏏𓐰𓏥𓆐𓐰𓎆𓂋𓐰𓈎𓃀𓎛𓅱𓏁𓇯𓐰𓈉𓊪𓅱𓂋𓐰𓂝𓁚𓅓𓇋𓏏𓐰𓈖𓇶
        #     𓅓𓐍𓅓𓏏𓋩𓐠𓈖𓐰𓆑𓈎𓐰𓂋𓋴𓌟𓀜𓊭𓐰𓁀𓆑𓐰𓈖𓆓𓐳𓏏𓇾𓐰𓂋𓅘𓎛𓎛𓇳𓐰𓈇
        #     𓋴𓇼𓃀𓊀𓈖𓐰𓏥𓋴𓃀𓄿𓇼𓐰𓇳𓏥𓐰𓆑
        # """,)),  # with stacking characters
        Image(
            relative_path="./img/cover-stone-hieroglyphs-1-1-years.png",
            alternative_text="𓂋𓈖𓊪 𓆳 𓏏𓏥 𓆐𓎆\n/\n𓂋𓐰𓈖𓐰𓊪𓆳𓏏𓐰𓏥𓆐𓐰𓎆",
        ),
        Image(
            relative_path="./img/cover-stone-hieroglyphs-1-2-sky.png",
            alternative_text="𓂋𓈎 𓃀 𓎛 𓅱 𓏁 𓇯𓈉 𓊪 𓅱\n/\n𓂋𓐰𓈎𓃀𓎛𓅱𓏁𓇯𓐰𓈉𓊪𓅱",
        ),
        Image(
            relative_path="./img/cover-stone-hieroglyphs-1-3-ra.png",
            alternative_text="𓂋𓂝 𓁚 𓅓 𓇋 𓏏𓈖 𓇶\n/\n𓂋𓐰𓂝𓁚𓅓𓇋𓏏𓐰𓈖𓇶",
        ),
        Image(
            relative_path="./img/cover-stone-hieroglyphs-2-1-buried.png",
            alternative_text="𓅓 𓐍 𓅓 𓏏 𓋩 𓐠 𓈖𓆑 𓈎𓂋 𓋴 𓌟 𓂡 𓊭𓁀 𓆑𓈖\n/\n𓅓𓐍𓅓𓏏𓋩𓐠𓈖𓐰𓆑𓈎𓐰𓂋𓋴𓌟𓀜𓊭𓐰𓁀𓆑𓐰𓈖",
        ),
        Image(
            relative_path="./img/cover-stone-hieroglyphs-2-2-forever.png",
            alternative_text="𓆓𓏏 𓇾𓂋 𓅘 𓎛 𓎛 𓇳𓈇\n/\n𓆓𓐳𓏏𓇾𓐰𓂋𓅘𓎛𓎛𓇳𓐰𓈇",
        ),
        Image(
            relative_path="./img/cover-stone-hieroglyphs-3-1-stargate.png",
            alternative_text="𓋴 𓇼 𓃀 𓊀 𓈖𓏥 𓋴 𓃀 𓄿 𓇼𓇳 𓏥𓆑\n/\n𓋴𓇼𓃀𓊀𓈖𓐰𓏥𓋴𓃀𓄿𓇼𓐰𓇳𓏥𓐰𓆑",
        ),
        Paragraph(text=("""
            The text mentions Ra - the god of the Sun - burying his "doorway to heaven" long ago.
            Therefore, the ring's name must be "Doorway to Heaven."
        """,)),
    )),
    PageBlockTypeWriter(parts=(
        Paragraph(text=("""
            Ok, so they called it "dorway to heaven" and we call it "door to heaven".
            Close enough.
            Guess we have a better translation half a century later.
        """)),
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
        """,)),
        Paragraph(text=("""
            I cannot bear the thought of losing the chance to study this ring - it is my life's work.
            It is precious to me.
            That's why I'm reaching out to you.
        """,)),
        Paragraph(text=("""
            You mentioned that the German government recently established the Ahnenerbe Institute, and that they're actively seeking ancient artifacts.
            While I deeply disagree with the path my fatherland has taken, this could be the only way to secure the funding I need to continue my research.
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
        Paragraph(is_literal=True, text=("""
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
            Those were dark days.
        """,)),
    )),
    PageBlock(parts=(
        Paragraph(text=("""
            Adolf Hitler rose to power in the early 1930s by exploiting Germany's economic despair after World War I and the Great Depression.
            Appointed Chancellor in 1933, he used propaganda, legal maneuvers, and violent suppression of opponents to consolidate absolute control.
            Central to Nazi ideology was the myth of the Aryan "master race" (and Germans being descendants of Aryans), which Hitler promoted to justify German dominance, territorial expansion, and the persecution of nations deemed "inferior."
            To lend pseudoscientific credibility to these racial theories, the SS founded the Ahnenerbe in 1935,
            a research organization that conducted global expeditions to "prove" Aryan supremacy through archaeology and history,
            though its findings were largely fabricated or distorted for propaganda purposes.
        """,)),
    )),
    PageBlock(parts=(
        Paragraph(text=("""
            Anyway, I'm not writing any more summaries or access-restriction recommendations until I find out what is going on here.
            Otherwise, I might also end up rewriting all of them later.
        """,)),
    )),
))


def main():
    PAGE.render(filename=__file__)


if __name__ == "__main__":
    main()
