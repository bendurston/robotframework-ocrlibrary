"""
OCRLibrary module
"""
from OCRLibrary.keywords.binary_image_transformation import ImageThresholdingKeywords, MorphologicalTransformationKeywords
from OCRLibrary.keywords.changing_colourspace_transformation import ChangingColourspaceKeywords
from OCRLibrary.keywords.content_location import ContentLocationKeywords
from OCRLibrary.keywords.content_validation import ContentValidationKeywords
from OCRLibrary.keywords.read_and_save_images import ReadImageKeywords, SaveImageKeywords
from OCRLibrary.keywords.smoothing_image_transformation import SmoothingImageKeywords

from OCRLibrary.version import VERSION

__version__ = VERSION

class OCRLibrary(ImageThresholdingKeywords,
                MorphologicalTransformationKeywords,
                ChangingColourspaceKeywords,
                ContentLocationKeywords,
                ContentValidationKeywords,
                ReadImageKeywords,
                SaveImageKeywords,
                SmoothingImageKeywords):
    """
    OCRLibrary is an image reading and processing library for Robot Framework.

    The OCR component of OCRLibrary utilizes pytesseract, which is a python wrapper for Google's Tesseract OCR.
    Image processing is done through the opencv-python package.

    Please note that recogizing all characters and their locations from screenshots is not guaranteed. Although processing the
    image will increase the chances for the desired characters to be read or located.

    = Information On Image Transformations =
    [https://docs.opencv.org/4.5.2/d7/d4d/tutorial_py_thresholding.html | OpenCV Thresholding Documentation]
    [https://docs.opencv.org/4.5.2/d9/d61/tutorial_py_morphological_ops.html | OpenCV Morphological Transformation Documentation]
    [https://docs.opencv.org/4.5.2/df/d9d/tutorial_py_colorspaces.html | OpenCV Changing Colourspaces Documentation]
    [https://docs.opencv.org/4.5.2/d4/d13/tutorial_py_filtering.html | OpenCV Smoothing Image Documentation]

    == Using And Not Using OSTU ==
    Information on keywords that use the ``apply_otsu`` argument.

    List of current keywords that can use OTSU:
    ``Get Binary Image``, ``Get To Zero Image`` and, ``Get Trunc Image``

    === Using OTSU ===
    Enabling otsu (``apply_otsu = True``) for thresholding keywords determines the threshold value automatically.
    When otsu is enabled, the image processing keyword will return a tuple. Index 0 contains the optimal threshold
    value found by the ostu threshold, and index 1 has the binary image.

    For an example, please see the example ``Using Get To Zero Image`` [https://github.com/bendurston/robotframework-ocrlibrary/blob/main/examples/keyword_usage.robot | in the keyword usage file.]

    === Not Using OTSU ===
    When ``apply_otsu = False`` threshold values must be provided. For more detail about the thresholding arguments,
    please see the OpenCV thresholding documentation listed above.

    For an example, please see the example ``Using Get Trunc Image`` [https://github.com/bendurston/robotframework-ocrlibrary/blob/main/examples/keyword_usage.robot | in the keyword usage file.]

    == Keywords With Apply Prefix ==
    This information pertains to the keywords with the ``Apply`` prefix.
    === Kernel Size Argument ===
    There are a few minor differences with this argument for some keywords.

    ``Apply Median Filtering To Image`` takes a kernel size as an integer that is odd and greater than 0.

    ``Apply Gaussian Blur To Image`` takes a kernel size as a tuple/list where the values must be positive odd integers.

    The rest of the keywords take a kernel size as a tuple/list where the values must be postive.

    === Kernel Type Argument ===
    Keywords that require a ``kernel_type`` take the given kernel size and create a structured element. The integer provided as
    the kernel type will determine the shape of the structured element. 0 will be a rectangle, 1 will be an ellipse, 
    and 2 will be a cross.

    === Iteration Argument ===
    Iteration is the number of times the transformation is performed on the image. The ``iteration`` can be any positive integer
    greater than 0.

    === Depth Argument ===
    Depth represents the desired depth of the destination image. When ``depth=-1`` the output image will have the same depth as the source.

    == Pytesseract Configuration Strings ==
    Please see [https://github.com/bendurston/robotframework-ocrlibrary#custom-configurations-for-reading-images |the OCRLibrary README.md] for an in depth explanation of the ``pyt_conf`` argument.

    Example:
    | ${img_path}=    Capture Page Screenshot
    | ${processed_img}=     Read Image  ${img_path}
    | ${content}=   Get Image Content   ${processed_img}    --psm 6 -c tessedit_char_whitelist=0123456789   eng
    Note: Only use one space between each configuration in the ``pyt_conf`` argument.

    == Masking Colours ==
    Users are able to mask (maintain) colours that exist within the provided upper and lower bounds. A BGR or HSV image can be
    used for either ``Mask Colour`` or ``Mask Colours``. Bounds can be either a list of a tuple, and each index must be of type int.
    Representation of BGR and HSV bounds respectively: (blue value, green value, red value), (hue value, saturation value, brightness value).

    For more detail about the masking colours, please see the OpenCV changing colourspaces documentation listed above.

    Please see the [https://github.com/bendurston/robotframework-ocrlibrary/blob/main/examples/keyword_usage.robot |keyword_usage.robot file] for an example of the Mask Colour or Mask Colours keywords.

    == Reading And Saving Images ==
    Please see the list of the following [https://docs.opencv.org/master/d4/da8/group__imgcodecs.html#ga288b8b3da0892bd651fce07b3bbd3a56 |formats that are supported] for image reading.

    Please see the [https://docs.opencv.org/master/d4/da8/group__imgcodecs.html#gabbc7ef1aa2edfaa87772f1202d67e0ce |list of exceptions] for saving an image.
    """
    ROBOT_LIBRARY_SCOPE = "GLOBAL"
    ROBOT_LIBRARY_VERSION = VERSION

    def __init__(self):
        for b in OCRLibrary.__bases__:
            b.__init__(self)
