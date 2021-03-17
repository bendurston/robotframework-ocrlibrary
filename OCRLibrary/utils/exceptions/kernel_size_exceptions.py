class Error(Exception):
    """
    Base Class for the kernel size exceptions module.
    """
    pass

class InvalidKernelSize(Error):
    """
    Purpose:
        Exception raised when the when the provided kernel size is invalid.
    Attributes:
        message - explanation of the error.
    """
    def __init__(self, message):
        self.message = message