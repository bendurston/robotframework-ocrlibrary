"""
Image thresholding module.
"""
import cv2

def threshold_binary(img, thresh, max_thresh):
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

def threshold_binary_inv(img, thresh, max_thresh):
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

def threshold_trunc(img, thresh, max_thresh):
    """
    Purpose:
        Apply truncated threshold to grayscale image.
    Arguments:
        img - a gray scale image.
        thresh - threshold value used to classify the pixel values.
        max_thresh - the max value to be given if a pixels value is more than the threshold value.
    Returns:
        Thresholded image.
    """
    return cv2.threshold(img, thresh, max_thresh, cv2.THRESH_TRUNC)[1]

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

def threshold_binary_otsu(img, max_thresh):
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

def threshold_binary_inv_otsu(img, max_thresh):
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

def threshold_trunc_otsu(img, max_thresh):
    """
    Purpose:
        Apply truncated threshold with otsu threshold to grayscale image.
    Arguments:
        img - a gray scale image.
        max_thresh - the max value to be given if a pixels value is more than the threshold value.
    Returns:
        tuple[0] - optimized threshold value.
        tuple[1] - thresholded image.
    """
    return cv2.threshold(img, 0, max_thresh, cv2.THRESH_TRUNC+cv2.THRESH_OTSU)

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
