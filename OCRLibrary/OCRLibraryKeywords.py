"""
Robot Framework Keywords
"""
import numpy
import cv2
from utils.imageprocessing.image_processing_gray import .
from utils.imageprocessing.image_processing_colour import .
from utils.imagereading.image_reading import .
from utils.imagereading.text_locating import .

from utils.exceptions.content_validation_exceptions import .
from utils.exceptions.common_exceptions import .

#### Content Validation Keywords - Start ####
def Validate_Image_Content(processed_img, expected_content, index=0, pyt_conf='--psm 6', lang='eng'):
    """
    Purpose:
        Confirm that an image contains the expected content. 
    Args:
        processed_img - a read and processed image (result of any of the image processing keywords)
        expected_content - content to check for in the image
        index - the occurance of the actual text (e.g. index=1 will check if there expected content is in the second occurance).
        pyt_conf - pytesseract configuration (see README.md) defaulted to --psm 6
        lang - the language used in the image defaulted to english
    """
    if isinstance(processed_img, numpy.ndarray):
        actual_content = return_image_content(processed_img, pyt_conf, lang)
        if expected_content not in actual_content:
            raise ContentNotFound(f"The expected content: {expected_content}\nwas not found in the actual content: {actual_content}")    
    else:
        raise InvalidImageArgument("The argument provided is invalid. Please give an image that has been returned from any of the image processing keywords.")

#### Content Validation Keywords - End ####

#### Content Location Keywords - Start ####
def Locate_Text_Coordinates(processed_img, text, pyt_conf='--psm 6', lang='eng'):
    """
    """
    # TODO Check if tuple or list should be returned for access in robotframework
    if isinstance(processed_img, numpy.ndarray):
        coordinates = return_text_coordinates(processed_img, text, pyt_conf, lang)
    else:
        raise InvalidImageArgument("The argument provided is invalid. Please give an image that has been returned from any of the image processing keywords.")
    return coordinates

def Locate_Multiple_Text_Coordinates(processed_img, text, pyt_conf='--psm 6', lang='eng'):
    """
    """
    if isinstance(processed_img, numpy.ndarray):
        multiple_coordinates = return_multiple_text_coordinates(processed_img, text, pyt_conf, lang)
    else:
        raise InvalidImageArgument("The argument provided is invalid. Please give an image that has been returned from any of the image processing keywords.")
    return multiple_coordinates

def Locate_Text_Bounds(processed_img, text, pyt_conf='--psm 6', lang='eng'):
    """
    """
    if isinstance(processed_img, numpy.ndarray):
        bounds = return_text_bounds(processed_img, text, pyt_conf, lang)
    else:
        raise InvalidImageArgument("The argument provided is invalid. Please give an image that has been returned from any of the image processing keywords.")
    return bounds

def Locate_Multiple_Text_Bounds(processed_img, text, pyt_conf='--psm 6', lang='eng'):
    """
    """
    if isinstance(processed_img, numpy.ndarray):
        multiple_bounds = return_multiple_text_bounds(processed_img, text, pyt_conf, lang)
    else:
        raise InvalidImageArgument("The argument provided is invalid. Please give an image that has been returned from any of the image processing keywords.")
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

# TODO: Create Keywords that do the basic grayscale with/without thresholding (one just plain bgr to gray)
# TODO: Then make keywords that have the prefix "Apply" to apply any other image processing technique.

#### Image Processing Keywords - End

def Save_Image(path, img):
    """
    Purpose:
        Saves the image in the specified path.
    Args:
        path - the path the save the image at.
        img - the image being saved (is of type InputArray)
    """
    cv2.imwrite(str(path), img)

