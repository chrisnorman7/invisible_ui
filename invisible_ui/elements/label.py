"""Label class."""

from . import Element


class Label(Element):
    """This element does nothing, and just acts as a header in menus ETC."""

    def __init__(self, title):
        """Set the title, and alter the help message."""
        super(Label, self).__init__(title)
        self.type = 'Label'
        self.help = 'This object has no controls.'

    def get_title(self):
        """Get the title."""
        return '%s' % (self.title)
