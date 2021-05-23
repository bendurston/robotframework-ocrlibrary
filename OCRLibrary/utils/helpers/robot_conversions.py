"""
Robot conversions module.
"""

def convert_to_valid_kernel_size(size):
    """
    Purpose:
        Converts a list/tuple given in robot to a tuple of ints.
    Args:
        size - list/tuple of strings, length 2.
    Returns
        kernel_size - A tuple of ints.
    """
    kernel_size = (int(float(size[0])), int(float(size[1])))
    return kernel_size
