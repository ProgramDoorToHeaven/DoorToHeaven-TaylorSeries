from tools import *

PAGE = Page(blocks=(
    PageBlockTypeWriter(parts=(
        Paragraph(text=("Dear Deitrich,",)),
        Paragraph(text=("""
            I've been working on the ancient ring for over 5 years and it feels like I haven't moved a bit. 
            The only success since its discovery has been the translation of the hieroglyphs on the cover stone.
        """,)),
        # From https://en.wikipedia.org/wiki/Stargate_%28film%29
        # r:n:p-rnp-t:Z2-I8:V20-r:q-b-H-w-W15-N1:N25-p-w-r:a-C1-m-i-t:n-N8
        # m-x-m-t-S20-Aa18-n:f-q:r-s-T19-A24-Q6:A55-f:n-D&t-tA:r-G21-H-H-ra:N23
        # s-sbA-b-O32-n:Z2-s-b-A-sbA:ra-Z2:f

        # MdC script
        #   https://oraec.github.io/corpus/mdc_to_unicode_converter.html
        #   https://www.leskoff.com/s01775-0
        #
        # TODO: Langford translation
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
        # literal translation of the text:
        # years million in sky this Ra as Aten (=sun disk)
        # sealed buried enduringly and repeatedly
        # door his to stars

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
            relative_path="../tools/img_common/cover-stone-hieroglyphs-1-ra.png",
            alternative_text="𓂋𓈖𓊪 𓆳 𓏏𓏥 𓆐𓎆 𓂋𓈎 𓃀 𓎛 𓅱 𓏁 𓇯𓈉 𓊪 𓅱 𓂋𓂝 𓁚 𓅓 𓇋 𓏏𓈖 𓇶",
        ),
        Image(
            relative_path="../tools/img_common/cover-stone-hieroglyphs-2-buried.png",
            alternative_text="𓅓 𓐍 𓅓 𓏏 𓋩 𓐠 𓈖𓆑 𓈎𓂋 𓋴 𓌟 𓂡 𓊭𓁀 𓆑𓈖 𓆓𓏏 𓇾𓂋 𓅘 𓎛 𓎛 𓇳𓈇",
        ),
        Image(
            relative_path="../tools/img_common/cover-stone-hieroglyphs-3-stargate.png",
            alternative_text="𓋴 𓇼 𓃀 𓊀 𓈖𓏥 𓋴 𓃀 𓄿 𓇼𓇳 𓏥𓆑",
        ),
        Paragraph(is_literal=True, text=("""
            ... TRANSLATION 
        """,)),
        # TODO https://steemit.com/steemstem/@laylahsophia/egyptology-the-perception-of-egypt-in-movies-part-1-in-which-museum-is-the-stargate-on-display
        Paragraph(text=("""
            I can feel that it is an important discovery, but without any successful research, it is just an "unknown artifact", a curiosity to hang on a wall and wonder about.
            Moreover, it is getting difficult to do any research with expensive equipment or with renowned colleagues when our funding is running dry.
        """,)),
        Paragraph(text=("""
            With my daughter Catherine, we've been living in the warehouse where we also store all the artifacts. 
            She even got her first part time job - cataloging items at the Cairo museum - to help with our financial situation. 
            I've also been doing some odd jobs to get us more money. 
            Like last week, I translated some Hebrew inscriptions for some French archeologist.
        """,)),
        Paragraph(text=("""
            I don't want to lose the opportunity to work on this ring.
            It is my life's work. 
            It is precious to me.
            And that's why I'm writing to you.
            You mentioned that the German government recently established the Ahnenerbe project and they are interested in various ancient artifacts.
            Even though I generally despise the way my fatherland recently decided to follow, it could help me with the research now.
            Could you please try to get some funding from them? 
            I don't have any contacts in Germany anymore.
            That is besides you.
            If you help with the paperwork, you can have your share.
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
))


def main():
    PAGE.render(filename=__file__)


if __name__ == "__main__":
    main()
