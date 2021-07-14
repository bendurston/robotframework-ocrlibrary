"""
binaryImageTransformation module.

This module is responsible for creating binary images (thresholding), and applying morphological tranformations to binary images.
"""
from ..utils.exceptions.exception_handler import \
    (verify_valid_kernel_size, verify_valid_iteration, raise_invalid_kernel_type, verify_valid_image,
    verify_valid_image_path, verify_valid_threshold_values)
from ..utils.helpers.robot_conversions import \
    (convert_to_valid_kernel_size)
from ..utils.imageprocessing.image_processing_gray import \
    (process_to_binary_image, process_to_binary_otsu_image, process_to_tozero_image,
    process_to_tozero_otsu_image, process_to_trunc_image, process_to_trunc_otsu_image,
    process_erosion_with_rect_kernel, process_erosion_with_ellipse_kernel, process_erosion_with_cross_kernel,
    process_dilation_with_rect_kernel, process_dilation_with_ellipse_kernel, process_dilation_with_cross_kernel,
    process_opening_with_rect_kernel, process_opening_with_ellipse_kernel, process_opening_with_cross_kernel,
    process_closing_with_rect_kernel, process_closing_with_ellipse_kernel, process_closing_with_cross_kernel,
    process_gradient_with_rect_kernel, process_gradient_with_ellipse_kernel, process_gradient_with_cross_kernel,
    process_tophat_with_rect_kernel, process_tophat_with_ellipse_kernel, process_tophat_with_cross_kernel,
    process_blackhat_with_rect_kernel, process_blackhat_with_ellipse_kernel, process_blackhat_with_cross_kernel)

class ImageThresholdingKeywords:
    """
    ImageThresholdingKeywords Class
    Reference: https://docs.opencv.org/4.5.2/d7/d4d/tutorial_py_thresholding.html
    """
    def get_binary_image(self, img_path, apply_otsu=False, inverse=False, max_threshold=255, threshold=127):
        """
        Converts an image to a binary image.

        See `introduction` for details about using arguments.

        For more details about this transformation see the OpenCV image thresholding documentation in the `Information On Image Transformations` section of the introduction.
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

        For more details about this transformation see the OpenCV image thresholding documentation in the `Information On Image Transformations` section of the introduction.
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

        For more details about this transformation see the OpenCV image thresholding documentation in the `Information On Image Transformations` section of the introduction.
        """
        verify_valid_image_path(img_path)
        verify_valid_threshold_values(threshold, max_threshold)
        if apply_otsu:
            processed_image = process_to_trunc_otsu_image(img_path, max_threshold)
        else:
            processed_image = process_to_trunc_image(img_path, threshold, max_threshold)
        return processed_image

