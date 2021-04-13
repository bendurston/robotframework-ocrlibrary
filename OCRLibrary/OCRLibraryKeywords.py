"""
Robot Framework Keywords
"""
import cv2
from OCRLibrary.utils.imageprocessing.image_processing_gray import *
from OCRLibrary.utils.imageprocessing.image_processing_colour import *
from OCRLibrary.utils.imageprocessing.image_processing_generic import *
from OCRLibrary.utils.imagereading.image_reading import *
from OCRLibrary.utils.imagereading.text_locating import *

from OCRLibrary.utils.exceptions.exception_handler import *

#### Content Validation Keywords - Start ####
def Validate_Image_Content(processed_img, expected_content, pyt_conf='--psm 6', lang='eng'):
    """
    Purpose:
        Confirm that an image contains the expected content

    Args:
        processed_img - a read and processed image (result of any of the image processing keywords)
        expected_content - content to check for in the image
        index - the occurance of the actual text (e.g. index=1 will check if there expected content is in the second occurance).
        pyt_conf - pytesseract configuration (see README.md) defaulted to --psm 6
        lang - the language used in the image defaulted to english
    """
    verify_valid_image(processed_img)
    actual_content = return_image_content(processed_img, pyt_conf, lang)
    return verify_content(expected_content, actual_content)
#### Content Validation Keywords - End ####

#### Content Location Keywords - Start ####
def Locate_Text_Coordinates(processed_img, text, pyt_conf='--psm 6', lang='eng'):
    """
    """
    # TODO Check if tuple or list should be returned for access in robotframework
    # TODO Throw error if return is None
    verify_valid_image(processed_img)
    coordinates = return_text_coordinates(processed_img, text, pyt_conf, lang)
    return coordinates

def Locate_Multiple_Text_Coordinates(processed_img, text, pyt_conf='--psm 6', lang='eng'):
    """
    """
    # TODO Throw error if return is empty
    verify_valid_image(processed_img)
    multiple_coordinates = return_multiple_text_coordinates(processed_img, text, pyt_conf, lang)
    return multiple_coordinates

def Locate_Text_Bounds(processed_img, text, pyt_conf='--psm 6', lang='eng'):
    """
    """
    # TODO Throw error if return is None
    verify_valid_image(processed_img)
    bounds = return_text_bounds(processed_img, text, pyt_conf, lang)
    return bounds

def Locate_Multiple_Text_Bounds(processed_img, text, pyt_conf='--psm 6', lang='eng'):
    """
    """
    # TODO Throw error if return is empty
    verify_valid_image(processed_img)
    multiple_bounds = return_multiple_text_bounds(processed_img, text, pyt_conf, lang)
    return multiple_bounds

#### Location Check Keywords - End ####

#### Image Processing Keywords - Start ####
def Get_Gray_Scale_Image(img_path):
    """
    Purpose:
        Convert image to gray scale
    Args:
        img_path - the path to the image.
    Returns:
        A read image in gray scale.
    """
    return process_to_gray_scale(img_path)

def Get_Binary_Image(img_path, apply_otsu=False, inverse=False, max_threshold=255, threshold=127):
    """
    Purpose:
        Process image to a binary image.
        If apply_otsu is true, a tuple will be returned. Index 0 contains the optimal threshold value found by
        the ostu threshold, and index 1 has the binary image.
    Args:
        img_path - path to the image to process
        apply_otsu - boolean, apply otsu threshold to the image.
        inverse - if true an inverted binary thresholding will be applied (optional). 
        threshold - threshold value used to classify the pixel values (optional).
        max_threshold - the max value to be given if a pixels value is more than the threshold value (optional).
    Returns:
        A binary image.
    """
    if apply_otsu:
        # TODO check for valid threshold values for otsu.
        return process_to_binary_otsu_image(img_path, inverse, max_threshold)
    else:
        # TODO check for valid threshold values.
        return process_to_binary_image(img_path, inverse, threshold, max_threshold)

