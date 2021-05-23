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

def convert_to_valid_int(value):
    """
    Purpose:
        Converts a string to an int.
    Args:
        value - string/float
    Returns:
        value - of type int.
    """
    return int(float(value))

def convert_to_valid_colour_bounds(*arg):
    """
    Purpose:
        Converts a colour bound of strings/floats to a bound of ints
    Args:
        *arg - list of bounds passed into the function
    Returns:
        colours - a list of the updated bounds.
    """
    args_num = len(arg)
    colours = []
    for i in range(0, args_num):
        colours.append((int(float(arg[i][0])), int(float(arg[i][1])), int(float(arg[i][2]))))
    return colours
