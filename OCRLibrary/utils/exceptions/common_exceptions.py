class Error(Exception):
    """
    Base Class for exceptions in common exceptions module.
    """
    pass

class InvalidImageArgument(Error):
    """
    Purpose:
        Exception raised when an image has been given to the function that has not been processed by opencv.
    Attributes:
        message - explanation of the error.
    """
    def __init__(self, message):
        self.message = message