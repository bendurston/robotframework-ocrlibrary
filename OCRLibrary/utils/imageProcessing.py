"""
Image Processing Reference: https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_table_of_contents_imgproc/py_table_of_contents_imgproc.html#

Note: To convert an image to binary (black and white) change image to grayscale, then add binary threshold or inverse binary threshold.
"""
import cv2
import numpy as np

# def image_process(path):
#     img = cv2.imread(path)
#     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#     blur = cv2.GaussianBlur(gray, (1,1), 0)
#     thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

#     kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1,1))
#     opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=1)
#     invert = 255 - opening
#     return invert
    
# Changing Colourspaces
# Reference: https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_colorspaces/py_colorspaces.html#converting-colorspaces
def convert_BGR_to_GRAY(img):
    """
    Purpose:
        Converts image from BGR to gray scale.
    Args:
        img - provided read image (result of cv2.imread()).
    Returns:
        Image in gray scale.
    """
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

def convert_BGR_to_HSV(img):
    """
    Purpose:
        Converts image from BGR to HSV.
    Args:
        img - provided read image (result of cv2.imread()).
    Returns:
        Image in HSV.
    """
    return cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

def mask_single_colour_BGR(img, lower_bound_colour, upper_bound_colour):
    """
    Purpose:
        Maskes any colour that is not in the range of the bounds of the provided colour.
    Args:
        img - provided read BGR image (result of cv2.imread()). 
        lower_bound_colour - the lower bound of the colour to not mask in BGR format.
        upper_bound_colour - the upper bound of the colour to not mask in BGR format.
    Returns:
        result - image with colours masked.
    """
    lower_bound_colour = np.array(lower_bound_colour)
    upper_bound_colour = np.array(upper_bound_colour)
    mask = cv2.inRange(img, lower_bound_colour, upper_bound_colour)
    result = cv2.bitwise_and(img, img, mask= mask)
    return result

def mask_double_colour_BGR(img, lower_bound_colour1, upper_bound_colour1, lower_bound_colour2, upper_bound_colour2):
    """
    Purpose:
        Maskes any colour that is not in the range of the bounds of the two provided colours.
    Args:
        img - provided read BGR image (result of cv2.imread()).
        lower_bound_colour1 - the lower bound of the first colour to not mask in BGR format.
        upper_bound_colour1 - the upper bound of the first colour to not mask in BGR format.        
        lower_bound_colour2 - the lower bound of the second colour to not mask in BGR format.
        upper_bound_colour2 - the upper bound of the second colour to not mask in BGR format.
    Returns:
        result - image with colours masked.
    """
    lower_bound_colour1 = np.array(lower_bound_colour1)
    upper_bound_colour1 = np.array(upper_bound_colour1)
    lower_bound_colour2 = np.array(lower_bound_colour2)
    upper_bound_colour2 = np.array(upper_bound_colour2)
    mask1 = cv2.inRange(img, lower_bound_colour1, upper_bound_colour1)
    mask2 = cv2.inRange(img, lower_bound_colour2, upper_bound_colour2)
    mask = cv2.bitwise_or(mask1, mask2)
    result = cv2.bitwise_and(img, img, mask= mask)
    return result

def mask_single_colour_HSV(img_hsv, lower_bound_colour, upper_bound_colour):
    """
    Purpose:
        Maskes any colour that is not in the range of the bounds of the provided colour.
    Args:
        img_hsv - provided read HSV image (result of cv2.imread()). 
        lower_bound_colour - the lower bound of the colour to not mask in HSV format.
        upper_bound_colour - the upper bound of the colour to not mask in HSV format.
    Returns:
        result - image with colours masked.
    """
    lower_bound_colour = np.array(lower_bound_colour)
    upper_bound_colour = np.array(upper_bound_colour)
    mask = cv2.inRange(img_hsv, lower_bound_colour, upper_bound_colour)
    result = cv2.bitwise_and(img, img, mask= mask)
    return result

