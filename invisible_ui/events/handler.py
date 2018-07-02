"""Handler class."""

from inspect import getdoc


class Handler(object):
    """Event handler. The data class that stores the event and action."""

    def __init__(self, handlerSource, type, params, func,
                 always_active, docstring=None):
        """
        Create a new event handler.

        handlerSource - The handlerSource class to which this handler is attached.

        type - The type of this handler.

        params - A dictionary containing parameters the calling event must conform to in order to succeed. The values of this dictionary can either be simple values or lambdas.
        In the case of simple values, each value will be turned into a lambda of the form lambda against, actual = value: against == value.

        func - The function which should be called when this handler has been verified.

        always_active - If True, this handler will be called even when the game is paused.

        docstring - The docstring for func. If docstring is not specified, inspect.getdoc(func) will be used.

        To call the provided function properly, use Handler.call_func(*args, **kwargs).
        """
        self.handlerSource = handlerSource  # the parent element that created this handler
        self.type = type
        self.params = {}
        self.func = func
        self.always_active = always_active
        self.docstring = docstring
        self.event = None  # Gets populated when called.
        self.handlerSource.logger.debug("Added Handler {!s}".format(self))

        for k, v in params.items():
            if callable(v):
                self.params[k] = v
            else:
                self.params[k] = lambda value, actual = v: value == actual

    def get_help(self):
        """Return help for self.func."""
        if self.docstring:
            return self.docstring
        else:
            return getdoc(self.func)

    def call_func(self, event, *args, **kwargs):
        """Call self.func after setting self.event."""
        self.event = event
        return self.func(event, *args, **kwargs)

    def __str__(self):
        """Return the data for this handler for testing."""
        return "<Handler: handlerSource = {0!s}, type = {1}, params = {2!s}, func = {3}, always_active = {4}, docstring = {5}>".format(
            self.handlerSource,
            self.type,
            self.params,
            self.func,
            self.always_active,
            self.docstring
        )

    def __repr__(self):
        """Return the Data in literal form for this object."""
        return str(self)
