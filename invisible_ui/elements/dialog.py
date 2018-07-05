"""Dialog class."""

from invisible_ui.elements.list import List


class Dialog(List):
    """Contains a label and a dismiss button."""

    def __init__(self, parent, title, message, button=None):
        super().__init__(parent, title)
        self.help = 'This is a dialog box.'
        self.type = 'dialog'
        self.add_item(Label(message))
        if not button:
            button = Button('OK', do_cancel)
        self.add_item(button)
