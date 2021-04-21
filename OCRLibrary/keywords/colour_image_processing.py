"""
colourImageProcessing module.
"""
from ..utils.exceptions.exception_handler import \
    (verify_valid_image, verify_valid_bgr_bounds, verify_valid_hsv_bounds)
from ..utils.imageprocessing.image_processing_colour import \
    (process_colour_image_to_hsv, mask_colour_bgr_or_hsv, mask_colours_bgr_or_hsv)

class ColourImageProcessingKeywords:
    """
    ColourImageProcessingKeywords Class
    """
    def convert_image_to_HSV(self, processed_img):
        """
        Purpose:
            Converts any image read as bgr into hsv colour scheme.
        Args:
            processed_img - the processed image in bgr.
        """
        verify_valid_image(processed_img)
        return process_colour_image_to_hsv(processed_img)

    def mask_colour(self, processed_img, lower_bound_colour, upper_bound_colour, colour_type=0):
        """
        Purpose:
            Mask any colour in an image that is not within the provided bound (exclude one colour bound). Note if the image is BGR the bounds
            must be ints 0 to 255. If the image is HSV the bounds must be a 3 element tuple containing ints 0 to 255.
            Note - Bounds can be of type tuple or list e.g - (blue, green, red), (hue, saturation, value) or [blue, green, red], [hue, saturation, value].
        Args:
            processed_img - the processed image.
            lower_bound_colour - the lower bound of the colour to exclude from the mask.
            upper_bound_colour - the upper bound of the colour to exclude from the mask.
            colour_type - 0 if the processed image is in BGR, 1 if the processed image is in HSV.
        Returns:
            The image with the colours masked.
        """
        verify_valid_image(processed_img)
        if colour_type == 0:
            verify_valid_bgr_bounds(lower_bound_colour, upper_bound_colour)
        elif colour_type == 1:
            verify_valid_hsv_bounds(lower_bound_colour, upper_bound_colour)
        return mask_colour_bgr_or_hsv(processed_img, lower_bound_colour, upper_bound_colour)

    def mask_colours(self, processed_img, lower_bound_colour1, upper_bound_colour1, lower_bound_colour2, upper_bound_colour2, colour_type=0):
        """
        Purpose:
            Mask any colour in an image that is not within the provided bounds (exclude two colour bounds). Note if the image is BGR the bounds
            must be ints 0 to 255. If the image is HSV the bounds must be a 3 element tuple containing ints 0 to 255.
            Note - Bounds can be of type tuple or list e.g - (blue, green, red), (hue, saturation, value) or 
            [blue, green, red], [hue, saturation, value].
        Args:
            processed_img - the processed image.
            lower_bound_colour1 - the lower bound of the first colour to exclude from the mask.
            upper_bound_colour1 - the upper bound of the first colour to exclude from the mask.
            lower_bound_colour2 - the lower bound of the second colour to exclude from the mask.
            upper_bound_colour2 - the upper bound of the second colour to exclude from the mask.
            colour_type - 0 if the processed image is in BGR, 1 if the processed image is in HSV.
        Returns:
            The image with the colours masked.
        """
        verify_valid_image(processed_img)
        if colour_type == 0:
            verify_valid_bgr_bounds(lower_bound_colour1, upper_bound_colour1, lower_bound_colour2, upper_bound_colour2)
        elif colour_type == 1:
            verify_valid_hsv_bounds(lower_bound_colour1, upper_bound_colour1, lower_bound_colour2, upper_bound_colour2)
        return mask_colours_bgr_or_hsv(processed_img, lower_bound_colour1, upper_bound_colour1, lower_bound_colour2, upper_bound_colour2)
