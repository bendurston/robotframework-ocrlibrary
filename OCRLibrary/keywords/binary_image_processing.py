"""
binaryImageProcessing module.
"""
from ..utils.exceptions.exception_handler import \
    verify_valid_image_path, verify_valid_threshold_values
from ..utils.imageprocessing.image_processing_gray import \
    (process_to_gray_scale, process_to_binary_image, process_to_binary_otsu_image, process_to_tozero_image,
    process_to_tozero_otsu_image, process_to_trunc_image, process_to_trunc_otsu_image)

class BinaryImageProcessingKeywords:
    """
    BinaryImageProcessingKeyword Class
    """
    def get_gray_scale_image(self, img_path):
        """
        Converts an image to gray scale.

        Example:
        | ${path}=    Capture Page Screenshot
        | ${gray_scale_image}=    Get Gray Scale Image    ${path}
        """
        verify_valid_image_path(img_path)
        return process_to_gray_scale(img_path)

    def get_binary_image(self, img_path, apply_otsu=False, inverse=False, max_threshold=255, threshold=127):
        """
        Converts an image to a binary image.

        See `introduction` for details about using arguments.
        """
        verify_valid_image_path(img_path)
        verify_valid_threshold_values(threshold, max_threshold)
        if apply_otsu:
            processed_image = process_to_binary_otsu_image(img_path, inverse, max_threshold)
        else:
            processed_image = process_to_binary_image(img_path, inverse, threshold, max_threshold)
        return processed_image

    def get_to_zero_image(self, img_path, apply_otsu=False, inverse=False, max_threshold=255, threshold=127):
        """
        Converts an image to a tozero image.
        All values considered black (if inverse is False) will be set to black, the rest of
        the image will remain in gray scale. If inverse is true, the values considered to be white will be set to black,
        the rest of the image will remain in gray scale.

        See `introduction` for details about using the arguments.
        """
        verify_valid_image_path(img_path)
        verify_valid_threshold_values(threshold, max_threshold)
        if apply_otsu:
            processed_image = process_to_tozero_otsu_image(img_path, inverse, max_threshold)
        else:
            processed_image = process_to_tozero_image(img_path, inverse, threshold, max_threshold)
        return processed_image

    def get_trunc_image(self, img_path, apply_otsu=False, max_threshold=255, threshold=127):
        """
        Converts an image to gray scale and applies truncation threshold. Values considered to be white will be set to white, the
        rest of the image will remain gray scale.

        See `introduction` for details about using the arguments.
        """
        verify_valid_image_path(img_path)
        verify_valid_threshold_values(threshold, max_threshold)
        if apply_otsu:
            processed_image = process_to_trunc_otsu_image(img_path, max_threshold)
        else:
            processed_image = process_to_trunc_image(img_path, threshold, max_threshold)
        return processed_image