def Get_To_Zero_Image(img_path, apply_otsu=False, inverse=False, max_threshold=255, threshold=127):
    """
    Purpose:
        Process image to a tozero image. 
        All values considered black (if no inverse) will be set to black, the rest of 
        the image will remain in gray scale. If inverse is true, the values considered to be white will be set to black,
        the rest of the image will remain in gray scale.
        If apply_otsu is true, a tuple will be returned. Index 0 contains the optimal threshold value found by
        the ostu threshold, and index 1 has the tozero image.
    Args:
        img_path - path to the image to process
        apply_otsu - boolean, apply otsu threshold to the image.
        inverse - if true an inverted tozeo thresholding will be applied (optional). 
        threshold - threshold value used to classify the pixel values (optional).
        max_threshold - the max value to be given if a pixels value is more than the threshold value (optional).
    Returns:
        A tozero image.
    """
    if apply_otsu:
        # TODO check for valid threshold values for otsu.
        return process_to_tozero_otsu_image(img_path, inverse, max_threshold)
    else:
        # TODO check for valid threshold values.
        return process_to_tozero_image(img_path, inverse, threshold, max_threshold)

def Get_Trunc_Image(img_path, apply_otsu=False, max_threshold=255, threshold=127):
    """
    Purpose:
        Process an image to gray scale and apply truncation threshold (values considered to be white will be set to white, the 
        rest of the image will remain gray scale).
        If apply_otsu is true, a tuple will be returned. Index 0 contains the optimal threshold value found by
        the ostu threshold, and index 1 has the tozero image.
    Args:
        img_path - path to the image to process
        apply_otsu - boolean, apply otsu threshold to the image.
        threshold - threshold value used to classify the pixel values (optional).
        max_threshold - the max value to be given if a pixels value is more than the threshold value (optional).
    Returns:
        A trunc image.
    """
    if apply_otsu:
        # TODO check for valid threshold values for otsu.
        return process_to_trunc_otsu_image(img_path, max_threshold)
    else:
        # TODO check for valid threshold values.
        return process_to_trunc_image(img_path, threshold, max_threshold)
        
# Binary images transformations - start

def Apply_Erosion_To_Image(img, kernel_size, kernel_type=0, iteration=1):
    """
    Purpose:
        Applies the erosion morphological transformation to a binary image.
    Args:
        img - processed binary image.
        kernel_size - size of the kernel
        kernel_type - shape of kernel used. 0 = rectangle, 1 = ellipse, and 2 = cross.
        iteration - number of iterations to perform on image.
    Returns:
        Image with erosion morphological transformation applied.
    """
    verify_valid_kernel_size(kernel_size)
    verify_valid_iteration(iteration)
    if kernel_type == 0:
        return process_erosion_with_rect_kernel(img, kernel_size, iteration)
    elif kernel_type == 1:
        return process_erosion_with_ellipse_kernel(img, kernel_size, iteration)
    elif kernel_type == 2:
        return process_erosion_with_cross_kernel(img, kernel_size, iteration)
    else:
        raise_invalid_kernel_type(kernel_type)

def Apply_Dilation_To_Image(img, kernel_size, kernel_type=0, iteration=1):
    """
    Purpose:
        Applies the dilation morphological transformation to a binary image.
    Args:
        img - processed binary image.
        kernel_size - size of the kernel
        kernel_type - shape of kernel used. 0 = rectangle, 1 = ellipse, and 2 = cross.
        iteration - number of iterations to perform on image.
    Returns:
        Image with dilation morphological transformation applied.
    """
    verify_valid_kernel_size(kernel_size)
    verify_valid_iteration(iteration)
    if kernel_type == 0:
        return process_dilation_with_rect_kernel(img, kernel_size, iteration)
    elif kernel_type == 1:
        return process_dilation_with_ellipse_kernel(img, kernel_size, iteration)
    elif kernel_type == 2:
        return process_dilation_with_cross_kernel(img, kernel_size, iteration)
    else:
        raise_invalid_kernel_type(kernel_type)    
    
