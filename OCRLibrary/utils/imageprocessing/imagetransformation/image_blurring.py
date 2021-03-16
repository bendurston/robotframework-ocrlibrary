import cv2

"""
Reference:  
    https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_filtering/py_filtering.html#filtering
"""
def image_filtering(img, depth, kernel):
    """
    Purpose:
        Removes noise if filtered with a low-pass filter. Finds edges if filtered with a high-pass filter.
    Args:
        img - provided read image (result of cv2.imread())
        depth - 
        kernel - 
    """
    return cv2.filter2D(img, depth, kernel)

def blurring_averaging(img, kernel):
    """
    Purpose:
    #TODO
    """
    return cv2.blur(img, kernel)

def blurring_gaussian(img, kernel, other):
    """
    #TODO
    """
    
    return cv2.GaussianBlur(img, kernel, other)

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
    # TODO if kernel_size is not 0, positive or odd, throw an error, else return
    return cv2.medianBlur(img, kernel_size)

