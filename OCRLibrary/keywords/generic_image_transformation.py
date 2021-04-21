"""
generic_image_transformation module.
"""
from ..utils.exceptions.exception_handler \
    import (verify_valid_kernel_size, verify_valid_depth, raise_invalid_kernel_type, verify_valid_kernel_size_non_tuple)
from ..utils.imageprocessing.image_processing_generic \
    import (process_image_filtering_with_rect_kernel, process_image_filtering_with_ellipse_kernel, process_image_filtering_with_cross_kernel,
    process_median_filtering, process_blurring_averaging, process_blurring_gaussian)

class GenericImageTransformationKeywords:
    """
    GenericImageTransformationKeywords Class
    """
    def apply_filter2D_to_image(self, img, kernel_size, kernel_type=0, depth=-1):
        """
        Purpose:
            Applies the filter2D filter to the image.
        Args:
            img - processed image.
            kernel_size - size of the kernel
            kernel_type - shape of kernel used. 0 = rectangle, 1 = ellipse, and 2 = cross.
            depth - desired depth of the destination image.
                when depth=-1, the output image will have the same depth as the source.
        Returns:
            Image with filter2D filtering applied.
        """
        verify_valid_kernel_size(kernel_size)
        verify_valid_depth(depth)
        if kernel_type == 0:
            processed_image = process_image_filtering_with_rect_kernel(img, kernel_size, depth)
        elif kernel_type == 1:
            processed_image = process_image_filtering_with_ellipse_kernel(img, kernel_size, depth)
        elif kernel_type == 2:
            processed_image = process_image_filtering_with_cross_kernel(img, kernel_size, depth)
        else:
            return raise_invalid_kernel_type(kernel_type)
        return processed_image

    def apply_median_filtering_to_image(self, img, kernel_size):
        """
        Purpose:
            Applies the median filter to the image.
        Args:
            img - processed image.
            kernel_size - size of the kernel (int that is odd and greater than 0)
        Returns:
            Image with a median filter applied.
        """
        verify_valid_kernel_size_non_tuple(kernel_size)
        return process_median_filtering(img, kernel_size)

    def apply_averaging_blur_to_image(self, img, kernel_size):
        """
        Purpose:
            Applies the averaging blur to the image.
        Args:
            img - processed image.
            kernel_size - size of the kernel
        Returns:
            Image with an averaging blur applied.
        """
        verify_valid_kernel_size(kernel_size)
        return process_blurring_averaging(img, kernel_size)

    def apply_gaussian_blur_to_image(self, img, kernel_size):
        """
        Purpose:
            Applies the gaussian blur to the image.
        Args:
            img - processed image.
            kernel_size - size of the kernel
        Returns:
            Image with a gaussian blur applied.
        """
        verify_valid_kernel_size(kernel_size)
        return process_blurring_gaussian(img, kernel_size)
