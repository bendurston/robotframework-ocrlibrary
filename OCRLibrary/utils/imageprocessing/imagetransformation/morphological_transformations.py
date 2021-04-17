"""
Morphological transformations module.
"""
import cv2

def morph_erosion(img, kernel, iteration=1):
    """
    Erodes the boundarios of foreground objects.
    """
    return cv2.erode(img, kernel, iterations=iteration)

def morph_dilation(img, kernel, iteration=1):
    """
    Opposite of erosion. A pixel becomes a '1' if at least one pixel under the kernel is '1'.
    """
    return cv2.dilate(img, kernel, iterations=iteration)

def morph_opening(img, kernel, iteration=1):
    """
    Useful in removing noise. Like erosion then dilation.
    """
    return cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel, iterations=iteration)

def morph_closing(img, kernel, iteration=1):
    """
    Opposite to opening.
    """
    return cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel, iterations=iteration)

def morph_gradient(img, kernel, iteration=1):
    """
    Will give the object an outline.
    """
    return cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel, iterations=iteration)

def morph_top_hat(img, kernel, iteration=1):
    """
    Will give the difference between input image and opening image.
    """
    return cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel, iterations=iteration)

def morph_black_hat(img, kernel, iteration=1):
    """
    Will give the difference between tthe closing of the input image and the input image.
    """
    return cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel, iterations=iteration)
