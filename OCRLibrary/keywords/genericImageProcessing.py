"""
genericImageProcessing module.
"""
import cv2
from ..utils.exceptions.exception_handler import verify_valid_image_path

class GenericImageProcessingKeywords():
    """
    GenericImageProcessingKeyword Class
    """

    def read_image(self, img_path):
        """
        Purpose:
            Reads image as is using opencv.
        Args:
            img_path - the path to the image.
        Returns:
            The read image
        """
        verify_valid_image_path(img_path)
        return cv2.imread(img_path)

    def save_image(self, path, img):
        """
        Purpose:
            Saves the image in the specified path.
        Args:
            path - the path the save the image at.
            img - the image being saved (is of type InputArray)
        Returns:
            bool - True if successful, false otherwise.
        """
        verify_valid_image_path(path, False)
        return cv2.imwrite(str(path), img)
