"""The Element class inherited from all invisible_ui elements."""

import logging

from accessible_output2.outputs.auto import Auto 
import pygame

from invisible_ui.events import EventManager


class Element(EventManager):
    """The object from which all elements are derived."""

    def __init__(self, parent, title, type, logger=None, help="Object usage instructions go here."):
        """Set the title, type, logger, and help for this item."""
        super().__init__(logger)

        if not isinstance(parent, EventManager):
            raise TypeError("Parent must be of type EventManager")

        self.parent = parent
        self.title = title
        self.help = help
        self.ao2 = Auto()
        self._type = type

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, type):
        if type == "":
            raise ValueError("You can not set the type for any element to an empty string.")

        self._type = type

    def get_title(self):
        """Get the title."""
        return "{0} {1}".format(self.title, self.type)

    def selected(self, interrupt=False):
        """This object has been selected."""
        self.ao2.output(self.get_title(), interrupt=interrupt)

    def get_help(self):
        """Show help for this control."""
        self.ao2.output(self.help)

    # override
    def handle_event(self, event):
        """Return True if the event was handled by this control, False otherwise."""
        return super().handle_event(event)

    def __str__(self):
        """Return the data for this class for printing"""
        return "{0} - (type: {1} title: {2} help: {3})".format(self.__class__, self.type, self.title, self.help)
