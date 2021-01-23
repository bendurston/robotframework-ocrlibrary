"""
This library will check if content exists on the page.
"""
import pytesseract

def Validate_Page_Content(img, expected_content, lang='eng', pyt_conf='--psm 6'):
    """
    Checks for expected content in image.
    """
    text = pytesseract.image_to_string(img, config=pyt_conf, lang=lang)
    if expected_content in text:
        return True
    return False
