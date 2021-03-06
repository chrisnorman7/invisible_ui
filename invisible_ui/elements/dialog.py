"""Dialog class."""

import logging
import pygame

from invisible_ui.interfaces import IContainer
from invisible_ui.elements.element import Element


class Dialog(IContainer, Element):

    def __init__(self, parent, title):
        if not isinstance(parent, IContainer):
            raise TypeError("Parent Element for dialogs must be of type IContainer.")

        Element.__init__(self, parent, title, type="Dialog", logger=logging.getLogger("Dialog"), help="Press tab or shift tab to navigate to the next element")

        self._control = None
        self._uiElements = []
        self._index = 0

        # Bind actions to key events.
        self.add_keydown(self.cancel, key=pygame.K_ESCAPE)
        self.add_keydown(self.previous, key=pygame.K_TAB, mod=(lambda v: v == pygame.KMOD_LSHIFT or v == pygame.KMOD_RSHIFT))
        self.add_keydown(self.next, key=pygame.K_TAB)

    def setup(self):
        super().selected()
        self._control = self.get_current_element()
        self.selected(interrupt=False)
        self.parent.control = self

    def cancel(self, event):
        """Close this dialog by handing focus back to the parent container."""
        self.parent.reset_control()

    @property
    def control(self):
        return self._control

    @control.setter
    def control(self, e):
        if not isinstance(e, Element):
            raise TypeError("Dialog.control can only point at objects of type Element.")

        self._control = e

    # Override
    def add(self, e):
        if not isinstance(e, Element):
            raise TypeError("Only objects of type Element can be added to the dialog.")
        
        self._uiElements.append(e)

    # Override
    def remove(self, e):
        if not isinstance(e, Element):
            raise TypeError("The given object to remove must be of type Element.")

        try:        
            self._uiElements.remove(e)
            return True
        except ValueError:
            return False

    # Override
    def next(self, event):
        if len(self._uiElements) > 0:
            self._index += 1
            self._index %= len(self._uiElements)
            self.set_control(self._uiElements[self._index])

    # Override
    def previous(self, event):
        if len(self._uiElements) > 0:
            self._index -= 1
            self._index %= len(self._uiElements)
            self.set_control(self._uiElements[self._index])

    # Override
    def get_current_element(self):
        if len(self._uiElements) == 0:
            return None

        return self._uiElements[self._index]

    # Override
    def set_control(self, e):
        self.control = e
        self.selected(interrupt=False)

    # Override
    def reset_control(self):
        self._control = self.get_current_element()

    # Override
    def selected(self, interrupt=True):
        self._uiElements[self._index].selected(interrupt)

    # Override
    def handle_event(self, event):
        if self._control is not None and self._control.handle_event(event):
            return True

        return super().handle_event(event)
