
import logging

import pygame
from accessible_output2.outputs.auto import Auto

from invisible_ui.elements.element import Element
from invisible_ui.events import EventManager
from invisible_ui.interfaces import IContainer


class Window(IContainer, EventManager):

    def __init__(self, session, title=""):
        EventManager.__init__(self, logging.getLogger("Window"))

        self._uiElements = []
        self._index = 0
        self._session = session
        self._title = title
        self._control = None

        # Bind actions to events
        self.add_handler(pygame.QUIT, self.quit)
        self.add_keydown(self.quit, key=pygame.K_F4, mod=(lambda v: v == pygame.KMOD_LALT or v == pygame.KMOD_RALT))
        self.add_keydown(self.previous, key=pygame.K_TAB, mod=(lambda v: v == pygame.KMOD_LSHIFT or v == pygame.KMOD_RSHIFT))
        self.add_keydown(self.next, key=pygame.K_TAB)

    def setup(self):
        pygame.init()
        self.set_title(self._title)
        self._session.control = self
        screen = pygame.display.set_mode()

        # Select the first Element in the queue.
        self._control = self.get_current_element()
        self.selected(interrupt=False)

    def get_title(self):
        return self._title

    def set_title(self, title):
        pygame.display.set_caption(self._title)

    def selected(self, interrupt=True):
        self._uiElements[self._index].selected(interrupt)

    def quit(self, event):
        pygame.quit()
        self._session.quit(event)

    @property
    def control(self):
        return self._control

    @control.setter
    def control(self, e):
        if not isinstance(e, Element):
            raise TypeError("Window.control can only point at objects of type Element.")

        self._control = e

    # Override
    def add(self, e):
        if not isinstance(e, Element):
            raise TypeError("Only objects of type Element can be added to the Window.")
        
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
        self.selected(interrupt=False)

    # Override
    def handle_event(self, event):
        if self._control is not None and self._control.handle_event(event):
            return True

        return super().handle_event(event)
