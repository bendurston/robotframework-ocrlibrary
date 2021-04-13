"""
Structuring element module.
"""
import cv2

def get_rect_kernel(kernel_size):
    """
    Purpose:
        Gets a rectangular shaped kernel
    Args:
        kernel_size - tuple: size of the kernel.
    Returns:
        2D array representing a rectangular kernel.
    """
    return cv2.getStructuringElement(cv2.MORPH_RECT, kernel_size)

def get_ellipse_kernel(kernel_size):
    """
    Purpose:
        Gets a ellipse shaped kernel
    Args:
        kernel_size - tuple: size of the kernel.
    Returns:
        2D array representing an ellipse kernel.
    """
    return cv2.getStructuringElement(cv2.MORPH_ELLIPSE, kernel_size)

def get_cross_kernel(kernel_size):
    """
    Purpose:
        Gets a rectangular shaped kernel
    Args:
        kernel_size - tuple: size of the kernel.
    Returns:
        2D array representing a rectangular kernel.
    """
    return cv2.getStructuringElement(cv2.MORPH_CROSS, kernel_size)
