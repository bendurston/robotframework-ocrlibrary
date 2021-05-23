"""
colourImageProcessing module.
"""
from ..utils.exceptions.exception_handler import \
    (verify_valid_image, verify_valid_colour_bounds)
from ..utils.helpers.robot_conversions import \
    (convert_to_valid_colour_bounds)
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

    def mask_colour(self, processed_img, lower_bound_colour, upper_bound_colour):
        """
        Mask all colours in an image that are not within the provided bounds. Masked colours become black.

        Example of masking all colours but red in a BGR image:
        | ${img_path}=     Capture Page Screenshot
        | ${processed_img}=    Read Image   ${img_path}
        | ${lower}=   Create List     0   0   200
        | ${upper}=   Create List     0   0   255
        | ${masked_img}=      Mask Colour     ${processed_img}    ${lower}    ${upper}

        See `introduction` for details about using the arguments.
        """
        verify_valid_image(processed_img)
        colours = convert_to_valid_colour_bounds(lower_bound_colour, upper_bound_colour)
        lower_bound_colour = colours[0]
        upper_bound_colour = colours[1]
        verify_valid_colour_bounds(lower_bound_colour, upper_bound_colour)
        return mask_colour_bgr_or_hsv(processed_img, lower_bound_colour, upper_bound_colour)

    def mask_colours(self, processed_img, lower_bound_colour1, upper_bound_colour1, lower_bound_colour2, upper_bound_colour2):
        """
        Mask all colours in an image that are not within the two provided bounds. Masked colours become black.

        Example of masking all colours but red and blue in a BGR image:
        | ${img_path}=     Capture Page Screenshot
        | ${processed_img}=    Read Image   ${img_path}
        | ${lower1}=   Create List     0   0   200
        | ${upper1}=   Create List     0   0   255
        | ${lower2}=   Create List     0   200  0
        | ${upper2}=   Create List     0   255  0
        | ${masked_img}=    Mask Colours    ${processed_img}    ${lower1}    ${upper1}    ${lower2}    ${upper2}

        See `introduction` for details about using the arguments.
        """
        colours = convert_to_valid_colour_bounds(lower_bound_colour1, upper_bound_colour1, lower_bound_colour2, upper_bound_colour2)
        lower_bound_colour1 = colours[0]
        upper_bound_colour1 = colours[1]
        lower_bound_colour2 = colours[2]
        upper_bound_colour2 = colours[3]
        verify_valid_image(processed_img)
        verify_valid_colour_bounds(lower_bound_colour1, upper_bound_colour1, lower_bound_colour2, upper_bound_colour2)
        return mask_colours_bgr_or_hsv(processed_img, lower_bound_colour1, upper_bound_colour1, lower_bound_colour2, upper_bound_colour2)
