"""Simple dialog class."""

from ..elements import Dialog, Button, Label
from ..xtras.cancel_button import CancelButton

class SimpleDialog(Dialog):
 """Always use the same button."""
 def __init__(self, title, message, button_name = 'OK'):
  super(Dialog, self).__init__(title, message, CancelButton(button_name))
