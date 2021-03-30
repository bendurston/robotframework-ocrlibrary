class Error(Exception):
    """
    Base Class for all custom exceptions
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

class ContentNotFound(Error):
    """
    Purpose:
        Exception raised when the desired content is not found within the image.
    Attributes:
        message - explanation of the error.
    """
    def __init__(self, message):
        self.message = message

class InvalidImageArgument(Error):
    """
    Purpose:
        Exception raised when an image has been given to the function that has not been processed by opencv.
    Attributes:
        message - explanation of the error.
    """
    def __init__(self, message):
        self.message = message