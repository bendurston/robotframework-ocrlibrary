"""
Image blurring module.
"""
import cv2

def image_filtering(img, depth, kernel):
    """
    Purpose:
        Removes noise if filtered with a low-pass filter. Finds edges if filtered with a high-pass filter.
    Args:
        img - provided read image (result of cv2.imread()).
        depth - desired depth of the destination image.
        kernel - correlation kernel.
    Returns:
        The filtered image.
    """
    return cv2.filter2D(img, depth, kernel)

def blurring_averaging(img, kernel):
    """
    Purpose:
        Apply average filtering to image. Takes average of pixels under kernel and 
        replaces the central element with the average.
    Args:
        img - provided read image (result of cv2.imread()).
        kernel - correlation kernel.
    Returns:
        The filtered image.
    """
    return cv2.blur(img, kernel)

def blurring_gaussian(img, kernel):
    """
    Purpose:
        Apply gaussian blurring to image.
        Border type is set to a constant 0.
    Args:
        img - provided read image (result of cv2.imread()).
        kernel - correlation kernel.
    Returns:
        The filtered image.
    """
    return cv2.GaussianBlur(img, kernel, 0)

def median_filtering(img, kernel_size):
    """
    Purpose:
        Apply a filter based off the median of all the pizels under the kernel window.
    Args:
        img - the image to apply the filter to.
        kernel_size - the size of the kernel
    Returns:
        The filtered image.
    """
    return cv2.medianBlur(img, kernel_size)
