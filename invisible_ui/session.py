"""Session class."""

import logging
import sys

import pygame

from invisible_ui.events import EventManager
from invisible_ui.elements.element import Element


class Session(EventManager):
    """
    Used to handle all events. You should instantiate a Session for every project that uses invisible_ui.

    public methods:
    main_loop - Main game loop.

    step - A method to be called with no arguments, and run after each iteration through the events from pygame.event.get().

    handle_event - overwritten method from EventManager, handles all events caught by main_loop.

    do_quit - A factory method which by default is bound to the pygame.QUIT event.

    do_pause - A method which pauses the game.

    do_unpause - A method which unpauses the game.

    toggle_pause - Toggle the state of self.running, calling self.do_pause and self.do_unpause as appropriate.

    Public properties:
    control - If this is not None, session.handle_event will pass any event received to self.control.handle_event(event).

    logger = The logger to which all tracebacks will be logged.

    running - If False, the game will be paused. Instead of setting this property manually, use the do_pause and do_unpause methods.

    Instead of handling the events yourself (unless you have a specific need to), use session.main_loop() after adding all the desired handlers, and let the session
    manage everything.
    """

    def __init__(self):
        """Initialise a new Session object."""
        super().__init__()
        self.logger = logging.getLogger("invisible_ui.Session")
        self._events = {}
        self._control = None  # handle events through this object first.
        self.running = True  # While True, the game will continue.
        self.add_handler(pygame.QUIT, self.do_quit)

    def main_loop(self):
        """Runs the main game loop."""
        while True:
            for e in pygame.event.get():
                self.handle_event(e)

            self.step()
            pygame.time.wait(5)

    def handle_event(self, event):
        """Handle an event."""
        if self.control is not None:
            self.control.handle_event(event)

        return super().handle_event(event)

    def step(self):
        """Method to be overwritten, to be called at the end of each iteration of the main loop."""
        pass

    @property
    def control(self):
        return self._control

    @control.setter
    def control(self, e):
        if not isinstance(e, EventManager) and e is not None:
            raise TypeError("Control can only point at objects of type Element.")

        self._control = e

    def do_quit(self, event, func=None):
        """Quit the game, and call the handler function passed in if is not None"""
        if func is not None:
            func(event)

        self.logger.info("Quitting.")
        pygame.quit()
        sys.exit()

    def do_pause(self, handler=None):
        """Pause the game by setting self.running to False."""
        self.running = False
        self.logger.debug("Paused.")

    def do_unpause(self, handler=None):
        """Unpause the game by setting self.running to True."""
        self.running = True
        self.logger.debug("Unpaused.")

    def toggle_paused(self, handler=None):
        """Toggles the paused state of the game."""
        if self.running:
            self.do_pause()
        else:
            self.do_unpause()
