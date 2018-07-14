if __name__ == "__main__":
    import logging
    import sys

    import pygame
    from accessible_output2.outputs.auto import Auto

    from invisible_ui import Session
    from invisible_ui import Window
    from invisible_ui.elements.extras import *
    from invisible_ui.elements import *


    #logging.basicConfig(stream=sys.stdout, level="DEBUG")


    class ListTextbox(Textbox):

        def __init__(self, parent, title, actions=None, hidden=False):
            super().__init__(parent, title, actions, hidden=hidden)
            self.remove_handler(self.getValueHandler)


    class ListIntTextbox(IntTextbox):

        def __init__(self, parent, title):
            super().__init__(parent, title)
            self.remove_handler(self.getValueHandler)


    class ExampleMenu(List):

        def __init__(self, parent):
            super().__init__(parent, "Example", autoSelect=True, doesWrap=False)

            self.type = "menu"

            self.usernameEditBox = ListTextbox(self, "Username", self.username_action)
            self.passwordEditBox = ListTextbox(self, "Password", self.password_action, hidden=True)
            self.ageEditBox = ListIntTextbox(self, "Age")
            self.levelGroup = Group(self, "Level", ["User", "Special Person", "Administrator", "God"])
            self.okButton = Button(self, "OK", parent.quit)

            # Create a horizontal list.
            l = List(self, "numbers", doesWrap=False)
            l.add(Label(l, "1"))
            l.add(Label(l, "2"))
            l.add(Label(l, "3"))
            l.add(Label(l, "4"))
            l.change_event_params(l.nextItemHandler, key=pygame.K_RIGHT)
            l.change_event_params(l.previousItemHandler, key=pygame.K_LEFT)

            # Create a second horizontal list.
            l2 = List(self, "letters", doesWrap=False)
            l2.add(Label(l2, "a"))
            l2.add(Label(l2, "b"))
            l2.add(Label(l2, "c"))
            l2.add(Label(l2, "d"))
            l2.change_event_params(l2.nextItemHandler, key=pygame.K_RIGHT)
            l2.change_event_params(l2.previousItemHandler, key=pygame.K_LEFT)

            self.add(self.usernameEditBox)
            self.add(self.passwordEditBox)
            self.add(self.ageEditBox)
            self.add(self.levelGroup)
            self.add(l)
            self.add(l2)
            self.add(self.okButton)

        def username_action(self, event):
            self.ao2.output("my username is " + self.usernameEditBox.value, interrupt=True)

        def password_action(self, event):
            self.ao2.output("my username is " + self.passwordEditBox.value, interrupt=True)


    class ExampleWindow(Window):

        def __init__(self, session):
            super().__init__(session, "Example UI.")

            self.ao2 = Auto()

            self.testLabel = Label(self, "This is an example label.")
            self.menu = ExampleMenu(self)
            self.dogCheckbox = Checkbox(self, "Like dogs?")
            self.openDialogButton = Button(self, "open Dialog", self.open_dialog)
            self.openSimpleDialog = Button(self, "Save", self.open_save_dialog)

            self.add(self.testLabel)
            self.add(self.menu)
            self.add(self.dogCheckbox)
            self.add(self.openDialogButton)
            self.add(self.openSimpleDialog)

        def open_dialog(self, event):
            dialog = Dialog(self, "My")
            favoriteGameBox = Textbox(self, "Favorite Game: ")
            gameTypeGroup = Group(self, "Game type", ("RPG", "Real Time Strategy", "Massive Multi Player Online"))
            okButton = Button(self, "OK",
                lambda event: self.ao2.output("Favorite game is " + favoriteGameBox.value + ". Favorite type is " + gameTypeGroup.selection + ".", interrupt=True))
            cancelButton = Button(self, "Cancel", dialog.cancel)

            dialog.add(favoriteGameBox)
            dialog.add(gameTypeGroup)
            dialog.add(okButton)
            dialog.add(cancelButton)
            dialog.setup()

        def open_save_dialog(self, event):
            dialog = SimpleDialog(self, "Warning", "Would you like to save before closing?", (lambda e: self.ao2.output("saving")))
            dialog.setup()

    class ExampleSession(Session):

        def __init__(self):
            super().__init__()
            self.add_keydown(self.quit, key=pygame.K_F4, mod=(lambda v: v == pygame.KMOD_LALT or v == pygame.KMOD_RALT))
            window = ExampleWindow(self)
            window.setup()


    session = ExampleSession()

    session.main_loop()
