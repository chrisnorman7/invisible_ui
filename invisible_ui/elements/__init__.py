"""Element classes."""

from accessible_output2.outputs.auto import Auto
import pygame

ao2 = Auto()


def cancel(session, message='Canceled.'):
    """Perform a cancel."""
    session.control = None
    if message:
        ao2.speak(message)


class Element(object):
    """The object from which all elements are derived."""

    def __init__(self, title, help='Object usage instructions go here.'):
        """Set the title and help for this item."""
        self.type = 'Element'
        self.value = None  # Place-holder value for the editable controls.
        self.title = title
        self.help = help
        # The keydown messages this control responds to.
        self.handled_keys = {pygame.K_F1: self.get_help}

    def get_title(self):
        """Get the title."""
        return '%s %s' % (self.title, self.type)

    def selected(self):
        """This object has been selected."""
        ao2.speak(self.get_title())

    def get_help(self):
        """Show help for this control."""
        ao2.speak(self.help)

    def handle_event(self, event):
        """Return True if the event was handled by this control, False otherwise."""
        if event.type == pygame.KEYDOWN:
            if event.key in self.handled_keys:
                self.handled_keys[event.key]()
                return True
        return False


from invisible_ui.elements.button import Button
from invisible_ui.elements.checkbox import Checkbox
from invisible_ui.elements.dialog import Dialog
from invisible_ui.elements.group import Group
from invisible_ui.elements.label import Label
from invisible_ui.elements.menu import Menu
from invisible_ui.elements.textbox import Textbox
