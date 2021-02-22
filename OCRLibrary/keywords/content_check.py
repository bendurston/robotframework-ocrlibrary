"""
This library will check if content exists on the page.
"""
from utils.imageprocessing.imagereading import .


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
    Returns:
        None?
    """
    actual_content = return_image_content(processed_img, pyt_conf, lang)
    if expected_content not in actual_content:
        raise #TODO custom error handlers.
        
    
