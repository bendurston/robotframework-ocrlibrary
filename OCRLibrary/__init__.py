"""
OCRLibrary module
"""
from OCRLibrary.keywords.generic_image_transformation import GenericImageTransformationKeywords
from OCRLibrary.keywords.generic_image_processing import GenericImageProcessingKeywords
from OCRLibrary.keywords.binary_image_transformation import BinaryImageTransformationKeywords
from OCRLibrary.keywords.binary_image_processing import BinaryImageProcessingKeywords
from OCRLibrary.keywords.colour_image_processing import ColourImageProcessingKeywords
from OCRLibrary.keywords.content_validation import ContentValidationKeywords
from OCRLibrary.keywords.content_location import ContentLocationKeywords

from OCRLibrary.version import VERSION

__version__ = VERSION

class OCRLibrary(GenericImageTransformationKeywords,
                GenericImageProcessingKeywords,
                BinaryImageTransformationKeywords,
                BinaryImageProcessingKeywords,
                ColourImageProcessingKeywords,
                ContentValidationKeywords,
                ContentLocationKeywords):
    """
    Explanation of the library goes here.
    """

    def __init__(self):
        for b in OCRLibrary.__bases__:
            b.__init__(self)
