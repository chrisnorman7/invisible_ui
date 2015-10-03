"""Dialog class."""

from .menu import Menu

class Dialog(Menu):
 """Contains a label and a dismiss button."""
 def __init__(self, title, message, button = None):
  super(Dialog, self).__init__(title)
  self.help = 'This is a dialog box.'
  self.type = 'dialog'
  self.add_item(Label(message))
  if not button:
   button = Button('OK', do_cancel)
  self.add_item(button)
