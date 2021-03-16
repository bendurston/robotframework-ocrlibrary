"""
High level functions to apply image processing to any photo (i.e. colour or gray/binary).
"""
import cv2
from imagetransformation.structuring_element import .
from imagetransformation.image_blurring import .

### Image blurring 
def process_image_filtering_with_rect_kernel(img, kernel_size, depth):
    pass

def process_image_filtering_with_ellipse_kernel(img, kernel_size, depth):
    pass

def process_image_filtering_with_cross_kernel(img, kernel_size, depth):
    pass

def process_median_filtering(img, kernel_size):
    pass

def process_blurring_averaging_with_rect_kernel(img, kernel_size):
    pass

def process_blurring_averaging_with_ellipse_kernel(img, kernel_size):
    pass

def process_blurring_averaging_with_cross_kernel(img, kernel_size):
    pass

def process_blurring_gaussian_with_rect_kernel(img, kernel_size):
    pass

def process_blurring_gaussian_with_ellipse_kernel(img, kernel_size):
    pass

def process_blurring_gaussian_with_cross_kernel(img, kernel_size):
    pass

