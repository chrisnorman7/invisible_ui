"""Session class."""

import logging, sys, pygame
from handler import Handler

class Session(object):
 """
 Used to handle all events.
 
 You should instanciate a Session for every project that uses invisible_ui.
 
 Override Session.step to run code between each iteration of the main while loop.
 
 Important functions:
 main_loop - Main game loop.
 
 add_keydown - Adds a keydown event to be trapped by the session.
 
 add_keyup - Adds a keyup event to be handled by the session.
 
 add_handler - Adds an event handler to this session.
 
 remove_handler - Remove an event handler from this session.
 
 do_quit - A factory function which by default is bound to the pygame.QUIT event.
 
 handle_event - Handles all events caught by main_loop.
 
 do_pause - A function which pauses the game.
 
 do_unpause - A function which unpauses the game.
 
 toggle_pause - Toggle the state of self.running, calling self.do_pause and self.do_unpause as appropriate.
 
 Important properties:
 control - If this is not None, session.handle_event will pass any event received to self.control.handle_event(event).
 
 step - A function to be called with no arguments, and run after each iteration through the events from pygame.event.get().
 
 logger = The logger to which all tracebacks will be logged.
 
 running - If False, the game will be paused. Instead of setting this property manually, use the do_pause and do_unpause functions.
 
 Instead of handling the events yourself (unless you have a specific need to), use session.main_loop() after adding all the desired handlers, and let the session manage everything.
 """
 def __init__(self):
  """Initialise a new Session object."""
  self.logger = logging.getLogger('invisible_ui.Session')
  self._events = {}
  self.add_handler(pygame.QUIT, self.do_quit)
  self.control = None # handle events through this object first.
  self.step = lambda: None
  self.running = True # While True, the game will continue.
 
 def get_events(self):
  """Return all event handlers."""
  return self._events
 
 def do_quit(self, handler = None):
  """Quit the game."""
  self.logger.info('Quitting.')
  pygame.quit()
  sys.exit()
 
 def main_loop(self):
  """Runs the main game loop."""
  while 1:
   for e in pygame.event.get():
    self.handle_event(e)
   self.step()
 
 def handle_event(self, event):
  """Handle an event."""
  self.logger.debug('Handle event: %s.', event)
  if self.control:
   return self.control.handle_event(event)
  for h in self._events.get(event.type, []):
   handle = True # Innocent until proven guilty.
   for k, v in h.params.items():
    if getattr(event, k, v) != v:
     handle = False
     break
   if handle:
    h.call_func()
 
 def add_handler(self, type, handler, docstring = None, **kwargs):
  """
  Add an event handler to be processed by this session.
  
  type - The type of the event (pygame.QUIT, pygame.KEYUP ETC).
  
  handler - The function which should be called when an event matching this specification is received.
  
  docstring - See the documentation for Handler.__init__ for details.
  
  kwargs - An arbitrary number of parameters which must be satisfied in order for the event to match.
  
  Example:
  
  session.add_handler(pygame.QUIT, session.do_quit)
  
  session.add_handler(pygame.KEYDOWN, lambda: ao2.speak('You pressed the enter key.'), key = pygame.K_RETURN)
  """
  l = self._events.get(type, [])
  h = Handler(self, type, kwargs, handler, docstring)
  l.append(h)
  self._events[type] = l
  return h
 
 def remove_handler(self, handler):
  """
  Remove a handler from the list.
  
  handler - The handler (as returned by add_handler) to remove.
  
  Returns True on success, False otherwise.
  """
  try:
   self._events[handler.type].remove(handler)
   return True
  except ValueError:
   return False
 
 def add_keydown(self, handler, **kwargs):
  """
  Add a pygame.KEYDOWN event handler.
  
  handler - The function to be called when this key is pressed.
  kwargs - The kwargs to be passed to self.add_handler.
  
  See the documentation for self.add_handler for examples.
  """
  return self.add_handler(pygame.KEYDOWN, handler, **kwargs)
 
 def add_keyup(self, handler, **kwargs):
  """See the documentation for self.add_keydown."""
  return self.add_handler(pygame.KEYUP, handler, **kwargs)
 
 def do_pause(self, handler = None):
  """Pause the game by setting self.running to False."""
  self.running = False
  self.logger.debug('Paused.')
 
 def do_unpause(self, handler = None):
  """Unpause the game by setting self.running to True."""
  self.running = True
  self.logger.debug('Unpaused.')
 
 def toggle_paused(self, handler = None):
  """Toggles the paused state of the game."""
  if self.running:
   self.do_pause()
  else:
   self.do_unpause()
