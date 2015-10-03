"""Int textbox class."""

from ..elements import Textbox

class IntTextbox(Textbox):
 """A text box that only allows integers."""
 def __init__(self, *args, **kwargs):
  kwargs['allowed_chars'] = '1234567890'
  super(IntTextbox, self).__init__(*args, **kwargs)
 
 def get_value(self):
  """Returns the value of this field as an integer."""
  return int(self.value) if self.value else 0
