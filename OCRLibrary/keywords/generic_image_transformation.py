"""
generic_image_transformation module.
"""
from ..utils.exceptions.exception_handler \
    import (verify_valid_kernel_size, verify_valid_depth, raise_invalid_kernel_type, verify_valid_kernel_size_non_tuple,
    verify_valid_image)
from ..utils.imageprocessing.image_processing_generic \
    import (process_image_filtering_with_rect_kernel, process_image_filtering_with_ellipse_kernel, process_image_filtering_with_cross_kernel,
    process_median_filtering, process_blurring_averaging, process_blurring_gaussian)

class GenericImageTransformationKeywords:
    """
    GenericImageTransformationKeywords Class
    """
    def apply_filter2D_to_image(self, processed_img, kernel_size, kernel_type=0, depth=-1):
        """
        Applies the filter2D filter to the provided image.

        Example:
        | ${img_path}=    Capture Page Screenshot
        | ${processed_img}=    Read Image    ${img_path}
        | ${filtered_img}=    Apply Filter2D To Image    ${processed_img}    (1, 1)

        See `introduction` for details about using arguments.
        """
        verify_valid_image(processed_img)
        verify_valid_kernel_size(kernel_size)
        verify_valid_depth(depth)
        if kernel_type == 0:
            transformed_image = process_image_filtering_with_rect_kernel(processed_img, kernel_size, depth)
        elif kernel_type == 1:
            transformed_image = process_image_filtering_with_ellipse_kernel(processed_img, kernel_size, depth)
        elif kernel_type == 2:
            transformed_image = process_image_filtering_with_cross_kernel(processed_img, kernel_size, depth)
        else:
            return raise_invalid_kernel_type(kernel_type)
        return transformed_image

    def apply_median_filtering_to_image(self, processed_img, kernel_size):
        """
        Applies the median filter to the provided image.
        ``kernel_size`` takes an integer that is odd and greater than 0. Not a tuple.

        See ``Apply Filter2D To Image`` for example of general usage.

        See `introduction` for details about using arguments.
        """
        verify_valid_image(processed_img)
        verify_valid_kernel_size_non_tuple(kernel_size)
        return process_median_filtering(processed_img, kernel_size)

    def apply_averaging_blur_to_image(self, processed_img, kernel_size):
        """
        Applies the averaging blur to the provided image.

        See ``Apply Filter2D To Image`` for example of general usage.

        See `introduction` for details about using arguments.
        """
        verify_valid_image(processed_img)
        verify_valid_kernel_size(kernel_size)
        return process_blurring_averaging(processed_img, kernel_size)

    def apply_gaussian_blur_to_image(self, processed_img, kernel_size):
        """
        Applies the gaussian blur to the provided image.

        See ``Apply Filter2D To Image`` for example of general usage.

        See `introduction` for details about using arguments.
        """
        verify_valid_image(processed_img)
        verify_valid_kernel_size(kernel_size)
        return process_blurring_gaussian(processed_img, kernel_size)
