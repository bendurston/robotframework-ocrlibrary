"""
binaryImageTransformation module.
"""
from ..utils.exceptions.exception_handler import \
    (verify_valid_kernel_size, verify_valid_iteration, raise_invalid_kernel_type, verify_valid_image)
from ..utils.helpers.robot_conversions import \
    (convert_to_valid_kernel_size)
from ..utils.imageprocessing.image_processing_gray import \
    (process_erosion_with_rect_kernel, process_erosion_with_ellipse_kernel, process_erosion_with_cross_kernel,
    process_dilation_with_rect_kernel, process_dilation_with_ellipse_kernel, process_dilation_with_cross_kernel,
    process_opening_with_rect_kernel, process_opening_with_ellipse_kernel, process_opening_with_cross_kernel,
    process_closing_with_rect_kernel, process_closing_with_ellipse_kernel, process_closing_with_cross_kernel,
    process_gradient_with_rect_kernel, process_gradient_with_ellipse_kernel, process_gradient_with_cross_kernel,
    process_tophat_with_rect_kernel, process_tophat_with_ellipse_kernel, process_tophat_with_cross_kernel,
    process_blackhat_with_rect_kernel, process_blackhat_with_ellipse_kernel, process_blackhat_with_cross_kernel)

class BinaryImageTransformationKeywords:
    """
    BinaryImageTransformationKeywords Class
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
