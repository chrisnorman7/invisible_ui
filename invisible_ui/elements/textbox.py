"""Textbox class."""

import pygame

from invisible_ui.elements.element import Element


class Textbox(Element):
    """An editable text box."""

    def __init__(self, parent, title, value="", hidden=False,
                 allowedChars=r"""abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ 1234567890!"$%^&*()[]{},.<>;:"@#~\|/?-_=+`"""):
        """If hidden is True then the characters will not be spoken as they are typed."""
        super().__init__(parent, title)
        self.value = value
        self.hidden = hidden
        self.allowedChars = allowedChars
        self.type = "Edit"
        self.help = "You can type into this field."

    def handle_event(self, event):
        """Handle an event."""
        if event.type == pygame.KEYDOWN:
            v = event.unicode
            if event.key == pygame.K_BACKSPACE:
                if self.value:
                    v = self.value[-1]
                    if v == " ":
                        v = "space"
                    elif self.hidden:
                        v = "Hidden"
                    self.ao2.speak("Deleted %s" % v)
                    self.value = self.value[:-1]
                else:
                    self.ao2.speak("No text to delete.")
                return True
            elif v and v in self.allowedChars:
                self.value += v
                self.ao2.speak(
                    "Hidden" if self.hidden else (
                        "space" if v == " " else v))
                return True
            else:
                return False

    def get_title(self):
        if self.hidden:
            length = len(self.value)
            quantitySpecifier = (" value" if length == 1 else " values")
            return "{0} {1} {2}".format(super().get_title(), length, quantitySpecifier)

        return "{0} {1}".format(super().get_title(), self.value)
