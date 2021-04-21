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
        Purpose:
            Convert image to gray scale
        Args:
            img_path - the path to the image.
        Returns:
            A read image in gray scale.
        """
        verify_valid_image_path(img_path)
        return process_to_gray_scale(img_path)

    def get_binary_image(self, img_path, apply_otsu=False, inverse=False, max_threshold=255, threshold=127):
        """
        Purpose:
            Process image to a binary image.
            If apply_otsu is true, a tuple will be returned. Index 0 contains the optimal threshold value found by
            the ostu threshold, and index 1 has the binary image.
        Args:
            img_path - path to the image to process
            apply_otsu - boolean, apply otsu threshold to the image.
            inverse - if true an inverted binary thresholding will be applied (optional).
            threshold - threshold value used to classify the pixel values (optional).
            max_threshold - the max value to be given if a pixels value is more than the threshold value (optional).
        Returns:
            A binary image. If applying otsu, a tuple will be returned. For otsu tuple[0] is the optimal threshold value,
            tuple[1] is the binary image.
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
        Purpose:
            Process image to a tozero image.
            All values considered black (if no inverse) will be set to black, the rest of
            the image will remain in gray scale. If inverse is true, the values considered to be white will be set to black,
            the rest of the image will remain in gray scale.
            If apply_otsu is true, a tuple will be returned. Index 0 contains the optimal threshold value found by
            the ostu threshold, and index 1 has the tozero image.
        Args:
            img_path - path to the image to process
            apply_otsu - boolean, apply otsu threshold to the image.
            inverse - if true an inverted tozeo thresholding will be applied (optional).
            threshold - threshold value used to classify the pixel values (optional).
            max_threshold - the max value to be given if a pixels value is more than the threshold value (optional).
        Returns:
            A tozero image. If applying otsu, a tuple will be returned. For otsu tuple[0] is the optimal threshold value,
            tuple[1] is the tozero image.
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
        Purpose:
            Process an image to gray scale and apply truncation threshold (values considered to be white will be set to white, the
            rest of the image will remain gray scale).
            If apply_otsu is true, a tuple will be returned. Index 0 contains the optimal threshold value found by
            the ostu threshold, and index 1 has the tozero image.
        Args:
            img_path - path to the image to process
            apply_otsu - boolean, apply otsu threshold to the image.
            threshold - threshold value used to classify the pixel values (optional).
            max_threshold - the max value to be given if a pixels value is more than the threshold value (optional).
        Returns:
            A trunc image. If applying otsu, a tuple will be returned. For otsu tuple[0] is the optimal threshold value,
            tuple[1] is the trunc image.
        """
        verify_valid_image_path(img_path)
        verify_valid_threshold_values(threshold, max_threshold)
        if apply_otsu:
            processed_image = process_to_trunc_otsu_image(img_path, max_threshold)
        else:
            processed_image = process_to_trunc_image(img_path, threshold, max_threshold)
        return processed_image
