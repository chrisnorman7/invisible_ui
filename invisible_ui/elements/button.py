"""Button class."""

from . import Element
import pygame

class Button(Element):
 """Perform an action when the enter key is pressed."""
 def __init__(self, title, action):
  """Action will be called when the enter key is pressed."""
  super(Button, self).__init__(title)
  self.type = 'Button'
  self.help = 'Press enter or space to activate this button.'
  self.handled_keys[pygame.K_RETURN] = action
  self.handled_keys[pygame.K_SPACE] = action
