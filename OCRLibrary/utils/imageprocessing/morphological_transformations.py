import cv2

"""
Reference:  
    https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_morphological_ops/py_morphological_ops.html#morphological-ops

Notes:
    Morphological transformations: results are best with binary images, specifically white foreground and black background. convert_BGR_to_GRAY() -> threshold_binary_inv()
    In noise removal erosion is followed by dilation. Erosion removes white noises but shrinks the object. So dilation is performed.
"""

def morph_erosion(img, kernel, iteration=1):
    """
    Erodes the boundarios of foreground objects.
    """
    return cv2.erode(img, kernel, iterations= iteration)

def morph_dilation(img, kernel, iteration=1):
    """
    Opposite of erosion. A pixel becomes a '1' if at least one pixel under the kernel is '1'.
    """
    return cv2.dialte(img, kernel, iterations= iteration)

def morph_opening(img, kernel):
    """
    Useful in removing noise. Like erosion then dilation.
    """
    return cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)

def morph_closing(img, kernel):
    """
    Opposite to opening.
    """
    return cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)

def morp_gradient(img, kernel):
    """
    Will give the object an outline. 
    """
    return cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)

def morph_top_hat(img, kernel):
    """
    """
    return cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)

def morph_black_hat(img, kernel):
    """
    """
    return cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)

"""
Structuring Element
"""
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