def mask_double_colour_HSV(img_hsv, lower_bound_colour1, upper_bound_colour1, lower_bound_colour2, upper_bound_colour2):
    """
    Purpose:
        Maskes any colour that is not in the range of the bounds of the two provided colours.
    Args:
        img_hsv - provided read HSV image (result of cv2.imread()).
        lower_bound_colour1 - the lower bound of the first colour to not mask in HSV format.
        upper_bound_colour1 - the upper bound of the first colour to not mask in HSV format.        
        lower_bound_colour2 - the lower bound of the second colour to not mask in HSV format.
        upper_bound_colour2 - the upper bound of the second colour to not mask in HSV format.
    Returns:
        result - image with colours masked.
    """
    lower_bound_colour1 = np.array(lower_bound_colour1)
    upper_bound_colour1 = np.array(upper_bound_colour1)
    lower_bound_colour2 = np.array(lower_bound_colour2)
    upper_bound_colour2 = np.array(upper_bound_colour2)
    mask1 = cv2.inRange(img_hsv, lower_bound_colour1, upper_bound_colour1)
    mask2 = cv2.inRange(img_hsv, lower_bound_colour2, upper_bound_colour2)
    mask = cv2.bitwise_or(mask1, mask2)
    result = cv2.bitwise_and(img, img, mask= mask)
    return result

# Image Thresholding
# Reference: https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_thresholding/py_thresholding.html#thresholding
# Note: Threshold first argument, image, should be gray scale. Second argument is the threshold value which is used to classify the pixel values.
# The third argument is the max value which represents the value to be given if the pixel value is more than (sometimes less than) the threshold value.
# The fourth argument are the different styles of thresholding: cvs.THRESH_BINARY, cvs.THRESH_BINARY_INV, cvs.THRESH_THRUNC, cvs.THRESH_TOZERO, and cvs.THRESH_TOZERO_INV

# Adaptive thresholding is good when the image has different lighting conditions in different areas.

"""
Notes:
    Reference: https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_thresholding/py_thresholding.html#thresholding
    See reference for example of the different thresholds.

    OTSU thresholding images should be in grayscale!

    All thresholding functions return a tuple, tuple[0] is the retVal, and tuple[1] is the thresholded image. 
    The thresholding functions without otsu thresholding will return the thresh argument as retVal. Therefore the tuple is indexed to 
    just return the thresholded image.

"""

def thresholding_binary(img, thresh, max_thresh):
    """
    Purpose:
        Apply binary threshold to grayscale image.
    Arguments:
        img - a gray scale image.
        thresh - threshold value used to classify the pixel values.
        max_thresh - the max value to be given if a pixels value is more than the threshold value.
    Returns:
        Thresholded image.
    """
    return cv2.threshold(img, thresh, max_thresh, cv2.THRESH_BINARY)[1]

def thresholding_binary_inv(img, thresh, max_thresh):
    """
    Purpose:
        Apply inverted binary threshold to grayscale image.
    Arguments:
        img - a gray scale image.
        thresh - threshold value used to classify the pixel values.
        max_thresh - the max value to be given if a pixels value is more than the threshold value.
    Returns:
        Thresholded image.
    """
    return cv2.threshold(img, thresh, max_thresh, cv2.THRESH_BINARY_INV)[1]

def thresholding_thrunc(img, thresh, max_thresh):
    """
    Purpose:
        Apply thruncated threshold to grayscale image.
    Arguments:
        img - a gray scale image.
        thresh - threshold value used to classify the pixel values.
        max_thresh - the max value to be given if a pixels value is more than the threshold value.
    Returns:
        Thresholded image.
    """
    return cv2.threshold(img, thresh, max_thresh, cv2.THRESH_THRUNC)[1]

def threshold_tozero(img, thresh, max_thresh):
    """
    Purpose:
        Appy to zero threshold to grayscale image.
    Arguments:
        img - a gray scale image.
        thresh - threshold value used to classify the pixel values.
        max_thresh - the max value to be given if a pixels value is more than the threshold value.
    Returns:
        Thresholded image.
    """
    return cv2.threshold(img, thresh, max_thresh, cv2.THRESH_TOZERO)[1]

def threshold_tozero_inv(img, thresh, max_thresh):
    """
    Purpose:
        Apply inverted to zero threshold to grayscale image.
    Arguments:
        img - a gray scale image.
        thresh - threshold value used to classify the pixel values.
        max_thresh - the max value to be given if a pixels value is more than the threshold value.
    Returns:
        Thresholded image.
    """
    return cv2.threshold(img, thresh, max_thresh, cv2.THRESH_TOZERO_INV)[1]

