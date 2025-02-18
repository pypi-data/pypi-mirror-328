import asyncio
from pyextend.utils.reporting import log

from pyextend.hooks.register import get_hooks

# Middleware for hooks: functions that can wrap/modify hook execution
_hook_middleware = []

def add_hook_middleware(fn):
    """Register a middleware function for hooks."""
    _hook_middleware.append(fn)

def execute_hooks(name: str, *args, mode: str = 'sync', **kwargs):
    """
    Execute all hooks registered under the given name.
    
    mode:
      - 'sync': Execute synchronously.
      - 'async': Schedule on the event loop.
      - 'deferred': Stub for deferred execution.
    """
    hooks = get_hooks(name)
    
    # Apply middleware to the hook parameters
    for mw in _hook_middleware:
        args, kwargs = mw(name, args, kwargs)
    
    if mode == 'sync':
        results = []
        for hook in hooks:
            try:
                results.append(hook(*args, **kwargs))
            except Exception as e:
                log.exception(f"Error executing hook {hook} in sync mode: {e}")
        return results
    elif mode == 'async':
        loop = asyncio.get_event_loop()
        tasks = []
        for hook in hooks:
            tasks.append(loop.create_task(async_hook_wrapper(hook, *args, **kwargs)))
        return tasks # Caller can await these tasks.
    elif mode == 'deferred':
        log.debug(f"Deferred hook execution for {name} with args {args} and kwargs {kwargs}")
    else:
        raise ValueError("Invalid execution mode. Choose 'sync', 'async', or 'deferred'.")

async def async_hook_wrapper(hook, *args, **kwargs):
    try:
        result = hook(*args, **kwargs)
        if asyncio.iscoroutine(result):
            return await result
        return result
    except Exception as e:
        log.exception(f"Error in async hook {hook}: {e}")
