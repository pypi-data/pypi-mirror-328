from pyextend.utils.reporting import log

def log_event(event_name: str, payload: dict | str = None):
    """
    Log an event detail
    :param event_name:
    :param payload:
    :return:
    """
    log.info(f"Event observed: {event_name} [| {payload} |]")

def debug_event(event_name: str, payload: dict | str = None):
    """
    Log an event detail
    :param event_name:
    :param payload:
    :return:
    """
    log.debug(f"Event debug: {event_name} [| {payload} |]")