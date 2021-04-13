"""
Exception handler module.
"""
import numpy
from OCRLibrary.utils.exceptions.exceptions \
    import (InvalidKernelSize, InvalidKernelType, InvalidIteration, ContentNotFound, InvalidImageArgument)

def verify_content(expected_content, actual_content):
    """
    Function verifies if the expected content is in the actual content. If it is, True is returned
    otherwise a ContentNotFound error is raised.
    """
    if expected_content not in actual_content:
        raise ContentNotFound(f"The expected content: {expected_content}\nwas not found in the actual content: {actual_content}")
    return True

def verify_valid_kernel_size(kernel_size):
    """
    Function verifies if the given kernel size is valid.
    Kernel size must be 0, or an odd positive number
    """
    if ((kernel_size == 0 or (kernel_size % 2 == 1)) and kernel_size >= 0):
        return True
    raise InvalidKernelSize("The kernel size argument provided is invalid. Please provide a size that is either 0 or a positive odd number.")

def raise_invalid_kernel_type(kernel_type):
    """
    Function raises an InvalidKernelType Error when called.
    """
    raise InvalidKernelType(f"The provided kernel type: {kernel_type} is invalid. Please provide a type that is either 0, 1 or 2.")

def verify_valid_iteration(iteration):
    """
    Function verifies if the iteration is valid.
    Must be an int greater than 0.
    """
    if isinstance(iteration, int):
        if iteration <= 0:
            raise InvalidIteration(f"The provided iteration: {iteration} is invalid. Please select and integer that is greater than or equal to 1.")
        return True
    raise InvalidIteration(f"The provided iteration: {iteration} is invalid. Iteration must be an integer.")

def verify_valid_image(processed_img):
    """
    Function verifies if the given image is valid.
    That is an image that has been processed by opencv (is of type numpy.ndarray).
    """
    if isinstance(processed_img, numpy.ndarray):
        return True
    else:
        raise InvalidImageArgument("The image argument provided is invalid. Please give an image that has \
            been returned from any of the image processing keywords.")
