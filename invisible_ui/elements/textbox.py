
import pygame

from invisible_ui.elements.element import Element


class Textbox(Element):

    def __init__(self, parent, title, value="", hidden = False,
            allowedChars="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ 1234567890!\"$\%^&*()[]{},.<>;:\'@#~\\|/?-_=+`"):
        super().__init__(parent, title)
        
        self.help = "You can type into this field."
        self.type = "Edit"
        self._hidden = hidden
        self._value = value
        self._allowedChars = allowedChars
        self._cursor = 0

        # bind actions to key events 
        self.deleteCharHandler = self.add_keydown(self.delete_char, key=pygame.K_BACKSPACE)
        self.nextCharHandler = self.add_keydown(self.next_char, key=pygame.K_RIGHT)
        self.previousCharHandler = self.add_keydown(self.previous_char, key=pygame.K_LEFT)
        self.getValueHandler = self.add_keydown(self.get_value, key=(lambda v: v == pygame.K_UP or v == pygame.K_DOWN))
        self.setHomeHandler = self.add_keydown(self.set_home, key=pygame.K_HOME)
        self.setEndHandler = self.add_keydown(self.set_end, key=pygame.K_END)
        self.add_keydown(self.type_char, unicode=(lambda v, allowedChars=self._allowedChars: v != "" and v in allowedChars))

    def set_cursor(self, index):
        v = ""
        
        if self._value == "":
            self._cursor = 0
            return "blank"
        elif index < 0:
            self._cursor = 0
            return "blank"
        elif index >= len(self._value):
            self._cursor = len(self._value)
            return "blank"
        else:
            self._cursor = index
            
            c = self._value[self._cursor]
            
            if c == " ":
                c = "space"
            
            return c

    def type_char(self, event):
        char = event.unicode
        c = ""

        if self._cursor == len(self._value):
            self._value += char
        else:
            self._value = self._value[:self._cursor] + char + self._value[self._cursor:]
        
        self.set_cursor(self._cursor + 1)
        
        if self._hidden:
            c = "hidden"
        elif char == " ":
            c = "space"
        else:
            c = char

        self.ao2.speak(c, interrupt=True)

    def delete_char(self, event):
        c = ""
        
        if (self._cursor - 1) < 0:
            c = "blank"
        else:
            if (self._cursor - 1) >= 0:
                c = self._value[self._cursor-1]
                self._value = self._value[:self._cursor-1] + self._value[self._cursor:]
                self.set_cursor(self._cursor - 1)
                
                if c == " ":
                    c = "space"

                if self._hidden:
                    c = "hidden"
        
        self.ao2.speak(c, interrupt=True)

    def next_char(self, event):
        c = ""
        
        if self._hidden:
            c = self.set_cursor(self._cursor + 1)
            
            if c != "blank":
                c = "hidden"
        else:
            c = self.set_cursor(self._cursor + 1)
        
        self.ao2.speak(c, interrupt=True)

    def previous_char(self, event):
        c = ""
        
        if self._hidden:
            c = self.set_cursor(self._cursor - 1)
            
            if c != "blank":
                c = "hidden"
        else:
            c = self.set_cursor(self._cursor - 1)
        
        self.ao2.speak(c, interrupt=True)

    def set_home(self, event):
        c = self.set_cursor(0)
        if self._hidden:
            c = "hidden"
        
        self.ao2.speak(c, interrupt=True)

    def set_end(self, event):
        c = self.set_cursor(len(self._value))
        self.ao2.speak(c, interrupt=True)

    def get_value(self, event):
        self.ao2.output(self._value, interrupt=True)

    # override
    def get_title(self):
        if self._hidden:
            length = len(self._value)
            quantitySpecifier = (" value" if length == 1 else " values")
            return "{0} {1} {2}".format(super().get_title(), length, quantitySpecifier)

        return "{0} {1}".format(super().get_title(), self._value)

    @property
    def value(self):
        return self._value
