"""Checkbox class."""

from invisible_ui.elements.button import Button


class Checkbox(Button):
    """A toggleable checkbox."""

    def __init__(self, parent, title, value=False, state_checked='checked',
                 state_unchecked='unchecked'):
        """Set the title and the initial state."""
        super().__init__(parent, title, self.activate)
        self.type = 'Checkbox'
        self.value = value
        self.state_checked = state_checked
        self.state_unchecked = state_unchecked
        self.help = 'Press enter or space to toggle the value.'

    def activate(self):
        """Toggle the state."""
        self.value = not self.value
        self.selected()

    def get_title(self):
        return '%s %s' % (super(Checkbox, self).get_title(
        ), self.state_checked if self.value else self.state_unchecked)
