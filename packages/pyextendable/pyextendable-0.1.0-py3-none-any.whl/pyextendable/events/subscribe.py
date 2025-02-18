from pyextend.events.dispatch import register_listener, unregister_listener

def subscribe(event_name: str, listener):
    """Alias for register_listener to subscribe to an event."""
    register_listener(event_name, listener)

def unsubscribe(event_name: str, listener):
    """Alias for unregister_listener to unsubscribe from an event."""
    unregister_listener(event_name, listener)