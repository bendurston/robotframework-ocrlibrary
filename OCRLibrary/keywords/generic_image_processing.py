"""
genericImageProcessing module.
"""
import cv2
from ..utils.exceptions.exception_handler import verify_valid_image_path

class GenericImageProcessingKeywords:
    """
    GenericImageProcessingKeyword Class
    """
    def read_image(self, img_path):
        """
        Reads an image.

        Example:
        | ${img_path}=    Capture Page Screenshot
        | ${read_image}=    Read Image    ${img_path}

        See ``introduction`` for details about valid images to provide.
        """
        verify_valid_image_path(img_path)
        return cv2.imread(img_path)

    def save_image(self, path, img):
        """
        Saves the provided image to the specified path. Returns True if successful,
        otherwise returns False.

        Example:
        | Save Image    home/usr/Pictures/save_image_result.png    ${processed_img}

        See ``introduction`` for details about valid image formats.
        """
        verify_valid_image_path(path, False)
        return cv2.imwrite(str(path), img)
