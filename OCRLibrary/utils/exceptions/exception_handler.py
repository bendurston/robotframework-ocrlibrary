import numpy

from OCRLibrary.utils.exceptions.exceptions import *

def verify_content(expected_content, actual_content):
    if expected_content not in actual_content:
        raise ContentNotFound(f"The expected content: {expected_content}\nwas not found in the actual content: {actual_content}")

def verify_valid_kernel_size(kernel_size):
    # Kernel size must be 0, or an odd positive number
    if ((kernel_size == 0 or (kernel_size % 2 == 1)) and kernel_size >= 0):
        return
    else:
        raise InvalidKernelSize("The kernel size argument provided is invalid. Please provide a size that is either 0 or a positive odd number.")

def raise_invalid_kernel_type(kernel_type):
    raise InvalidKernelType(f"The provided kernel type: {kernel_type} is invalid. Please provide a type that is either 0, 1 or 2.")

def verify_valid_iteration(iteration):
    if type(iteration) is not int:
        raise InvalidIteration(f"The provided iteration: {iteration} is invalid. Iteration must be an integer.")
    if iteration < 1:
        raise InvalidIteration(f"The provided iteration: {iteration} is invalid. Please select and integer that is greater than or equal to 1.")

def verify_valid_image(processed_image):
    if isinstance(processed_img, numpy.ndarray):
        pass
    else:
        raise InvalidImageArgument("The image argument provided is invalid. Please give an image that has been returned from any of the image processing keywords.")

