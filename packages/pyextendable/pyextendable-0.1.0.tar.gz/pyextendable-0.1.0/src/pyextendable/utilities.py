# Description: Logging utilities

def import_logger():
    log = None
    try:
        from pyutil.reporting import logged
        log = logged.logger
    except ImportError as e:
        import logging as logged
        log = logged.getLogger(__name__)
    finally:
        log.info("Logging is working")
        return log

log = import_logger()