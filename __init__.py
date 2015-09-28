import pygame
from accessible_output2.outputs.auto import Auto
ao2 = Auto()

class Element(object):
 """The object from which all elements are derived."""
 def __init__(self, title, help = 'Object usage instructions go here.'):
  """Set the title for this item."""
  self.title = title
  self.help = help
  self.handled_keys = {pygame.K_F1: self.get_help} # The keydown messages this control responds to.
 
 def selected(self):
  """This object has been selected."""
  ao2.speak(self.title)
 
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

class Menu(Element):
 """A control which can be scrolledwith the arrow keys."""
 def __init__(self, title):
  """Give the title of the menu."""
  super(Menu, self).__init__(title + ' menu')
  self._position = None # The user's position in the menu.
  self._items = []
  self.help = 'Use the arrow keys to move up and down in the menu.'
 
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
   else:
    c = self.get_current_control()
    if c:
     return c.handle_event(event)
  return False
 
 def get_position(self):
  """Get the current position."""
  return self._position
 
 def set_position(self, pos):
  """Set the user's position in the menu."""
  l = len(self._items)
  if not l:
   raise ValueError('There are no items in this menu.')
  else:
   if pos >= l:
    pos = 0
    self.selected()
   elif pos < 0:
    pos = l - 1
   self._position = pos
   self.get_current_control().selected()
 
 def do_up(self):
  """Move up the menu."""
  p = self.get_position()
  if p == None:
   self.set_position(0)
  else:
   self.set_position(p - 1)
 
 def do_down(self):
  """Move down in the menu."""
  p = self.get_position()
  if p == None:
   self.set_position(0)
  else:
   self.set_position(self.get_position() + 1)

class Label(Element):
 """This element does nothing, and just acts as a header in menus ETC."""
 def __init__(self, title):
  """Set the title, and alter the help message."""
  super(Label, self).__init__(title + ' label')
  self.help = 'This object has no controls.'

class Button(Element):
 """Perform an action when the enter key is pressed."""
 def __init__(self, title, action):
  """Action will be called when the enter key is pressed."""
  super(Button, self).__init__(title + ' button')
  self.help = 'Press enter to activate this button.'
  self.action = action
  self.handled_keys[pygame.K_RETURN] = self.action
  self.handled_keys[pygame.K_SPACE] = self.action

if __name__ == '__main__':
 """Run a little example."""
 running = 1 # Keep the loop alive.
 
 def do_quit():
  """Terminate the program."""
  global running
  running = 0
  print('Exiting program.')
 
 screen = pygame.display.set_mode()
 m = Menu('Test')
 m.add_item(Label('This is a menu'))
 m.add_item(Button('OK', lambda: ao2.speak('You pressed the OK button.')))
 m.add_item(Button('Cancel', do_quit))
 m.selected()
 while running:
  for e in pygame.event.get():
   m.handle_event(e)
