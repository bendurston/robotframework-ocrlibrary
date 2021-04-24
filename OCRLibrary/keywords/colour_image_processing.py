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
        Converts any image read as bgr into hsv colour scheme.

        Example:
        | ${img_path}=     Capture Page Screenshot
        | ${processed_img}=    Read Image   ${img_path}
        | ${hsv_img}=     Convert Image To HSV    ${processed_img}
        """
        verify_valid_image(processed_img)
        return process_colour_image_to_hsv(processed_img)

    def mask_colour(self, processed_img, lower_bound_colour, upper_bound_colour, colour_type=0):
        """
        Mask all colours in an image that are not within the provided bounds. Masked colours become black.

        Example of masking all colours but red in a BGR image:
        | ${img_path}=     Capture Page Screenshot
        | ${processed_img}=    Read Image   ${img_path}
        | ${masked_img}=    Mask Colour    ${processed_img}    (0, 0, 200)    (0, 0, 255)    0

        See `introduction` for details about using the arguments.
        """
        verify_valid_image(processed_img)
        if colour_type == 0:
            verify_valid_bgr_bounds(lower_bound_colour, upper_bound_colour)
        elif colour_type == 1:
            verify_valid_hsv_bounds(lower_bound_colour, upper_bound_colour)
        return mask_colour_bgr_or_hsv(processed_img, lower_bound_colour, upper_bound_colour)

    def mask_colours(self, processed_img, lower_bound_colour1, upper_bound_colour1, lower_bound_colour2, upper_bound_colour2, colour_type=0):
        """
        Mask all colours in an image that are not within the two provided bounds. Masked colours become black.

        Example of masking all colours but red and blue in a BGR image:
        | ${img_path}=     Capture Page Screenshot
        | ${processed_img}=    Read Image   ${img_path}
        | ${masked_img}=    Mask Colours    ${processed_img}    (0, 0, 200)    (0, 0, 255)    (200, 0, 0)    (255, 0, 0)    0

        See `introduction` for details about using the arguments.
        """
        verify_valid_image(processed_img)
        if colour_type == 0:
            verify_valid_bgr_bounds(lower_bound_colour1, upper_bound_colour1, lower_bound_colour2, upper_bound_colour2)
        elif colour_type == 1:
            verify_valid_hsv_bounds(lower_bound_colour1, upper_bound_colour1, lower_bound_colour2, upper_bound_colour2)
        return mask_colours_bgr_or_hsv(processed_img, lower_bound_colour1, upper_bound_colour1, lower_bound_colour2, upper_bound_colour2)
