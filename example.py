if __name__ == "__main__":
    import logging
    import sys

    import pygame

    from invisible_ui import Session
    from invisible_ui.extras import IntTextbox
    from invisible_ui.elements import *
    from invisible_ui.elements.list import List


#    logging.basicConfig(stream=sys.stdout, level="DEBUG")


    class ExampleMenu(List):

        def __init__(self, parent, session):
            super().__init__(parent, "Example", autoSelect=False, doesWrap=False)
            self.type = "menu"
            self.add_item(Textbox(self, "Username"))
            self.add_item(Textbox(self, "Password", hidden=True))
            self.add_item(IntTextbox(self, "Age"))
            self.add_item(Group(self, "Level", ["User", "Special Person", "Administrator", "God"]))
            self.add_item(Button(self, "OK", session.quit))

            l = List(self, "Test", doesWrap=False)
            l.add_item(Label(l, "1"))
            l.add_item(Label(l, "2"))
            l.add_item(Label(l, "3"))
            l.add_item(Label(l, "4"))
            l.change_event(l.nextItemHandler, key=pygame.K_RIGHT)
            l.change_event(l.previousItemHandler, key=pygame.K_LEFT)
            self.add_item(l)

            l2 = List(self, "Test", doesWrap=False)
            l2.add_item(Label(l2, "a"))
            l2.add_item(Label(l2, "b"))
            l2.add_item(Label(l2, "c"))
            l2.add_item(Label(l2, "d"))
            l2.change_event(l2.nextItemHandler, key=pygame.K_RIGHT)
            l2.change_event(l2.previousItemHandler, key=pygame.K_LEFT)
            self.add_item(l2)


    class ExampleSession(Session):

        def __init__(self):
            super().__init__()
            self.add_keydown(self.quit, key=pygame.K_F4, mod=(lambda v: v == pygame.KMOD_LALT or v == pygame.KMOD_RALT))
            self.control = ExampleMenu(self, self)


    pygame.init()
    screen = pygame.display.set_mode()
    session = ExampleSession()
    session.main_loop()
