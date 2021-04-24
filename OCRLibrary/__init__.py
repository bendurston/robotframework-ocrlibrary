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

    == About arguments for image processing ==
    OTSU and thresholding
    If apply_otsu is true, a tuple will be returned. Index 0 contains the optimal threshold value found by
            the ostu threshold, and index 1 has the binary image.

    === Talk about how some keywords need different kernel sizes, some tuple some ints ===

    ==== pyt_conf and lang ====

    === binary transformation arguments ===
    img - processed binary image.
            kernel_size - size of the kernel
            kernel_type - shape of kernel used. 0 = rectangle, 1 = ellipse, and 2 = cross.
            iteration - number of iterations to perform on image.

    === generic image transforatmion arguments ====
    img - processed image.
            kernel_size - size of the kernel
            kernel_type - shape of kernel used. 0 = rectangle, 1 = ellipse, and 2 = cross.
            depth - desired depth of the destination image.
                when depth=-1, the output image will have the same depth as the source.

    ===== Notes on colour bounds =====
    Note if the image is BGR the bounds
            must be ints 0 to 255. If the image is HSV the bounds must be a 3 element tuple containing ints 0 to 255.
            Note - Bounds can be of type tuple or list e.g - (blue, green, red), (hue, saturation, value) or [blue, green, red], [hue, saturation, value].
        Args:
            processed_img - the processed image.
            lower_bound_colour - the lower bound of the colour to exclude from the mask.
            upper_bound_colour - the upper bound of the colour to exclude from the mask.
            colour_type - 0 if the processed image is in BGR, 1 if the processed image is in HSV.

    ==== about valid images to read and valid image formats to save processed images. ====
    """

    def __init__(self):
        for b in OCRLibrary.__bases__:
            b.__init__(self)
