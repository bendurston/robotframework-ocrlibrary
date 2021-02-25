"""
Robot Framework Keywords
"""
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
    try:
        if cv2.haveImageReader(processed_img):
            raise InvalidImageArgument("The argument provided is invalid. Please give an image that has been returned from any of the image processing keywords.")
    except TypeError:
        actual_content = return_image_content(processed_img, pyt_conf, lang)
        if expected_content not in actual_content:
            raise ContentNotFound(f"The expected content: {expected_content}\nwas not found in the actual content: {actual_content}")
    except:
        # May need to adjust message after testing.
        raise InvalidImageArgument("The argument provided is invalid. Please give an image that has been returned from any of the image processing keywords.")

#### Content Validation Keywords - End ####

#### Content Location Keywords - Start ####
# TODO
#### Location Check Keywords - End ####

#### Image Processing Keywords - Start ####
# TODO
#### Image Processing Keywords - End