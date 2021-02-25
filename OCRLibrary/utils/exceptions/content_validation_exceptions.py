class Error(Exception):
    """
    Base Class for exceptions in content validation exceoptions module.
    """
    pass

class ContentNotFound(Error):
    """
    Purpose:
        Exception raised when the desired content is not found within the image.
    Attributes:
        message - explanation of the error.
    """
    def __init__(self, message):
        self.message = message