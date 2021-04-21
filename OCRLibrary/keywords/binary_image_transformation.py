"""
binaryImageTransformation module.
"""
from ..utils.exceptions.exception_handler import \
    verify_valid_kernel_size, verify_valid_iteration, raise_invalid_kernel_type
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
    def apply_erosion_to_image(self, img, kernel_size, kernel_type=0, iteration=1):
        """
        Purpose:
            Applies the erosion morphological transformation to a binary image.
        Args:
            img - processed binary image.
            kernel_size - size of the kernel
            kernel_type - shape of kernel used. 0 = rectangle, 1 = ellipse, and 2 = cross.
            iteration - number of iterations to perform on image.
        Returns:
            Image with erosion morphological transformation applied.
        """
        verify_valid_kernel_size(kernel_size)
        verify_valid_iteration(iteration)
        if kernel_type == 0:
            processed_image = process_erosion_with_rect_kernel(img, kernel_size, iteration)
        elif kernel_type == 1:
            processed_image = process_erosion_with_ellipse_kernel(img, kernel_size, iteration)
        elif kernel_type == 2:
            processed_image = process_erosion_with_cross_kernel(img, kernel_size, iteration)
        else:
            return raise_invalid_kernel_type(kernel_type)
        return processed_image

    def apply_dilation_to_image(self, img, kernel_size, kernel_type=0, iteration=1):
        """
        Purpose:
            Applies the dilation morphological transformation to a binary image.
        Args:
            img - processed binary image.
            kernel_size - size of the kernel
            kernel_type - shape of kernel used. 0 = rectangle, 1 = ellipse, and 2 = cross.
            iteration - number of iterations to perform on image.
        Returns:
            Image with dilation morphological transformation applied.
        """
        verify_valid_kernel_size(kernel_size)
        verify_valid_iteration(iteration)
        if kernel_type == 0:
            processed_image = process_dilation_with_rect_kernel(img, kernel_size, iteration)
        elif kernel_type == 1:
            processed_image = process_dilation_with_ellipse_kernel(img, kernel_size, iteration)
        elif kernel_type == 2:
            processed_image = process_dilation_with_cross_kernel(img, kernel_size, iteration)
        else:
            return raise_invalid_kernel_type(kernel_type)
        return processed_image

    def apply_opening_to_image(self, img, kernel_size, kernel_type=0, iteration=1):
        """
        Purpose:
            Applies the opening morphological transformation to a binary image.
        Args:
            img - processed binary image.
            kernel_size - size of the kernel
            kernel_type - shape of kernel used. 0 = rectangle, 1 = ellipse, and 2 = cross.
            iteration - number of iterations to perform on image.
        Returns:
            Image with opening morphological transformation applied.
        """
        verify_valid_kernel_size(kernel_size)
        verify_valid_iteration(iteration)
        if kernel_type == 0:
            processed_image = process_opening_with_rect_kernel(img, kernel_size)
        elif kernel_type == 1:
            processed_image = process_opening_with_ellipse_kernel(img, kernel_size)
        elif kernel_type == 2:
            processed_image = process_opening_with_cross_kernel(img, kernel_size)
        else:
            return raise_invalid_kernel_type(kernel_type)
        return processed_image

    def apply_closing_to_image(self, img, kernel_size, kernel_type=0, iteration=1):
        """
        Purpose:
            Applies the closing morphological transformation to a binary image.
        Args:
            img - processed binary image.
            kernel_size - size of the kernel
            kernel_type - shape of kernel used. 0 = rectangle, 1 = ellipse, and 2 = cross.
            iteration - number of iterations to perform on image.
        Returns:
            Image with closing morphological transformation applied.
        """
        verify_valid_kernel_size(kernel_size)
        verify_valid_iteration(iteration)
        if kernel_type == 0:
            processed_image = process_closing_with_rect_kernel(img, kernel_size)
        elif kernel_type == 1:
            processed_image = process_closing_with_ellipse_kernel(img, kernel_size)
        elif kernel_type == 2:
            processed_image = process_closing_with_cross_kernel(img, kernel_size)
        else:
            return raise_invalid_kernel_type(kernel_type)
        return processed_image

    def apply_gradient_to_image(self, img, kernel_size, kernel_type=0, iteration=1):
        """
        Purpose:
            Applies the gradient morphological transformation to a binary image.
        Args:
            img - processed binary image.
            kernel_size - size of the kernel
            kernel_type - shape of kernel used. 0 = rectangle, 1 = ellipse, and 2 = cross.
            iteration - number of iterations to perform on image.
        Returns:
            Image with gradien morphological transformation applied.
        """
        verify_valid_kernel_size(kernel_size)
        verify_valid_iteration(iteration)
        if kernel_type == 0:
            processed_image = process_gradient_with_rect_kernel(img, kernel_size)
        elif kernel_type == 1:
            processed_image = process_gradient_with_ellipse_kernel(img, kernel_size)
        elif kernel_type == 2:
            processed_image = process_gradient_with_cross_kernel(img, kernel_size)
        else:
            return raise_invalid_kernel_type(kernel_type)
        return processed_image

    def apply_top_hat_to_image(self, img, kernel_size, kernel_type=0, iteration=1):
        """
        Purpose:
            Applies the top hat morphological transformation to a binary image.
        Args:
            img - processed binary image.
            kernel_size - size of the kernel
            kernel_type - shape of kernel used. 0 = rectangle, 1 = ellipse, and 2 = cross.
            iteration - number of iterations to perform on image.
        Returns:
            Image with top hat morphological transformation applied.
        """
        verify_valid_kernel_size(kernel_size)
        verify_valid_iteration(iteration)
        if kernel_type == 0:
            processed_image = process_tophat_with_rect_kernel(img, kernel_size)
        elif kernel_type == 1:
            processed_image = process_tophat_with_ellipse_kernel(img, kernel_size)
        elif kernel_type == 2:
            processed_image = process_tophat_with_cross_kernel(img, kernel_size)
        else:
            return raise_invalid_kernel_type(kernel_type)
        return processed_image

    def apply_black_hat_to_image(self, img, kernel_size, kernel_type=0, iteration=1):
        """
        Purpose:
            Applies the black hat morphological transformation to a binary image.
        Args:
            img - processed binary image.
            kernel_size - size of the kernel
            kernel_type - shape of kernel used. 0 = rectangle, 1 = ellipse, and 2 = cross.
            iteration - number of iterations to perform on image.
        Returns:
            Image with black hat morphological transformation applied.
        """
        verify_valid_kernel_size(kernel_size)
        verify_valid_iteration(iteration)
        if kernel_type == 0:
            processed_image = process_blackhat_with_rect_kernel(img, kernel_size)
        elif kernel_type == 1:
            processed_image = process_blackhat_with_ellipse_kernel(img, kernel_size)
        elif kernel_type == 2:
            processed_image = process_blackhat_with_cross_kernel(img, kernel_size)
        else:
            raise_invalid_kernel_type(kernel_type)
        return processed_image
