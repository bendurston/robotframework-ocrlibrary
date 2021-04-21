"""
content_validation module.
"""
from ..utils.exceptions.exception_handler \
    import (verify_valid_image, verify_content)
from ..utils.imagereading.image_reading \
    import (return_image_content)

class ContentValidationKeywords:
    """
    ContentValidationKeywords Class
    """
    def validate_image_content(self, processed_img, expected_content, pyt_conf='--psm 6', lang='eng'):
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
            Returns True if content is found.
        """
        verify_valid_image(processed_img)
        actual_content = return_image_content(processed_img, pyt_conf, lang)
        return verify_content(expected_content, actual_content)
