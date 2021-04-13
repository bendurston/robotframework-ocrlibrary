"""
Changing colourspaces module.
"""
import cv2
import numpy as np

def convert_bgr_to_gray(img):
    """
    Purpose:
        Converts image from BGR to gray scale.
    Args:
        img - provided read image (result of cv2.imread()).
    Returns:
        Image in gray scale.
    """
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

def convert_bgr_to_hsv(img):
    """
    Purpose:
        Converts image from BGR to HSV.
    Args:
        img - provided read image (result of cv2.imread()).
    Returns:
        Image in HSV.
    """
    return cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

def mask_single_colour_bgr(img, lower_bound_colour, upper_bound_colour):
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

def mask_double_colour_bgr(img, lower_bound_colour1, upper_bound_colour1, lower_bound_colour2, upper_bound_colour2):
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
    result = cv2.bitwise_and(img, img, mask=mask)
    return result

def mask_single_colour_hsv(img_hsv, lower_bound_colour, upper_bound_colour):
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
    result = cv2.bitwise_and(img_hsv, img_hsv, mask=mask)
    return result

def mask_double_colour_hsv(img_hsv, lower_bound_colour1, upper_bound_colour1, lower_bound_colour2, upper_bound_colour2):
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
    result = cv2.bitwise_and(img_hsv, img_hsv, mask= mask)
    return result
    