"""
Exception handler module.
"""
import numpy
import cv2
from OCRLibrary.utils.exceptions.exceptions \
    import (InvalidKernelSize, InvalidKernelType, InvalidIteration, ContentNotFound, InvalidImageArgument,
    InvalidColourBoundArguments, InvalidImagePath, InvalidThresholdValue, InvalidDepthArgument)

def verify_content(expected_content, actual_content):
    """
    Function verifies if the expected content is in the actual content. If it is, True is returned
    otherwise a ContentNotFound error is raised.
    """
    if expected_content not in actual_content:
        raise ContentNotFound(f"The expected content: {expected_content} was not found in the actual content: {actual_content}")
    return True

def verify_valid_kernel_size(kernel_size):
    """
    Function verifies if the given kernel size is valid.
    Kernel size must be a tuple/list of ints with positive values.
    """
    if isinstance(kernel_size, (tuple, list)):
        if (int(float(kernel_size[0])) > 0 and int(float(kernel_size[1])) > 0):
            if (int(float(kernel_size[0])) and int(float(kernel_size[1]))):
                return True
    raise InvalidKernelSize("The kernel size argument provided is invalid. Please provide a size that is a positive number of type int, and the kernel_size is of type tuple or list.")

def verify_valid_kernel_size_only_odds(kernel_size):
    """
    Function verifies if the given kernel size is valid.
    Kernel size must be a tuple/list of ints with positive odd values.
    """
    if isinstance(kernel_size, (tuple, list)):
        if (int(float(kernel_size[0])) > 0 and int(float(kernel_size[1])) > 0):
            if (int(float(kernel_size[0])) % 2 == 1 and int(float(kernel_size[1])) % 2 == 1):
                return True
    raise InvalidKernelSize("The kernel size argument provided is invalid. Please provide a size that is a positive odd number of type int, and the kernel_size is of type tuple or list.")

def verify_valid_kernel_size_non_tuple(kernel_size):
    """
    Function verifies if the given kernel size is valid.
    Kernel size must be a an int that is greater than zero and is odd.
    """
    if isinstance(kernel_size, (int, str, float)):
        if (int(kernel_size) > 0 and int(kernel_size) % 2 == 1):
            return True
    raise InvalidKernelSize(f"The kernel size argument provided is invalid. Please provide a size that is a positive odd number of type int. {type(kernel_size)}")

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
    raise InvalidImageArgument("The image argument provided is invalid. Please give an image that has \
        been returned from any of the image processing keywords.")

def verify_valid_colour_bounds(*arg):
    """
    Function verifies if the given bgr or hsv bounds are valid.
    BGR/HSV values range from 0 to 255. This condition must be met.
    """
    args_num = len(arg)
    for i in range(0, args_num):
        if ((isinstance(arg[i][0], int)) and (isinstance(arg[i][1], int)) and (isinstance(arg[i][2], int))):
            if ((arg[i][0] < 0 or arg[i][0] > 255) or (arg[i][1] < 0 or arg[i][1] > 255) or (arg[i][2] < 0 or arg[i][2] > 255)):
                raise InvalidColourBoundArguments("The bound(s) provided are invalid. Please give values that are ints between 0 and 255.")
        else:
            raise InvalidColourBoundArguments("The bound(s) provided are invalid. Please provide an int between 0 and 255.")
    return True

def verify_valid_image_path(filename, read=True):
    """
    Function verifies if the given image can be encoded/decoded by OpenCV.
    If read is true, function checks if image can be decoded (imread()) Otherwise the
    function checks if the image can be encoded (imwrite()).
    """
    if read:
        if cv2.haveImageReader(filename):
            return True
        raise InvalidImagePath("The image path provided is invalid. Please insure the path is correct \
            or the file format is supported.")
    if cv2.haveImageWriter(filename):
        return True
    raise InvalidImagePath("The provided filename cannot be encoded by OpenCV. Please \
        insure your desired file format is supported.")

def verify_valid_threshold_values(threshold, max_threshold):
    """
    Function verifies if the given threshold values are valid. Threshold values must be an int or a float.
    """
    if (isinstance(threshold, (int, float)) and isinstance(max_threshold, (int, float))):
        return True
    raise InvalidThresholdValue(f"Either threshold value {threshold} or {max_threshold} are invalid.\
         Please insure the thresholds are either of type int or float.")

def verify_valid_depth(depth):
    """
    Function verifies if the given depth if valid. Must be a negative int.
    """
    if (isinstance(depth, (int, str, float)) and int(depth) < 0):
        return True
    raise InvalidDepthArgument("The depth value provided is invalid. Please provide a negative integer.")
