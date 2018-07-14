"""Group class."""

import logging 

from invisible_ui.elements.button import Button


class Group(Button):
    """Choose from a list of pre-defined values."""

    def __init__(self, parent, title, values, index=0):
        """Set the possible values for this control."""
        super().__init__(parent, title, self.activate)
        if len(values):
            self._values = values
        else:
            raise ValueError("You must provide at least one value.")

        self._index = index
        self._selection = values[index]
        self.help = "Press enter or space to change the value."
        self.type = "Group"
        self.logger=logging.getLogger("Group")

    def activate(self, event):
        """Change the value."""
        self._index += 1
        if self._index >= len(self._values):
            self._index = 0

        self._selection = self._values[self._index]
        self.ao2.speak(self._selection)

    @property
    def selection(self):
            return self._selection

    # Override 
    def get_title(self):
        return "{0} ({1} selected)".format(super().get_title(), self._values[self._index])
