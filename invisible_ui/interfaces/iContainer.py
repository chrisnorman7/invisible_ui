"""An interface that enforces that any object that wishes to include other elements, must include these methods."""

from abc import ABC, abstractmethod


class IContainer(ABC):

    def __init__(self):
        raise TypeError("Interface can not be instantiated.")

    @abstractmethod
    def add(self, e):
        """Adds an element to this object."""
        pass

    @abstractmethod
    def remove(self, e):
        """Removes an element from this object."""
        pass

    @abstractmethod
    def next(self, event):
        """Navigate to the next element."""
        pass

    @abstractmethod
    def previous(self, event):
        """Navigate to the previous element."""
        pass

    @abstractmethod
    def get_current_element(self):
        """Return the current element in the queue."""
        pass

    @abstractmethod
    def set_control(self, element):
        """Set control of this object to the given element. Used by external elements to change the currently focused element."""
        pass

    @abstractmethod
    def reset_control(self):
        """Reset control to the currently selected Element before set_control was called."""
        pass
