from typing import Any, Callable, Dict, List, Tuple

# Central registry for hooks: mapping hook name to list of (priority, hook function)
_hook_registry: Dict[str, List[Tuple[int, Callable[..., Any]]]] = {}

def register_hook(name: str, hook_fn: Callable[..., Any], priority: int = 10):
    """
    Register a hook with a given priority.
    Lower numbers indicate higher priority.
    """
    _hook_registry.setdefault(name, []).append((priority, hook_fn))
    # Keep hooks sorted by priority.
    _hook_registry[name].sort(key=lambda x: x[0])

def get_hooks(name: str) -> List[Callable[..., Any]]:
    """Retrieve hooks for a given name, sorted by priority."""
    return [hook for _, hook in _hook_registry.get(name, [])]

def unregister_hook(name: str, hook_fn: Callable[..., Any]):
    """Unregister a specific hook."""
    if name in _hook_registry:
        _hook_registry[name] = [(p, fn) for p, fn in _hook_registry[name] if fn != hook_fn]