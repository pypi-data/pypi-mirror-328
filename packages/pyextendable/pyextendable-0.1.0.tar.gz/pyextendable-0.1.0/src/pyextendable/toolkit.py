from pyextend.hooks import core_hooks

class Extender:  # TODO: Make a singleton/global object
    """

    """

    def __init__(self):
        """

        """
        self._events = None
        self._expansions = None
        self._hooks = None

    @property
    def events(self):
        """"""
        return self._events

    @property
    def expansions(self):
        """"""
        return self._expansions

    @property
    def hooks(self):
        """"""
        return self._hooks