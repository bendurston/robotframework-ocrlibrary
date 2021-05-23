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
        Confirms that an image contains the expected content. If the content is not found, ``ContentNotFound`` will be raised.

        See `introduction` for details about pyt_conf and lang arguments.
        """
        verify_valid_image(processed_img)
        actual_content = return_image_content(processed_img, pyt_conf, lang)
        return verify_content(expected_content, actual_content)

    def get_image_content(self, processed_img, pyt_conf='--psm 6', lang='eng'):
        """
        Gets the text found within the provided processed image.

        See `introduction` for details about pyt_conf and lang arguments.
        """
        verify_valid_image(processed_img)
        return return_image_content(processed_img, pyt_conf, lang)