def Apply_Opening_To_Image(img, kernel_size, kernel_type=0):
    """
    Purpose:
        Applies the opening morphological transformation to a binary image.
    Args:
        img - processed binary image.
        kernel_size - size of the kernel
        kernel_type - shape of kernel used. 0 = rectangle, 1 = ellipse, and 2 = cross.
    Returns:
        Image with opening morphological transformation applied.
    """
    verify_valid_kernel_size(kernel_size)
    if kernel_type == 0:
        return process_opening_with_rect_kernel(img, kernel_size)
    elif kernel_type == 1:
        return process_opening_with_ellipse_kernel(img, kernel_size)
    elif kernel_type == 2:
        return process_opening_with_cross_kernel(img, kernel_size)
    else:
        raise_invalid_kernel_type(kernel_type)

def Apply_Closing_To_Image(img, kernel_size, kernel_type=0):
    """
    Purpose:
        Applies the closing morphological transformation to a binary image.
    Args:
        img - processed binary image.
        kernel_size - size of the kernel
        kernel_type - shape of kernel used. 0 = rectangle, 1 = ellipse, and 2 = cross.
    Returns:
        Image with closing morphological transformation applied.
    """
    verify_valid_kernel_size(kernel_size)
    if kernel_type == 0:
        return process_closing_with_rect_kernel(img, kernel_size)
    elif kernel_type == 1:
        return process_closing_with_ellipse_kernel(img, kernel_size)
    elif kernel_type == 2:
        return process_closing_with_cross_kernel(img, kernel_size)
    else:
        raise_invalid_kernel_type(kernel_type)

def Apply_Gradient_To_Image(img, kernel_size, kernel_type=0):
    """
    Purpose:
        Applies the gradient morphological transformation to a binary image.
    Args:
        img - processed binary image.
        kernel_size - size of the kernel
        kernel_type - shape of kernel used. 0 = rectangle, 1 = ellipse, and 2 = cross.
    Returns:
        Image with gradien morphological transformation applied.
    """
    verify_valid_kernel_size(kernel_size)
    if kernel_type == 0:
        return process_gradient_with_rect_kernel(img, kernel_size)
    elif kernel_type == 1:
        return process_gradient_with_ellipse_kernel(img, kernel_size)
    elif kernel_type == 2:
        return process_gradient_with_cross_kernel(img, kernel_size)
    else:
        raise_invalid_kernel_type(kernel_type)

def Apply_Top_Hat_To_Image(img, kernel_size, kernel_type=0):
    """
    Purpose:
        Applies the top hat morphological transformation to a binary image.
    Args:
        img - processed binary image.
        kernel_size - size of the kernel
        kernel_type - shape of kernel used. 0 = rectangle, 1 = ellipse, and 2 = cross.
    Returns:
        Image with top hat morphological transformation applied.
    """
    verify_valid_kernel_size(kernel_size)
    if kernel_type == 0:
        return process_tophat_with_rect_kernel(img, kernel_size)
    elif kernel_type == 1:
        return process_tophat_with_ellipse_kernel(img, kernel_size)
    elif kernel_type == 2:
        return process_tophat_with_cross_kernel(img, kernel_size)
    else:
        raise_invalid_kernel_type(kernel_type)

def Apply_Black_Hat_To_Image(img, kernel_size, kernel_type=0):
    """
    Purpose:
        Applies the black hat morphological transformation to a binary image.
    Args:
        img - processed binary image.
        kernel_size - size of the kernel
        kernel_type - shape of kernel used. 0 = rectangle, 1 = ellipse, and 2 = cross.
    Returns:
        Image with black hat morphological transformation applied.
    """
    verify_valid_kernel_size(kernel_size)
    if kernel_type == 0:
        processed_image = process_blackhat_with_rect_kernel(img, kernel_size)
    elif kernel_type == 1:
        processed_image = process_blackhat_with_ellipse_kernel(img, kernel_size)
    elif kernel_type == 2:
        processed_image = process_blackhat_with_cross_kernel(img, kernel_size)
    else:
        raise_invalid_kernel_type(kernel_type)
    return processed_image
