"""
Image Processing Reference: https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_table_of_contents_imgproc/py_table_of_contents_imgproc.html#
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
    Converts image from BGR to gray scale.
    """
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

def convert_BGR_to_HSV(img, colour1, colour2):
    """
    Extracts the given colours from the image.
    """
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    hsv_colour1 = np.asarray(colour1)
    hsv_colour2 = np.asarray(colour2)
    mask = cv2.inRange(img_hsv, hsv_colour1, hsv_colour2)
    return mask
    

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
#TODO Image blurring/Image Smoothing
"""


"""
Structuring Element
"""
def get_rect_kernal(kernal_size):
    """
    Purpose:
        Gets a rectangular shaped kernal
    Args:
        kernal_size - tuple: size of the kernal.
    Returns:
        2D array representing a rectangular kernal.
    """
    return cv2.getStructuringElement(cv2.MORPH_RECT, kernal_size)

def get_ellipse_kernal(kernal_size):
    """
    Purpose:
        Gets a ellipse shaped kernal
    Args:
        kernal_size - tuple: size of the kernal.
    Returns:
        2D array representing an ellipse kernal.
    """
    return cv2.getStructuringElement(cv2.MORPH_ELLIPSE, kernal_size)

def get_cross_kernal(kernal_size):
    """
    Purpose:
        Gets a rectangular shaped kernal
    Args:
        kernal_size - tuple: size of the kernal.
    Returns:
        2D array representing a rectangular kernal.
    """
    return cv2.getStructuringElement(cv2.MORPH_CROSS, kernal_size)

"""
Morphological transformations: results are best with binary images, specifically white foreground and black background.
"""
