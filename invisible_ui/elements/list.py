
import pygame 

from invisible_ui.elements.element import Element


class List(Element):

    def __init__(self, parent, title, help="Use the arrow keys to navigate to select your choice.", autoSelect=True, doesWrap=True):
        super().__init__(parent, title, help=help)
        
        self._autoSelect = autoSelect
        self._doesWrap = doesWrap
        self.type = "List"
        self._position = -1
        self._items = []
        
        if self._autoSelect:
            self._position = 0

        # Bind actions to key events.
        self.previousItemHandler = self.add_keydown(self.previous_item, key=pygame.K_UP)
        self.nextItemHandler = self.add_keydown(self.next_item, key=pygame.K_DOWN)
        self.selectFirstItemHandler = self.add_keydown(self.select_first_item, key=pygame.K_HOME)
        self.selectLastItemHandler = self.add_keydown(self.select_last_item, key=pygame.K_END)

    def add_item(self, item):
        if isinstance(item, Element):
            self._items.append(item)
        else:
            raise TypeError("Menu items must be of type Element")

    def remove_item(self, item):
        if item is None or not isinstance(item, Element):
            raise IndexError("The given item can not be None, and must be of type Element")

        try:
            self._items.remove(item)
        except ValueError as v:
            raise v

    def get_current_control(self):
        return self._items[self._position]

    # Override
    def handle_event(self, event):
        if super().handle_event(event):
            return True

        control = self.get_current_control()
        return control is not None and control.handle_event(event)

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
        else:
            if self._doesWrap:
                self._position = pos % length  
            else:
                if pos >= length:
                    self._position = length - 1
                elif pos < 0:
                    self._position = 0
                else:
                    self._position = pos
        
        c = self.get_current_control()
        if c is not None:
            c.selected()

    def next_item(self, event):
        self.position += 1

    def previous_item(self, event):
        self.position -= 1

    def select_first_item(self, event):
        self._position = 0
        self.get_current_control().selected()

    def select_last_item(self, event):
        self._position = len(self._items) - 1
        self.get_current_control().selected()

    # Override
    def selected(self, interrupt=True):
        self.ao2.output(self.get_title(), interrupt=interrupt)
        self.ao2.output(self.get_current_control().get_title(), interrupt=False)

