from pyutil.errors import PyForgeException, ExceptionHandler

class PyExtendException(PyForgeException):
    def __init__(self, message: str = 'An unknown error occurred in the system.'):
        self.message = message

    def __str__(self):
        return f"{self.message}"


class HooksException(PyExtendException):
    def __init__(self, message: str = 'An unknown error occurred in the PyExtend system.'):
        super().__init__(message=message)
