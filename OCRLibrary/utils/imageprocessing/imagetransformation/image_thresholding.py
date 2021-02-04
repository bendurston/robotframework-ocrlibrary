import cv2

"""
Reference: 
    https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_thresholding/py_thresholding.html#thresholding

Notes:

    Threshold first argument, image, should be gray scale. Second argument is the threshold value which is used to classify the pixel values.
    The third argument is the max value which represents the value to be given if the pixel value is more than (sometimes less than) the threshold value.
    The fourth argument are the different styles of thresholding: cvs.THRESH_BINARY, cvs.THRESH_BINARY_INV, cvs.THRESH_THRUNC, cvs.THRESH_TOZERO, and cvs.THRESH_TOZERO_INV

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
