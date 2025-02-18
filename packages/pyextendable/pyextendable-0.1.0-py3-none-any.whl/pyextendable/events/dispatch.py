from pyextend.utils.reporting import log

import asyncio
from typing import Any, Callable, Dict, List, Optional

middleware: List[Callable[[str, Dict[str, Any]], Dict[str, Any]]] = []

def add_middleware(fn: Callable[[str, Dict[str, Any]], Dict[str, Any]] = None):
    """
    Register a middleware function for events
    :param fn:
    :return: nothing
    """
    try:
        middleware.append(fn)
        log.debug(f"Middleware Added: {fn}")
    except Exception as e:
        log.error(f"Failed to add Middleware: {str(fn)}")
        raise e

def dispatch(event_name: str,
             payload: Optional[Dict[str, Any]] = None,
             mode: str = 'sync'):
    """
    Dispatch an event with the given payload.

    *Modes*:
        - 'sync': Execute listeners
        - 'async': Schedule listeners on the event loop
        - 'deferred': Execute listener later (e.g. via a task queue)

    :param event_name:
    :param payload:
    :param mode:
    :return:
    """
    payload = payload or {}

    # Apply middleware

    for fn in middleware:
        payload = fn(event_name, payload)

    # Dispatch to subscribed listeners

    listeners = get_listeners(event_name)

    if mode == 'sync':
        for listener in listeners:
            try:
                listener(event_name, payload)
            except Exception as e:
                log.exception(f"Error in listener {listener} for event {event_name}: {e}")

    elif mode == 'async':
        loop = asyncio.get_event_loop()
        for listener in listeners:
            loop.create_task(async_listener_wrapper(listener, event_name, payload))
    elif mode == 'deferred':
        # Stub for deferred execution: integrate with a task queue if needed.
        log.debug(f"Deferred dispatch for event {event_name} with payload {payload}")
    else:
        raise ValueError("Invalid dispatch mode. Choose 'sync', 'async', or 'deferred'.")

async def async_listener_wrapper(listener: Callable[[str, Dict[str, Any]], Any], event_name: str, payload: Dict[str, Any]):
    try:
        result = listener(event_name, payload)
        if asyncio.iscoroutine(result):
            await result
    except Exception as e:
        log.exception(f"Error in async listener {listener} for event {event_name}: {e}")
# A simple in-memory event listener registry.
_listener_registry: Dict[str, List[Callable[[str, Dict[str, Any]], Any]]] = {}

def register_listener(event_name: str, listener: Callable[[str, Dict[str, Any]], Any]):
    """Subscribe a listener to an event."""
    _listener_registry.setdefault(event_name, []).append(listener)

def unregister_listener(event_name: str, listener: Callable[[str, Dict[str, Any]], Any]):
    """Unsubscribe a listener from an event."""
    if event_name in _listener_registry:
        _listener_registry[event_name].remove(listener)

def get_listeners(event_name: str) -> List[Callable[[str, Dict[str, Any]], Any]]:
    """Retrieve all listeners for the event, including those registered for wildcard scopes."""
    # For simplicity, this returns only exact matches.
    return _listener_registry.get(event_name, [])
