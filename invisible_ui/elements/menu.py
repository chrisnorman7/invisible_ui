"""Menu class."""

from . import cancel, Element
import pygame

class Menu(Element):
 """A control which can be scrolled with the arrow keys."""
 def __init__(self, session, title, autoselect = True):
  """
  Instanciate a menu.
  
  session - The session to attach this menu to.
  
  title - The title of the menu.
  
  autoselect - Automatically run self.selected when created.
  """
  super(Menu, self).__init__(title)
  self.type = 'Menu'
  self.session = session
  self._position = -1 # The user's position in the menu.
  self._items = []
  self.help = 'Use the arrow keys to move up and down in the menu and escape to exit.'
  session.control = self
  if autoselect:
   self.selected()
 
 def add_item(self, item):
  """Add an item to the menu."""
  if isinstance(item, Element):
   self._items.append(item)
  else:
   raise TypeError('Only objects of type Element can be added to menus.')
 
 def get_current_control(self):
  """Gets the currently selected control."""
  if self._position == None:
   return None
  else:
   return self._items[self._position]
 
 def handle_event(self, event):
  """Handle an event."""
  if event.type == pygame.KEYDOWN:
   if event.key == pygame.K_UP:
    self.do_up()
   elif event.key == pygame.K_DOWN:
    self.do_down()
   elif event.key == pygame.K_ESCAPE:
    cancel(self.session)
   else:
    c = self.get_current_control()
    if c:
     return c.handle_event(event)
 
 def get_position(self):
  """Get the current position."""
  return self._position
 
 def set_position(self, pos):
  """Set the user's position in the menu."""
  l = len(self._items)
  if not l:
   raise ValueError('There are no items in this menu.')
  else:
   if pos >= l or pos < -1:
    pos = 0
    self.selected()
   elif pos < 0:
    pos = l - 1
   self._position = pos
   self.get_current_control().selected()
 
 def do_up(self):
  """Move up the menu."""
  self.set_position(self.get_position() - 1)
 
 def do_down(self):
  """Move down in the menu."""
  self.set_position(self.get_position() + 1)
