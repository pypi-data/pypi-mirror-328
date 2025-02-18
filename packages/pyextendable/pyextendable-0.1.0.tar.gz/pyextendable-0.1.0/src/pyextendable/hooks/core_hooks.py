from abc import ABC, abstractmethod
from typing import Any

from pyextend.utils.reporting import log

class BaseHook(ABC):
    """
    Abstract base class for hooks.
    Hooks can be defined inline or via configuration.
    """

    @abstractmethod
    def execute(self, **kwargs) -> Any:
        """Execute the hook logic."""
        pass


# Example core hook
class PreActionHook(BaseHook):
    def execute(self, **kwargs):
        log.info("Executing pre-action hook with:", kwargs)
        return kwargs