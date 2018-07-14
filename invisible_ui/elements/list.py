
import logging 

import pygame 

from invisible_ui.elements.element import Element
from invisible_ui.interfaces import IContainer


class List(IContainer, Element):

    def __init__(self, parent, title, help="Use the arrow keys to navigate to select your choice.", autoSelect=True, doesWrap=True):
        Element.__init__(self, parent, title, "List", logging.getLogger("List"), help)
        
        self._autoSelect = autoSelect
        self._doesWrap = doesWrap
        self._position = -1
        self._items = []
        self._control = None

        if self._autoSelect:
            self._position = 0

        # Bind actions to key events.
        self.previousItemHandler = self.add_keydown(self.previous, key=pygame.K_UP)
        self.nextItemHandler = self.add_keydown(self.next, key=pygame.K_DOWN)
        self.selectFirstItemHandler = self.add_keydown(self.select_first_item, key=pygame.K_HOME)
        self.selectLastItemHandler = self.add_keydown(self.select_last_item, key=pygame.K_END)

    def select_first_item(self, event):
        self._position = 0
        self._control.selected()

    def select_last_item(self, event):
        self._position = len(self._items) - 1
        self._control.selected()

    @property
    def control(self):
        return self._control

    @control.setter
    def control(self, e):
        if not isinstance(e, Element):
            raise TypeError("List.control can only point at objects of type Element.")

        self._control = e

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, pos):
        length = len(self._items)
        
        if length == 0:
            ao2.output("Empty Menu")
        elif self._position == -1:
            self._position = 0
            c = self.get_current_element()
            self.set_control(c)
        else:
            if self._doesWrap:
                self._position = pos % length  
                c = self.get_current_element()
                self.set_control(c)
            else:
                if pos >= length:
                    self._position = length - 1
                elif pos < 0:
                    self._position = 0
                else:
                    self._position = pos
                    c = self.get_current_element()
                    self.set_control(c)

    # Override
    def add(self, item):
        if not isinstance(item, Element):
            raise TypeError("Menu items must be of type Element")

        self._items.append(item)

        if len(self._items) == 1:
            self._control = self.get_current_element()

    # Override
    def remove(self, item):
        if item is None or not isinstance(item, Element):
            raise IndexError("The given item can not be None, and must be of type Element")

        try:
            self._items.remove(item)
            return True
        except ValueError:
            return False

    # Override
    def next(self, event):
        self.position += 1

    # Override
    def previous(self, event):
        self.position -= 1

    # Override 
    def get_current_element(self):
        if len(self._items) == 0:
            return None

        return self._items[self._position]

    # Override
    def set_control(self, e):
        self._control = e
        self._control.selected()

    # Override
    def reset_control(self):
        self._control = self.get_current_element()

    # Override
    def selected(self, interrupt=True):
        self.ao2.output(self.get_title(), interrupt=interrupt)
        e = self.get_current_element()

        # This check insures that an item is not spoken if the position is -1.
        if self._position >= 0 and self._position < len(self._items):
            self.ao2.output(e.get_title(), interrupt=False)

    # Override
    def handle_event(self, event):
        if self._control is not None and self._control.handle_event(event):
            return True

        return super().handle_event(event)
