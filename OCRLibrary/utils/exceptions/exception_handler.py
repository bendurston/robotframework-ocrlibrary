import numpy

from exceptions import *

def verify_content(expected_content, actual_content):
    if expected_content not in actual_content:
        raise ContentNotFound(f"The expected content: {expected_content}\nwas not found in the actual content: {actual_content}")

def verify_valid_kernel_size(kernel_size):
    # Kernel size must be 0, or an odd positive number
    if ((kernel_size == 0 or (kernel_size % 2 == 1)) and kernel_size >= 0):
        return
    else:
        raise InvalidKernelSize("The kernel size argument provided is invalid. Please provide a size that is either 0 or a positive odd number.")

def verify_valid_image(processed_image):
    if isinstance(processed_img, numpy.ndarray):
        continue
    else:
        raise InvalidImageArgument("The image argument provided is invalid. Please give an image that has been returned from any of the image processing keywords.")

