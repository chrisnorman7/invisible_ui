"""Checkbox class."""

import logging

from invisible_ui.elements.button import Button


class Checkbox(Button):
    """A toggleable checkbox."""

    def __init__(self, parent, title, value=False, stateChecked="checked", stateUnchecked="unchecked"):
        """Set the title and the initial state."""
        super().__init__(parent, title, self.activate)
        self.type = "Checkbox"
        self.logger = logging.getLogger("Checkbox")
        self.value = value
        self.stateChecked = stateChecked
        self.stateUnchecked = stateUnchecked
        self.help = "Press enter or space to toggle the value."

    def activate(self, event):
        """Toggle the state."""
        self.value = not self.value
        self.selected()

    def get_title(self):
        state = self.stateChecked if self.value else self.stateUnchecked
        return "{0} {1}".format(super().get_title(), state)
