"""
genericImageProcessing module.
"""
import os
import cv2
from ..utils.exceptions.exception_handler import verify_valid_image_path
from ..utils.helpers.logging import get_log_dir, log_info

class ReadImageKeywords:
    """
    ReadImageKeywords Class
    """
    def read_image(self, img_path):
        """
        Reads an image.

        Example:
        | ${img_path}=    Capture Page Screenshot
        | ${read_image}=    Read Image    ${img_path}

        See `Reading And Saving Images` for details about valid images to provide.
        """
        verify_valid_image_path(img_path)
        return cv2.imread(img_path)

class SaveImageKeywords:
    """
    SaveImageKeywords Class
    """
    def __init__(self):
        self.saved_image_count = 0

    def save_image(self, img, path=None):
        """
        Saves processed image to log directory. Add path with image name and file extension to save image elsewhere.
        Returns True if successful, otherwise returns False.

        Example:
        | Save Image    ${processed_img}

        Example with specified location:
        | Save Image    ${processed_img}    home/usr/Pictures/save_image_result.png    

        See `Reading And Saving Images` for details about valid image formats.
        """
        if path is not None:
            verify_valid_image_path(path, False)
        else:
            self.saved_image_count += 1
            log_dir = get_log_dir()
            image_name = f'ocrlibrary-saved-image-{self.saved_image_count}.png'
            path = os.path.join(log_dir, image_name)
        message = f'<a href="{path}""><img src="{path}" width="800px"></a>'
        log_info(message, True)
        return cv2.imwrite(str(path), img)
