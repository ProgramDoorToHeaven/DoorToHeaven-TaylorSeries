from tools import *

PAGE = Page(blocks=(
    PageBlockTypeWriter(parts=(
        Paragraph(text=("Dear Deitrich,",)),
        Paragraph(text=("""
            I've been working on the ancient ring for over 5 years and it feels like I haven't moved a bit. 
            The only success since it's discovery has been the translation of the hieroglyphs on the cover stone.
        """,)),
        Paragraph(text=("""
            ... HIEROGLYPHS
            ... TRANSLATION 
        """,)),  # TODO
        Paragraph(text=("""
            I can feel that it is an important discovery, but without any successful research, it is just an "unknown artifact", a curiosity to hang on a wall and wonder about.
            Moreover, it is getting difficult to do any research with expensive equipment or with renowned colleagues when our finding is running dry.
        """,)),
        Paragraph(text=("""
            With my daughter Catherine, we've been living in the warehouse where we have all the artifacts. 
            She even got her first part time job - cataloging items at the Cairo museum - to help with our financial situation. 
            I've also been doing some odd jobs to get us more money. 
            Like last week, I translate some Hebrew inscriptions for some French archeologist.
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
))


def main():
    PAGE.render(filename=__file__)


if __name__ == "__main__":
    main()