# Binary images transformations - end

# Generic image (any colour) transformations - start
def Apply_Filter2D_To_Image(img, kernel_size, kernel_type=0, depth=-1):
    """
    Purpose:
        Applies the filter2D filter to the image.
    Args:
        img - processed image.
        kernel_size - size of the kernel
        kernel_type - shape of kernel used. 0 = rectangle, 1 = ellipse, and 2 = cross.
        depth - desired depth of the destination image.
            when depth=-1, the output image will have the same depth as the source.
    Returns:
        Image with filter2D filtering applied.
    """
    # TODO verify valid depth?
    verify_valid_kernel_size(kernel_size)
    if kernel_type == 0:
        processed_image = process_image_filtering_with_rect_kernel(img, kernel_size, depth)
    elif kernel_type == 1:
        processed_image = process_image_filtering_with_ellipse_kernel(img, kernel_size, depth)
    elif kernel_type == 2:
        processed_image = process_image_filtering_with_cross_kernel(img, kernel_size, depth)
    else:
        return raise_invalid_kernel_type(kernel_type)
    return processed_image

def Apply_Median_Filtering_To_Image(img, kernel_size):
    """
    Purpose:
        Applies the median filter to the image.
    Args:
        img - processed image.
        kernel_size - size of the kernel
    Returns:
        Image with a median filter applied.
    """
    verify_valid_kernel_size(kernel_size)
    return process_median_filtering(img, kernel_size)

def Apply_Averaging_Blur_To_Image(img, kernel_size, kernel_type=0):
    """
    Purpose:
        Applies the averaging blur to the image.
    Args:
        img - processed image.
        kernel_size - size of the kernel
        kernel_type - shape of kernel used. 0 = rectangle, 1 = ellipse, and 2 = cross.
    Returns:
        Image with an averaging blur applied.
    """
    verify_valid_kernel_size(kernel_size)
    if kernel_type == 0:
        processed_image = process_blurring_averaging_with_rect_kernel(img, kernel_size)
    elif kernel_type == 1:
        processed_image = process_blurring_averaging_with_ellipse_kernel(img, kernel_size)
    elif kernel_type == 2:
        processed_image = process_blurring_averaging_with_cross_kernel(img, kernel_size)
    else:
        return raise_invalid_kernel_type(kernel_type)
    return processed_image

def Apply_Gaussian_Blur_To_Image(img, kernel_size, kernel_type=0):
    """
    Purpose:
        Applies the gaussian blur to the image.
    Args:
        img - processed image.
        kernel_size - size of the kernel
        kernel_type - shape of kernel used. 0 = rectangle, 1 = ellipse, and 2 = cross.
    Returns:
        Image with a gaussian blur applied.
    """
    verify_valid_kernel_size(kernel_size)
    if kernel_type == 0:
        processed_image = process_blurring_gaussian_with_rect_kernel(img, kernel_size)
    elif kernel_type == 1:
        processed_image = process_blurring_gaussian_with_ellipse_kernel(img, kernel_size)
    elif kernel_type == 2:
        processed_image = process_blurring_gaussian_with_cross_kernel(img, kernel_size)
    else:
        return raise_invalid_kernel_type(kernel_type)
    return processed_image
# Generic image (any colour) transformations - end

#### Image Processing Keywords - End

def Save_Image(path, img):
    """
    Purpose:
        Saves the image in the specified path.
    Args:
        path - the path the save the image at.
        img - the image being saved (is of type InputArray)
    Returns:
        bool - True if successful, false otherwise.
    """
    return cv2.imwrite(str(path), img)
