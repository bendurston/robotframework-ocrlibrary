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
    OCRLibrary is an image reading and processing library for Robot Framework.

    The OCR component of OCRLibrary utilizes pytesseract, which is a python wrapper for Google's Tesseract OCR.
    Image processing is done through the opencv-python package.

    Please note that recogizing all characters and their locations from screenshots is not guaranteed. Although processing the
    image will increase the chances for the desired characters to be read or located.

    == Arguments for image processing keywords ==

    === Using OTSU For Binary Image Processing ===
    Enabling otsu ``apply_otsu = True`` for thresholding keywords determines the threshold value automatically.
    When apply_otsu is true, the image processing keyword will return a tuple. Index 0 contains the optimal threshold
    value found by the ostu threshold, and index 1 has the binary image.

    List of current keywords that can use otsu: Get Binary Image, Get To Zero Image and, Get Trunc Image

    === Image Transformation Arguments ===
    Most of the image transformation keywords require a kernel size. All but ``Apply Median Filtering To Image`` take
    kernel size as a tuple/list. The keywords that take kernel size as a tuple/list must be positve (even & odd) ints.
    ```Apply Gaussian Blur To Image``` is the one keyword where the values in the tuple/list must be positive odd ints.
    The keywords take the kernel size and create a structured element in the shape of either a
    rectangle, ellipse or a cross. These shapes are chosen by the value passed to ``kernel_type``. 0 will be arectangle,
    1 will be an ellipse, and 2 will be a cross.

    For the keywords that require an ``iteration`` value - iteration is the number of times the transformation is performed
    on the image.

    For the keywords that require a ``depth`` value - depth represents the desired depth of the destination image.
    When ``depth=-1`` the output image will have the same depth as the source.

    === Pytesseract Config and Language Arguments ===
    Please see [https://github.com/bendurston/robotframework-ocrlibrary#custom-configurations-for-reading-images |the OCRLibrary README.md] for an in depth explanation of the ``pyt_conf`` argument.

    List of [https://tesseract-ocr.github.io/tessdoc/Data-Files#data-files-for-version-400-november-29-2016 |supported languages] as of Tesseract OCR version 4.0.0, along with language codes used
    for the ``lang`` argument.

    == Masking Colours ==
    Users are able to mask (maintain) colours that exist within the provided upper and lower bounds. A BGR or HSV image can be
    used for either ``Mask Colour`` or ``Mask Colours``. Bounds can be either a list of a tuple, and each index must be of type int.
    Representation of BGR and HSV bounds respectively: (blue value, green value, red value), (hue value, saturation value, brightness value).

    == Reading and Saving Images ==
    Please see the list of the following [https://docs.opencv.org/master/d4/da8/group__imgcodecs.html#ga288b8b3da0892bd651fce07b3bbd3a56 |formats that are supported] for image reading.

    Please see the [https://docs.opencv.org/master/d4/da8/group__imgcodecs.html#gabbc7ef1aa2edfaa87772f1202d67e0ce |list of exceptions] for saving an image.
    """
    ROBOT_LIBRARY_SCOPE = "GLOBAL"
    ROBOT_LIBRARY_VERSION = VERSION

    def __init__(self):
        for b in OCRLibrary.__bases__:
            b.__init__(self)
