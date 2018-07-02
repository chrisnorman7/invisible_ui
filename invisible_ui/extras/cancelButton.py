"""Cancel button class."""

from invisible_ui.elements import cancel
from invisible_ui.elements import Button


class CancelButton(Button):
    def __init__(self, parent, title='Cancel', action=None):
        """
        Create a cancel button.

        parent - The parent element who's control attribute should be cleared.

        title - The title of this button.

        action - The action to be called when this button is activated.
        """
        if not action:
            action = lambda event, s = parent: cancel(s)
        super().__init__(parent, title, action)
