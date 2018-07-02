"""Simple dialog class."""

from invisible_ui.elements import Dialog
from invisible_ui.elements import Button
from invisible_ui.elements import Label
from invisible_ui.extras.cancelButton import CancelButton


class SimpleDialog(Dialog):
    """Always use the same button."""

    def __init__(self, parent, title, message, buttonName="OK"):
        super().__init__(parent, title, message, CancelButton(buttonName))
