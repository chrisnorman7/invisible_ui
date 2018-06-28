# -*-coding: latin-1

"""Textbox class."""

import pygame

from . import Element, ao2


class Textbox(Element):
    """An editable text box."""

    def __init__(self, title, value=u'', hidden=False,
                 allowed_chars=ur"""abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ 1234567890!"£$%^&*()[]{},.<>;:'@#~\|/?-_=+`¬"""):
        """If hidden is True then the characters will not be spoken as they are typed."""
        super(Textbox, self).__init__(title)
        self.value = value
        self.hidden = hidden
        self.allowed_chars = allowed_chars
        self.type = 'Edit'
        self.help = 'You can type into this field.'

    def handle_event(self, event):
        """Handle an event."""
        if event.type == pygame.KEYDOWN:
            v = event.unicode
            if event.key == pygame.K_BACKSPACE:
                if self.value:
                    v = self.value[-1]
                    if v == ' ':
                        v = 'space'
                    elif self.hidden:
                        v = 'Hidden'
                    ao2.speak('Deleted %s' % v)
                    self.value = self.value[:-1]
                else:
                    ao2.speak('No text to delete.')
                return True
            elif v and v in self.allowed_chars:
                self.value += v
                ao2.speak(
                    'Hidden' if self.hidden else (
                        'space' if v == ' ' else v))
                return True
            else:
                return False

    def get_title(self):
        l = len(self.value)
        return '%s %s' % (super(Textbox, self).get_title(), ('%s %s' % (
            l, 'value' if l == 1 else 'values')) if self.hidden else self.value)
