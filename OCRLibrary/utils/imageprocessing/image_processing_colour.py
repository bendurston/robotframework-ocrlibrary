"""
Image processing colour module.
"""
from OCRLibrary.utils.imageprocessing.imagetransformation.changing_colourspaces \
    import (convert_bgr_to_hsv, mask_single_colour, mask_double_colour)

def process_colour_image_to_hsv(img):
    """
    Purpose:
        Converts image from BGR to HSV.
    Args:
        img - provided read image (result of cv2.imread()).
    Returns:
        Image in HSV.
    """
    return convert_bgr_to_hsv(img)

def mask_colour_bgr_or_hsv(processed_image, lower_bound_colour, upper_bound_colour):
    """
    Purpose:
        Maskes any colour that is not in the range of the bounds of the provided colour.
    Args:
        processed_img - provided read image (result of cv2.imread()).
        lower_bound_colour - the lower bound of the colour to not mask in BGR format.
        upper_bound_colour - the upper bound of the colour to not mask in BGR format.
    Returns:
        result - image with colours masked.
    """
    return mask_single_colour(processed_image, lower_bound_colour, upper_bound_colour)

def mask_colours_bgr_or_hsv(processed_image, lower_bound_colour1, upper_bound_colour1, lower_bound_colour2, upper_bound_colour2):
    """
    Purpose:
        Maskes any colour that is not in the range of the bounds of the two provided colours.
    Args:
        img - provided read image (result of cv2.imread()).
        lower_bound_colour1 - the lower bound of the first colour to not mask in BGR format.
        upper_bound_colour1 - the upper bound of the first colour to not mask in BGR format.
        lower_bound_colour2 - the lower bound of the second colour to not mask in BGR format.
        upper_bound_colour2 - the upper bound of the second colour to not mask in BGR format.
    Returns:
        result - image with colours masked.
    """
    return mask_double_colour(processed_image, lower_bound_colour1, upper_bound_colour1, lower_bound_colour2, upper_bound_colour2)
