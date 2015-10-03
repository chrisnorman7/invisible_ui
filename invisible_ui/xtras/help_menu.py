"""Help menu calss."""

from ..elements import Menu, Button, Label
import pygame

keys = {} # All the keys that pygame recognises.
for x in dir(pygame):
 if x.startswith('K_'):
  keys[getattr(pygame, x)] = x[2:]

def handle_keys(value):
 """Print appropriate values for KEYDOWN and KEYUP params."""
 key = value.get('key')
 if key:
  return keys.get(key, 'Unknown')
 else:
  return 'No key... bizarly'

class HelpMenu(Menu):
 """A help menu which displays help on all the bound events."""
 def __init__(self, handler, title = 'Command Help'):
  super(HelpMenu, self).__init__(handler.session, title)
  for type, handlers in handler.session.get_events().items():
   if type == pygame.QUIT:
    label = 'Quit (Click the Close button of the main game window)'
    func = lambda value: 'Quit'
   elif type == pygame.KEYDOWN:
    label = 'Key Down'
    func = handle_keys
   elif type == pygame.KEYUP:
    label = 'Key Up'
    func = handle_keys
   else:
    label = 'Unrecognised'
    func = lambda value: ', '.join(['%s = %s' % (x, y) for x, y in h.params.items()])
   self.add_item(Label(label))
   for h in handlers:
    self.add_item(Button('%s: %s' % (func(h.params), h.get_help()), h.call_func))
