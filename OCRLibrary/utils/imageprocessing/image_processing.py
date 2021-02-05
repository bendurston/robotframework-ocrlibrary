"""
High level implementations of functions within image transformation/
"""
from imagetransformation.changing_colourspaces import .
from imagetransformation.image_blurring import .
from imagetransformation.image_thresholding import .
from imagetransformation.morphological_transformations import .

def process_to_binary_image(img, inverse, threshold=127, max_threshold=255):
    """
    Purpose:
         Process an image to binary colours.
    Args:
        img - a read image (result of imread())
        threshold - threshold value used to classify the pixel values (optional).
        max_threshold - the max value to be given if a pixels value is more than the threshold value (optional).
    Returns:
        A binary image.
    """
    gray_img = convert_bgr_to_gray(img)
    if inverse:
        binary_image = thresholding_binary_inv(gray_img, threshold, max_threshold)
    else:
        binary_image = thresholding_binary(gray_img, threshold, max_threshold)
    return binary_image
