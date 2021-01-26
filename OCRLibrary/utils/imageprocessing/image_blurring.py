import cv2

"""
Reference:  
    https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_filtering/py_filtering.html#filtering
"""
def blurring_averaging(img, kernel):
    """
    """
    return cv2.blur(img, kernel)

def blurring_gaussian(img, kernel, other):
    """
    """
    return cv2.GaussianBlur(img, kernel, other)

# TODO median filtering

# TODO bilateral filtering

# TODO Image filtering cv2.filter2D()