"""Handler class."""


class Handler(object):
    """Event handler. The data class that stores the event and action."""

    def __init__(self, handlerSource, type, params, actions):
        """
        Create a new event handler.

        handlerSource - The handlerSource class to which this handler is attached.

        type - The type of this handler.

        params - A dictionary containing parameters the calling event must conform to in order to succeed. The values of this dictionary can either be simple values or lambdas.
        In the case of simple values, each value will be turned into a lambda of the form lambda against, actual = value: against == value.

        actions - The functions which should be called when this handler has been verified.

        When the provided actions are called, the current event that triggered the action is passed in as the first argument 
        """
        self._handlerSource = handlerSource  # the parent element that created this handler
        self._type = type
        self._params = {}
        self._actions = [actions] if not isinstance(actions, list) else actions
        self._event = None  # Gets populated when called.

        if self._handlerSource.logger is not None:
            self._handlerSource.logger.debug("Added Handler {!s}".format(self))

        for k, v in params.items():
            if callable(v):
                self._params[k] = v
            else:
                self._params[k] = lambda value, actual = v: value == actual

    @property
    def type(self):
        return self._type

    @property
    def params(self):
        return self._params

    @property
    def actions(self):
        return self._actions

    @property
    def event(self):
        return self._event

    def call_actions(self, event, *args, **kwargs):
        """Call each function in self._actions after setting self._event."""
        self._event = event

        for func in self._actions:
            func(event, *args, **kwargs)

    def __str__(self):
        """Return the data for this handler for testing."""
        return "<Handler: handlerSource = {0!s}, type = {1}, params = {2!s}, func = {3}".format(
            self._handlerSource,
            self._type,
            self._params,
            self._actions
        )

    def __repr__(self):
        """Return the Data in literal form for this object."""
        return str(self)
