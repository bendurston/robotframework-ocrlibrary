"""
High level implementations of functions within image transformation/
"""
from imagetransformation.changing_colourspaces import .
from imagetransformation.image_blurring import .
from imagetransformation.image_thresholding import .
from imagetransformation.morphological_transformations import .


def process_to_binary_image(img, inverse=False, threshold=127, max_threshold=255):
    """
    Purpose:
         Process an image to binary colours.
    Args:
        img - a read image (result of imread())
        inverse - if true an inverted binary thresholding will be applied (optional). 
        threshold - threshold value used to classify the pixel values (optional).
        max_threshold - the max value to be given if a pixels value is more than the threshold value (optional).
    Returns:
        A binary image.
    """
    gray_img = convert_bgr_to_gray(img)
    if inverse:
        binary_image = thresholding_binary_inv(gray_img, threshold, max_threshold)
    else:
        binary_image = thresholding_binary(gray_img, threshold, max_threshold)
    return binary_image

def process_to_binary_otsu_image(img, inverse=False, max_threshold=255):
    """
    Purpose:
        Process an image to binary colours using binary otsu thresholding.
    Args:
        img - a read image (result of imread())
        inverse - if true an inverted binary thresholding will be applied (optional). 
        max_threshold - the max value to be given if a pixels value is more than the threshold value (optional).
    Returns:
        binary_image_tuple[0] - optimal threshold value found by otsu threshold.
        binary_image_tuple[1] - binary image.
    """
    gray_img = convert_bgr_to_gray(img)
    if inverse:
        binary_image_tuple = threshold_binary_inv_otsu(gray_img, max_threshold)
    else:
        binary_image_tuple = threshold_binary_otsu(gray_img, max_threshold)
    return binary_image_tuple

def process_to_tozero_image(img, inverse=False, threshold=177, max_threshold=255):
    """
    Purpose:
        Process an image tozero. All values considered black (if no inverse) will be set to black, the rest of 
        the image will remain in gray scale. If inverse is true, the values considered to be white will be set to black,
        the rest of the image will remain in gray scale.
    Args:
        img - a read image (result of imread())
        inverse - if true an inverted binary thresholding will be applied (optional). 
        threshold - threshold value used to classify the pixel values (optional).
        max_threshold - the max value to be given if a pixels value is more than the threshold value (optional).
    Returns:
        Tozero grayscale/binary image.
    """
    gray_img = convert_bgr_to_gray(img)
    if inverse:
        tozero_image = threshold_tozero_inv(gray_img, threshold, max_threshold)
    else:
        tozero_image = threshold_tozero(gray_img, threshold, max_threshold)
    return tozero_image

def process_to_tozero_otsu_image(img, inverse=False, max_threshold=255):
    """
    Purpose:
        Process an image tozero colours using tozero otsu thresholding.
    Args:
        img - a read image (result of imread())
        inverse - if true an inverted tozero thresholding will be applied (optional). 
        max_threshold - the max value to be given if a pixels value is more than the threshold value (optional).
    Returns:
        tozero_image_tuple[0] - optimal threshold value found by otsu threshold.
        tozero_image_tuple[1] - tozero binary/grayscale image.
    """
    gray_img = convert_bgr_to_gray(img)
    if inverse:
        tozero_image_tuple = threshold_tozero_inv_otsu(gray_img, max_threshold)
    else:
        tozero_image_tuple = threshold_tozero_otsu(gray_img, max_threshold)
    return tozero_image_tuple

def process_to_thrunc_image(img, threshold=177, max_threshold=255):
    """
    Purpose:
        Process an image to gray scale and apply thruncation threshold (values considered to be white will be set to white, the 
        rest of the image will remain gray scale).
    Args:
        img - a read image (result of imread())
        threshold - threshold value used to classify the pixel values (optional).
        max_threshold - the max value to be given if a pixels value is more than the threshold value (optional).
    Returns:
        Thruncated binary/grayscale image.
    """
    gray_img = convert_bgr_to_gray(img)
    thrunc_image = threshold_thrunc(gray_img, threshold, max_threshold)
    return thrunc_image


def process_to_thrunc_otsu_image(img, max_threshold=255):
     """
    Purpose:
        Process an image to gray scale and apply thruncation and otsu threshold (values considered to be white will be set to white, the 
        rest of the image will remain gray scale).
    Args:
        img - a read image (result of imread())
        max_threshold - the max value to be given if a pixels value is more than the threshold value (optional).
    Returns:
        thrunc_image_tuple[0] - optimal threshold value found by otsu threshold.
        thrunc_image_tuple[1] - thrunc binary/grayscale image.
    """
    gray_img = convert_bgr_to_gray(img)
    thrunc_image_tuple = threshold_thrunc_otsu(gray_img, max_threshold)
    return thrunc_image_tuple