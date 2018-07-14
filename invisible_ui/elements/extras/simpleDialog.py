"""Simple dialog class."""

from invisible_ui.elements import Dialog
from invisible_ui.elements import Button
from invisible_ui.elements import Label


class SimpleDialog(Dialog):
    """Always use the same button."""

    def __init__(self, parent, title, message, action, okButtonName="OK", cancelButtonName="Cancel"):
        super().__init__(parent, title)
        self.add(Label(self, message))
        self.add(Button(self, okButtonName, action))
        self.add(Button(self, cancelButtonName, self.cancel))
