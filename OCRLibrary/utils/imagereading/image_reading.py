"""
High level implementation of image reading (pytesseract) functionality
"""
import pytesseract as pt

def return_image_content(img, config, lang):
    """
    Purpose:
        Returns the text from the image based on the config and languange
    Args:
        img - processed image returned from one of the image processing functions.
        config - configuration to read the image.
        lang - the language of the text to read.
    """
    return pt.image_to_string(img, config=config, lang=lang)
