"""Session class."""

import logging
import sys

import pygame

from invisible_ui.events import EventManager
from invisible_ui.window import Window


class Session(EventManager):
    """
    Used to handle all events. You should instantiate a Session for every project that uses invisible_ui.

    public methods:
    main_loop - Main game loop.

    step - A method to be called with no arguments, and run after each iteration through the events from pygame.event.get().
    This method is meant to be overritten, it is stubbed out by default.

    on_exit - a method that is called right before program execution has finished.
    This method is meant to be overritten, it is stubbed out by default.

    handle_event - overwritten method from EventManager, handles all events caught by main_loop.

    quit - A factory method which will stop the main loop and end the program naturally.

    stop_loop - A method which stops the main loop .

    resume_loop - A method which resumes the main loop.

    Public properties:
    control - If this is not None, session.handle_event will pass any event received to self.control.handle_event(event).

    running - If False, the game will be paused. Instead of setting this property manually, use the do_pause and do_unpause methods.

    Instead of handling the events yourself (unless you have a specific need to), use session.main_loop() after adding all the desired handlers, and let the session
    manage everything.
    """

    def __init__(self):
        """Initialise a new Session object."""
        super().__init__(logging.getLogger("invisible_ui.Session"))
        self._control = None  # handle events through this object first.
        self._running = True  # While True, the game will continue.

    def main_loop(self):
        """Runs the main game loop."""
        while True:
            for e in pygame.event.get():
                self.handle_event(e)

            self.step()
            pygame.time.wait(5)

    # Override
    def handle_event(self, event):
        """Handle an event."""
        if self._control is not None and             self._control.handle_event(event):
            return True

        return super().handle_event(event)

    def step(self):
        """Method to be overwritten, to be called at the end of each iteration of the main loop."""
        pass

    def on_exit(self):
        """Method to be overwritten, to be called at the end of program execution write before the program naturally ends."""
        pass

    @property
    def control(self):
        return self._control

    @control.setter
    def control(self, w):
        if not isinstance(w, Window):
            raise TypeError("Session.control can only point at objects of type Window.")

        self._control = w

    def quit(self, event):
        """Quit the game."""
        self.logger.info("Quitting.")
        self.on_exit()
        sys.exit()

    def stop_loop(self):
        """Pause the game by setting self._running to False."""
        self._running = False
        self.logger.debug("stop loop.")

    def resume_loop(self):
        """Unpause the game by setting self._running to True."""
        self._running = True
        self.logger.debug("Resumed loop.")
