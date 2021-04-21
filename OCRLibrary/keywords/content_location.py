"""
content_location module.
"""
from ..utils.exceptions.exception_handler \
    import (verify_valid_image)
from ..utils.imagereading.text_locating \
    import (return_text_coordinates, return_multiple_text_coordinates,
    return_text_bounds, return_multiple_text_bounds)

class ContentLocationKeywords:
    """
    ContentLocationKeywords Class
    """
    def locate_text_coordinates(self, processed_img, text, pyt_conf='--psm 6', lang='eng'):
        """
        Purpose:
            Locates the coordinates of the provided text. This keyword gets the first occurrance of the text.
            Use Locate Multiple Text Coordinates if there is more than one occurrance of the text.
        Args:
            processed_img - the processed image.
            text - the text to locate.
            pyt_conf - the pytesseract image reading configuration.
            lang - the language of the text being read.
        Returns:
            The coordinates found, stored in a tuple (x, y). If nothing is found, None is returned.
        """
        verify_valid_image(processed_img)
        coordinates = return_text_coordinates(processed_img, text, pyt_conf, lang)
        return coordinates

    def locate_multiple_text_coordinates(self, processed_img, text, pyt_conf='--psm 6', lang='eng'):
        """
        Purpose:
            Locates the coordiantes of more than one instance of the provided text. This keyword can also be used if there is one occurrance.
        Args:
            processed_img - the processed image.
            text - the text to locate.
            pyt_conf - the pytesseract image reading configuration.
            lang - the language of the text being read.
        Returns:
            A list of coordinates found, each index stores a tuple (x, y). If nothing is found, None is returned.
        """
        verify_valid_image(processed_img)
        multiple_coordinates = return_multiple_text_coordinates(processed_img, text, pyt_conf, lang)
        return multiple_coordinates

    def locate_text_bounds(self, processed_img, text, pyt_conf='--psm 6', lang='eng'):
        """
        Purpose:
            Locates the bounds found around the provided text. This keyword gets the first occurrance of the text.
            Use Locate Multiple Text bounds if there is more than one occurrance of the text.
        Args:
            processed_img - the processed image.
            text - the text to locate.
            pyt_conf - the pytesseract image reading configuration.
            lang - the language of the text being read.
        Returns:
            A tuple of the bounds is returned. Returns None if nothing is found.
                Tuple[0] - x (the x value of the bound furthest to the left)
                Tuple[1] - y (the y value of the bound on the top)
                Tuple[2] - w (the width of the bound)
                Tuple[3] - h (the height of the bound)
        """
        verify_valid_image(processed_img)
        bounds = return_text_bounds(processed_img, text, pyt_conf, lang)
        return bounds

    def locate_multiple_text_bounds(self, processed_img, text, pyt_conf='--psm 6', lang='eng'):
        """
        Purpose:
            Locates the bounds found around more than one instance of the provided text. This keyword can also be used if there is one occurrance.
        Args:
            processed_img - the processed image.
            text - the text to locate.
            pyt_conf - the pytesseract image reading configuration.
            lang - the language of the text being read.
        Returns:
            A list of tuples containing the bounds are returned if the text is found. Returns None if nothing is found.
                Tuple[0] - x (the x value of the bound furthest to the left)
                Tuple[1] - y (the y value of the bound on the top)
                Tuple[2] - w (the width of the bound)
                Tuple[3] - h (the height of the bound)
        """
        verify_valid_image(processed_img)
        multiple_bounds = return_multiple_text_bounds(processed_img, text, pyt_conf, lang)
        return multiple_bounds
