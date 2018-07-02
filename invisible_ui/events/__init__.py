"""
This package is used to handle events for the pygame events in invisible_ui.

The Handler is a data helper class used to store the event, the action, and other parameters for the event.

The EventManager is an abstract base class used to manage events using Handlers.
EventManager provides methods for adding and removing events as well as an abstract method handle_event for all subclasses to implement 
"""

from invisible_ui.events.eventManager import EventManager
