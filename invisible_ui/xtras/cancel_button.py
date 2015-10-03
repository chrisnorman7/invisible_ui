"""Cancel button class."""

from ..elements import Button, cancel

class CancelButton(Button):
 def __init__(self, session, title = 'Cancel', action = None):
  """
  Create a cancel button.
  
  session - The session who's control attribute should be cleared.
  
  title - The title of this button.
  
  action - The action to be called when this button is activated.
  """
  if not action:
   action = lambda s = session: cancel(s)
  super(CancelButton, self).__init__(title, action)
