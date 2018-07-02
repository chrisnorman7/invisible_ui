"""Group class."""

from invisible_ui.elements.button import Button


class Group(Button):
    """Choose from a list of pre-defined values."""

    def __init__(self, parent, title, values, value=0):
        """Set the possible values for this control."""
        super().__init__(parent, title, lambda event: self.activate())
        if len(values):
            self.values = values
        else:
            raise ValueError("You must provide at least one value.")
        self.value = value
        self.help = "Press enter or space to change the value."
        self.type = "Group"

    def activate(self):
        """Change the value."""
        self.value += 1
        if self.value >= len(self.values):
            self.value = 0
        self.ao2.speak(self.values[self.value])

    # Override 
    def get_title(self):
        return "{0} ({1} selected)".format(super(Group, self).get_title(), self.values[self.value])
