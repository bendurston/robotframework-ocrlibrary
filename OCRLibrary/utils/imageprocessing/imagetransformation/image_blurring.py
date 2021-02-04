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
    """
    return cv2.blur(img, kernel)

def blurring_gaussian(img, kernel, other):
    """
    """
    
    return cv2.GaussianBlur(img, kernel, other)

# TODO median filtering

# TODO bilateral filtering

# TODO Image filtering cv2.filter2D()