class MorphologicalTransformationKeywords:
    """
    MorphologicalTransformationKeywords Class
    Reference: https://docs.opencv.org/4.5.2/d9/d61/tutorial_py_morphological_ops.html
    """

    def apply_erosion_to_image(self, processed_img, kernel_size, kernel_type=0, iteration=1):
        """
        Applies the erosion morphological transformation to a binary image. Kernel size must be a tuple/list of positive ints.

        Example:
        | ${img_path}=    Capture Page Screenshot
        | ${processed_img}=    Get Binary Image    ${img_path}
        | ${kernel_size}=    Create List    1    1
        | ${eroded_img}=    Apply Erosion To Image    ${processed_img}    ${kernel_size}

        See `introduction` for details about using the arguments.

        For more details about this transformation see the OpenCV morphological transformation documentation in the `Information On Image Transformations` section of the introduction.
        """
        verify_valid_image(processed_img)
        verify_valid_kernel_size(kernel_size)
        verify_valid_iteration(iteration)
        kernel_size = convert_to_valid_kernel_size(kernel_size)
        if kernel_type == 0:
            transformed_image = process_erosion_with_rect_kernel(processed_img, kernel_size, iteration)
        elif kernel_type == 1:
            transformed_image = process_erosion_with_ellipse_kernel(processed_img, kernel_size, iteration)
        elif kernel_type == 2:
            transformed_image = process_erosion_with_cross_kernel(processed_img, kernel_size, iteration)
        else:
            return raise_invalid_kernel_type(kernel_type)
        return transformed_image

    def apply_dilation_to_image(self, processed_img, kernel_size, kernel_type=0, iteration=1):
        """
        Applies the dilation morphological transformation to a binary image. Kernel size must be a tuple/list of positive ints.

        See ``Apply Erosion To Image`` for example of general usage.

        See `introduction` for details about using the arguments.

        For more details about this transformation see the OpenCV morphological transformation documentation in the `Information On Image Transformations` section of the introduction.
        """
        verify_valid_image(processed_img)
        verify_valid_kernel_size(kernel_size)
        verify_valid_iteration(iteration)
        kernel_size = convert_to_valid_kernel_size(kernel_size)
        if kernel_type == 0:
            transformed_image = process_dilation_with_rect_kernel(processed_img, kernel_size, iteration)
        elif kernel_type == 1:
            transformed_image = process_dilation_with_ellipse_kernel(processed_img, kernel_size, iteration)
        elif kernel_type == 2:
            transformed_image = process_dilation_with_cross_kernel(processed_img, kernel_size, iteration)
        else:
            return raise_invalid_kernel_type(kernel_type)
        return transformed_image

    def apply_opening_to_image(self, processed_img, kernel_size, kernel_type=0, iteration=1):
        """
        Applies the opening morphological transformation to a binary image. Kernel size must be a tuple/list of positive ints.

        See ``Apply Erosion To Image`` for example of general usage.

        See `introduction` for details about using the arguments.

        For more details about this transformation see the OpenCV morphological transformation documentation in the `Information On Image Transformations` section of the introduction.
        """
        verify_valid_image(processed_img)
        verify_valid_kernel_size(kernel_size)
        verify_valid_iteration(iteration)
        kernel_size = convert_to_valid_kernel_size(kernel_size)
        if kernel_type == 0:
            transformed_image = process_opening_with_rect_kernel(processed_img, kernel_size)
        elif kernel_type == 1:
            transformed_image = process_opening_with_ellipse_kernel(processed_img, kernel_size)
        elif kernel_type == 2:
            transformed_image = process_opening_with_cross_kernel(processed_img, kernel_size)
        else:
            return raise_invalid_kernel_type(kernel_type)
        return transformed_image

    def apply_closing_to_image(self, processed_img, kernel_size, kernel_type=0, iteration=1):
        """
        Applies the closing morphological transformation to a binary image. Kernel size must be a tuple/list of positive ints.

        See ``Apply Erosion To Image`` for example of general usage.

        See `introduction` for details about using the arguments.

        For more details about this transformation see the OpenCV morphological transformation documentation in the `Information On Image Transformations` section of the introduction.
        """
        verify_valid_image(processed_img)
        verify_valid_kernel_size(kernel_size)
        verify_valid_iteration(iteration)
        kernel_size = convert_to_valid_kernel_size(kernel_size)
        if kernel_type == 0:
            transformed_image = process_closing_with_rect_kernel(processed_img, kernel_size)
        elif kernel_type == 1:
            transformed_image = process_closing_with_ellipse_kernel(processed_img, kernel_size)
        elif kernel_type == 2:
            transformed_image = process_closing_with_cross_kernel(processed_img, kernel_size)
        else:
            return raise_invalid_kernel_type(kernel_type)
        return transformed_image

    def apply_gradient_to_image(self, processed_img, kernel_size, kernel_type=0, iteration=1):
        """
        Applies the gradient morphological transformation to a binary image. Kernel size must be a tuple/list of positive ints.

        See ``Apply Erosion To Image`` for example of general usage.

        See `introduction` for details about using the arguments.
        
        For more details about this transformation see the OpenCV morphological transformation documentation in the `Information On Image Transformations` section of the introduction.
        """
        verify_valid_image(processed_img)
        verify_valid_kernel_size(kernel_size)
        verify_valid_iteration(iteration)
        kernel_size = convert_to_valid_kernel_size(kernel_size)
        if kernel_type == 0:
            transformed_image = process_gradient_with_rect_kernel(processed_img, kernel_size)
        elif kernel_type == 1:
            transformed_image = process_gradient_with_ellipse_kernel(processed_img, kernel_size)
        elif kernel_type == 2:
            transformed_image = process_gradient_with_cross_kernel(processed_img, kernel_size)
        else:
            return raise_invalid_kernel_type(kernel_type)
        return transformed_image

    def apply_top_hat_to_image(self, processed_img, kernel_size, kernel_type=0, iteration=1):
        """
        Applies the top hat morphological transformation to a binary image. Kernel size must be a tuple/list of positive ints.

        See ``Apply Erosion To Image`` for example of general usage.

        See `introduction` for details about using the arguments.

        For more details about this transformation see the OpenCV morphological transformation documentation in the `Information On Image Transformations` section of the introduction.
        """
        verify_valid_image(processed_img)
        verify_valid_kernel_size(kernel_size)
        verify_valid_iteration(iteration)
        kernel_size = convert_to_valid_kernel_size(kernel_size)
        if kernel_type == 0:
            transformed_image = process_tophat_with_rect_kernel(processed_img, kernel_size)
        elif kernel_type == 1:
            transformed_image = process_tophat_with_ellipse_kernel(processed_img, kernel_size)
        elif kernel_type == 2:
            transformed_image = process_tophat_with_cross_kernel(processed_img, kernel_size)
        else:
            return raise_invalid_kernel_type(kernel_type)
        return transformed_image

    def apply_black_hat_to_image(self, processed_img, kernel_size, kernel_type=0, iteration=1):
        """
        Applies the black hat morphological transformation to a binary image. Kernel size must be a tuple/list of positive ints.

        See ``Apply Erosion To Image`` for example of general usage.

        See `introduction` for details about using the arguments.

        For more details about this transformation see the OpenCV morphological transformation documentation in the `Information On Image Transformations` section of the introduction.
        """
        verify_valid_image(processed_img)
        verify_valid_kernel_size(kernel_size)
        verify_valid_iteration(iteration)
        kernel_size = convert_to_valid_kernel_size(kernel_size)
        if kernel_type == 0:
            transformed_image = process_blackhat_with_rect_kernel(processed_img, kernel_size)
        elif kernel_type == 1:
            transformed_image = process_blackhat_with_ellipse_kernel(processed_img, kernel_size)
        elif kernel_type == 2:
            transformed_image = process_blackhat_with_cross_kernel(processed_img, kernel_size)
        else:
            raise_invalid_kernel_type(kernel_type)
        return transformed_image
