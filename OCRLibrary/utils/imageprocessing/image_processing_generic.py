"""
High level functions to apply image processing to any photo (i.e. colour or gray/binary).
"""
from OCRLibrary.utils.imageprocessing.imagetransformation.structuring_element \
    import get_rect_kernel, get_ellipse_kernel, get_cross_kernel
from OCRLibrary.utils.imageprocessing.imagetransformation.image_blurring \
    import image_filtering, blurring_averaging, blurring_gaussian, median_filtering

def process_image_filtering_with_rect_kernel(img, kernel_size, depth):
    """
    Purpose:
        Apply 2D image filter with a rectange kernel to an image.
    Args:
        img - the processed image.
        kernel_size - size of the kernel.
        depth - desired depth of the destination image.
    Returns:
        The filtered image.
    """
    kernel = get_rect_kernel(kernel_size)
    return image_filtering(img, depth, kernel)

def process_image_filtering_with_ellipse_kernel(img, kernel_size, depth):
    """
    Purpose:
        Apply 2D image filter with an ellipse kernel to an image.
    Args:
        img - the processed image.
        kernel_size - size of the kernel.
        depth - desired depth of the destination image.
    Returns:
        The filtered image.
    """
    kernel = get_ellipse_kernel(kernel_size)
    return image_filtering(img, depth, kernel)

def process_image_filtering_with_cross_kernel(img, kernel_size, depth):
    """
    Purpose:
        Apply 2D image filter with a cross kernel to an image.
    Args:
        img - the processed image.
        kernel_size - size of the kernel.
        depth - desired depth of the destination image.
    Returns:
        The filtered image.
    """
    kernel = get_cross_kernel(kernel_size)
    return image_filtering(img, depth, kernel)

def process_median_filtering(img, kernel_size):
    """
    Purpose:
        Apply median image filter to an image.
    Args:
        img - the processed image.
        kernel_size - size of the kernel.
    Returns:
        The filtered image.
    """
    return median_filtering(img, kernel_size)

def process_blurring_averaging_with_rect_kernel(img, kernel_size):
    """
    Purpose:
        Apply blurring averaging filter with a rectangle kernel to an image.
    Args:
        img - the processed image.
        kernel_size - size of the kernel.
    Returns:
        The filtered image.
    """
    kernel = get_rect_kernel(kernel_size)
    return blurring_averaging(img, kernel)

def process_blurring_averaging_with_ellipse_kernel(img, kernel_size):
    """
    Purpose:
        Apply blurring averaging filter with an ellispe kernel to an image.
    Args:
        img - the processed image.
        kernel_size - size of the kernel.
    Returns:
        The filtered image.
    """
    kernel = get_ellipse_kernel(kernel_size)
    return blurring_averaging(img, kernel) 

def process_blurring_averaging_with_cross_kernel(img, kernel_size):
    """
    Purpose:
        Apply blurring averaging filter with a cross kernel to an image.
    Args:
        img - the processed image.
        kernel_size - size of the kernel.
    Returns:
        The filtered image.
    """
    kernel = get_cross_kernel(kernel_size)
    return blurring_averaging(img, kernel)

def process_blurring_gaussian_with_rect_kernel(img, kernel_size):
    """
    Purpose:
        Apply blurring gaussian filter with a rectangle kernel to an image.
    Args:
        img - the processed image.
        kernel_size - size of the kernel.
    Returns:
        The filtered image.
    """
    kernel = get_rect_kernel(kernel_size)
    return blurring_gaussian(img, kernel)

def process_blurring_gaussian_with_ellipse_kernel(img, kernel_size):
    """
    Purpose:
        Apply blurring gaussian filter with an ellipse kernel to an image.
    Args:
        img - the processed image.
        kernel_size - size of the kernel.
    Returns:
        The filtered image.
    """
    kernel = get_ellipse_kernel(kernel_size)
    return blurring_gaussian(img, kernel)

def process_blurring_gaussian_with_cross_kernel(img, kernel_size):
    """
    Purpose:
        Apply blurring gaussian filter with a cross kernel to an image.
    Args:
        img - the processed image.
        kernel_size - size of the kernel.
    Returns:
        The filtered image.
    """
    kernel = get_cross_kernel(kernel_size)
    return blurring_gaussian(img, kernel)
