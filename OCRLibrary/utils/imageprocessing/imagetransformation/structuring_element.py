"""
Structuring Element
"""
from exceptions.kernel_size_exceptions import InvalidKernelSize

def get_rect_kernel(kernel_size):
    """
    Purpose:
        Gets a rectangular shaped kernel
    Args:
        kernel_size - tuple: size of the kernel.
    Returns:
        2D array representing a rectangular kernel.
    """
    verify_valid_kernel_size(kernel_size)
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
    verify_valid_kernel_size(kernel_size)
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
    verify_valid_kernel_size(kernel_size)
    return cv2.getStructuringElement(cv2.MORPH_CROSS, kernel_size)

def verify_valid_kernel_size(kernel_size):
    # Kernel size must be 0, or an odd positive number
    if ((kernel_size == 0 or (kernel_size % 2 == 1)) and kernel_size >= 0):
        return
    else:
        raise InvalidKernelSize("The provided kernel size is invalid. Please provide a size that is either 0 or a positive odd number.")