def thresholding_binary_otsu(img, max_thresh):
    """
    Purpose:
        Apply binary threshold with otsu threshold to grayscale image.
    Arguments:
        img - a gray scale image.
        max_thresh - the max value to be given if a pixels value is more than the threshold value.
    Returns:
        tuple[0] - optimized threshold value.
        tuple[1] - thresholded image.
    """
    return cv2.threshold(img, 0, max_thresh, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

def thresholding_binary_inv_otsu(img, max_thresh):
    """
    Purpose:
        Apply inverted binary threshold with otsu threshold to grayscale image.
    Arguments:
        img - a gray scale image.
        max_thresh - the max value to be given if a pixels value is more than the threshold value.
    Returns:
        tuple[0] - optimized threshold value.
        tuple[1] - thresholded image.
    """
    return cv2.threshold(img, 0, max_thresh, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

def thresholding_thrunc_otsu(img, max_thresh):
    """
    Purpose:
        Apply thruncated threshold with otsu threshold to grayscale image.
    Arguments:
        img - a gray scale image.
        max_thresh - the max value to be given if a pixels value is more than the threshold value.
    Returns:
        tuple[0] - optimized threshold value.
        tuple[1] - thresholded image.
    """
    return cv2.threshold(img, 0, max_thresh, cv2.THRESH_THRUNC+cv2.THRESH_OTSU)

def threshold_tozero_otsu(img, max_thresh):
    """
    Purpose:
        Apply to zero threshold with otsu threshold to grayscale image.
    Arguments:
        img - a gray scale image.
        max_thresh - the max value to be given if a pixels value is more than the threshold value.
    Returns:
        tuple[0] - optimized threshold value.
        tuple[1] - thresholded image.
    """
    return cv2.threshold(img, 0, max_thresh, cv2.THRESH_TOZERO+cv2.THRESH_OTSU)

def threshold_tozero_inv_otsu(img, max_thresh):
    """
    Purpose:
        Apply inverted to zero threshold with otsu threshold to grayscale image.
    Arguments:
        img - a gray scale image.
        max_thresh - the max value to be given if a pixels value is more than the threshold value.
    Returns:
        tuple[0] - optimized threshold value.
        tuple[1] - thresholded image.
    """
    return cv2.threshold(img, 0, max_thresh, cv2.THRESH_TOZERO_INV + cv2.THRESH_OTSU)

"""
Image blurring/Image Smoothing
"""
def blurring_averaging(img, kernel):
    """
    """
    return cv2.blur(img, kernel)

def blurring_gaussian(img, kernel, other):
    """
    """
    return cv2.GaussianBlur(img, kernel, other)

"""
Structuring Element
"""
def get_rect_kernel(kernel_size):
    """
    Purpose:
        Gets a rectangular shaped kernel
    Args:
        kernel_size - tuple: size of the kernel.
    Returns:
        2D array representing a rectangular kernel.
    """
    return cv2.getStructuringElement(cv2.MORPH_RECT, kernel_size)

def get_ellipse_kernel(kernel_size):
    """
    Purpose:
        Gets a ellipse shaped kernel
    Args:
        kernel_size - tuple: size of the kernel.
    Returns:
        2D array representing an ellipse kernel.
    """
    return cv2.getStructuringElement(cv2.MORPH_ELLIPSE, kernel_size)

def get_cross_kernel(kernel_size):
    """
    Purpose:
        Gets a rectangular shaped kernel
    Args:
        kernel_size - tuple: size of the kernel.
    Returns:
        2D array representing a rectangular kernel.
    """
    return cv2.getStructuringElement(cv2.MORPH_CROSS, kernel_size)

"""
Morphological transformations: results are best with binary images, specifically white foreground and black background. convert_BGR_to_GRAY() -> threshold_binary_inv()

In noise removal erosion is followed by dilation. Erosion removes white noises but shrinks the object. So dilation is performed.
"""
def morph_erosion(img, kernel, iteration=1):
    """
    Erodes the boundarios of foreground objects.
    """
    return cv2.erode(img, kernel, iterations= iteration)

def morph_dilation(img, kernel, iteration=1):
    """
    Opposite of erosion. A pixel becomes a '1' if at least one pixel under the kernel is '1'.
    """
    return cv2.dialte(img, kernel, iterations= iteration)

def morph_opening(img, kernel):
    """
    Useful in removing noise. Like erosion then dilation.
    """
    return cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)

def morph_closing(img, kernel):
    """
    Opposite to opening.
    """
    return cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)

def morp_gradient(img, kernel):
    """
    Will give the object an outline. 
    """
    return cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)

def morph_top_hat(img, kernel):
    """
    """
    return cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)

def morph_black_hat(img, kernel):
    """
    """
    return cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)
