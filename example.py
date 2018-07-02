if __name__ == "__main__":
    import logging
    import sys

    import pygame

    from invisible_ui import Session
    from invisible_ui.extras import IntTextbox
    from invisible_ui.elements import *

#    logging.basicConfig(stream=sys.stdout, level="DEBUG")


    class ExampleMenu(Menu):

        def __init__(self, session):
            super().__init__(session, "Example Menu")
            self.session = session
            self.add_item(Textbox(self, "Username"))
            self.add_item(Textbox(self, "Password", hidden=True))
            self.add_item(IntTextbox(self, "Age"))
            self.add_item(Group(self, "Level", ["User", "Special Person", "Administrator", "God"]))
            self.add_item(Button(self, "OK", (lambda event, s=self.session: session.do_quit()) ))


    class ExampleSession(Session):

        def __init__(self):
            super().__init__()
            self.add_keydown(self.do_quit, key=pygame.K_F4, mod=(lambda v: v == pygame.KMOD_LALT or v == pygame.KMOD_RALT))
            self.control = ExampleMenu(self)


    pygame.init()
    screen = pygame.display.set_mode()
    session = ExampleSession()
    session.main_loop()
