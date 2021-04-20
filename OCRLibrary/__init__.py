"""
OCRLibrary module
"""
from OCRLibrary.keywords import GenericImageProcessingKeywords
from OCRLibrary.version import VERSION

__version__ = VERSION

class OCRLibrary(GenericImageProcessingKeywords):
    """
    Explanation of the library goes here.
    """

    def __init__(self):
        for b in OCRLibrary.__bases__:
            b.__init__(self)
