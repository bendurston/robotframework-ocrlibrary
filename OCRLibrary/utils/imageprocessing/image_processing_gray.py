"""
High level implementations of functions within image transformation/
"""
import cv2
from imagetransformation.changing_colourspaces import .
from imagetransformation.image_thresholding import .
from imagetransformation.morphological_transformations import .
from imagetransformation.structuring_element import .

def process_to_gray_scale(img_path):
    """
    #TODO
    """
    img = cv2.imread(img_path)
    gray_img = convert_bgr_to_gray(img)
    return gray_img

def process_to_binary_image(img_path, inverse=False, threshold=127, max_threshold=255):
    """
    Purpose:
         Process an image to binary colours.
    Args:
        img_path - path to the image to process
        inverse - if true an inverted binary thresholding will be applied (optional). 
        threshold - threshold value used to classify the pixel values (optional).
        max_threshold - the max value to be given if a pixels value is more than the threshold value (optional).
    Returns:
        A binary image.
    """
    img = cv2.imread(img_path)
    gray_img = convert_bgr_to_gray(img)
    if inverse:
        binary_image = thresholding_binary_inv(gray_img, threshold, max_threshold)
    else:
        binary_image = thresholding_binary(gray_img, threshold, max_threshold)
    return binary_image

def process_to_binary_otsu_image(img_path, inverse=False, max_threshold=255):
    """
    Purpose:
        Process an image to binary colours using binary otsu thresholding.
    Args:
        img_path - path to the image to process
        inverse - if true an inverted binary thresholding will be applied (optional). 
        max_threshold - the max value to be given if a pixels value is more than the threshold value (optional).
    Returns:
        binary_image_tuple[0] - optimal threshold value found by otsu threshold.
        binary_image_tuple[1] - binary image.
    """
    img = cv2.imread(img_path)
    gray_img = convert_bgr_to_gray(img)
    if inverse:
        binary_image_tuple = threshold_binary_inv_otsu(gray_img, max_threshold)
    else:
        binary_image_tuple = threshold_binary_otsu(gray_img, max_threshold)
    return binary_image_tuple

def process_to_tozero_image(img_path, inverse=False, threshold=177, max_threshold=255):
    """
    Purpose:
        Process an image tozero. All values considered black (if no inverse) will be set to black, the rest of 
        the image will remain in gray scale. If inverse is true, the values considered to be white will be set to black,
        the rest of the image will remain in gray scale.
    Args:
        img_path - path to the image to process
        inverse - if true an inverted binary thresholding will be applied (optional). 
        threshold - threshold value used to classify the pixel values (optional).
        max_threshold - the max value to be given if a pixels value is more than the threshold value (optional).
    Returns:
        Tozero grayscale/binary image.
    """
    img = cv2.imread(img_path)
    gray_img = convert_bgr_to_gray(img)
    if inverse:
        tozero_image = threshold_tozero_inv(gray_img, threshold, max_threshold)
    else:
        tozero_image = threshold_tozero(gray_img, threshold, max_threshold)
    return tozero_image

def process_to_tozero_otsu_image(img_path, inverse=False, max_threshold=255):
    """
    Purpose:
        Process an image tozero colours using tozero otsu thresholding.
    Args:
        img_path - path to the image to process 
        inverse - if true an inverted tozero thresholding will be applied (optional). 
        max_threshold - the max value to be given if a pixels value is more than the threshold value (optional).
    Returns:
        tozero_image_tuple[0] - optimal threshold value found by otsu threshold.
        tozero_image_tuple[1] - tozero binary/grayscale image.
    """
    img = cv2.imread(img_path)
    gray_img = convert_bgr_to_gray(img)
    if inverse:
        tozero_image_tuple = threshold_tozero_inv_otsu(gray_img, max_threshold)
    else:
        tozero_image_tuple = threshold_tozero_otsu(gray_img, max_threshold)
    return tozero_image_tuple

def process_to_thrunc_image(img_path, threshold=177, max_threshold=255):
    """
    Purpose:
        Process an image to gray scale and apply thruncation threshold (values considered to be white will be set to white, the 
        rest of the image will remain gray scale).
    Args:
        img_path - path to the image to process
        threshold - threshold value used to classify the pixel values (optional).
        max_threshold - the max value to be given if a pixels value is more than the threshold value (optional).
    Returns:
        Thruncated binary/grayscale image.
    """
    img = cv2.imread(img_path)
    gray_img = convert_bgr_to_gray(img)
    thrunc_image = threshold_thrunc(gray_img, threshold, max_threshold)
    return thrunc_image


def process_to_thrunc_otsu_image(img_path, max_threshold=255):
     """
    Purpose:
        Process an image to gray scale and apply thruncation and otsu threshold (values considered to be white will be set to white, the 
        rest of the image will remain gray scale).
    Args:
        img_path - path to the image to process
        max_threshold - the max value to be given if a pixels value is more than the threshold value (optional).
    Returns:
        thrunc_image_tuple[0] - optimal threshold value found by otsu threshold.
        thrunc_image_tuple[1] - thrunc binary/grayscale image.
    """
    img = cv2.imread(img_path)
    gray_img = convert_bgr_to_gray(img)
    thrunc_image_tuple = threshold_thrunc_otsu(gray_img, max_threshold)
    return thrunc_image_tuple

### Morphological transformations

def process_erosion_with_rect_kernel(img, kernel_size, iteration=1):
    pass

def process_erosion_with_ellipse_kernel(img, kernel_size, iteration=1):
    pass

def process_erosion_with_cross_kernel(img, kernel_size, iteration=1):
    pass

def process_dilation_with_rect_kernel(img, kernel_size, iteration=1):
    pass

def process_dilation_with_ellipse_kernel(img, kernel_size, iteration=1):
    pass

def process_dilation_with_cross_kernel(img, kernel_size, iteration=1):
    pass

def process_opening_with_rect_kernel(img, kernel_size):
    pass

def process_opening_with_ellipse_kernel(img, kernel_size):
    pass

def process_opening_with_cross_kernel(img, kernel_size):
    pass

def process_closing_with_rect_kernel(img, kernel_size):
    pass

def process_closing_with_ellipse_kernel(img, kernel_size):
    pass

def process_closing_with_cross_kernel(img, kernel_size):
    pass

def process_tophat_with_rect_kernel(img, kernel_size):
    pass

def process_tophat_with_ellipse_kernel(img, kernel_size):
    pass

def process_tophat_with_cross_kernel(img, kernel_size):
    pass

def process_blackhat_with_rect_kernel(img, kernel_size):
    pass

def process_blackhat_with_ellipse_kernel(img, kernel_size):
    pass

def process_blackhat_with_cross_kernel(img, kernel_size):
    pass

