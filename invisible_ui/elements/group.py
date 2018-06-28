"""Group class."""

from .button import Button
from . import ao2


class Group(Button):
    """Choose from a list of pre-defined values."""

    def __init__(self, title, values, value=0):
        """Set the possible values for this control."""
        super(Group, self).__init__(title, self.activate)
        if len(values):
            self.values = values
        else:
            raise ValueError('You must provide at least one value.')
        self.value = value
        self.help = 'Press enter or space to change the value.'
        self.type = 'Group'

    def activate(self):
        """Change the value."""
        self.value += 1
        if self.value >= len(self.values):
            self.value = 0
        ao2.speak(self.values[self.value])

    def get_title(self):
        return '%s (%s selected)' % (
            super(Group, self).get_title(), self.values[self.value])
