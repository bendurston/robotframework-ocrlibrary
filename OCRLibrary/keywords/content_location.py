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
        Locates the coordinates of the provided text. This keyword gets the first occurrance of the text.
        Use ``Locate Multiple Text Coordinates`` if there is more than one occurrance of the text.
        The coordinates found are returned as a tuple (x, y). If nothing is found, None is returned.

        See `introduction` for details about pyt_conf and lang arguments.

        Please note: as of version 1.2.0 this keyword only finds the coordinates of a single word. This will not
        work for sentances.
        """
        verify_valid_image(processed_img)
        coordinates = return_text_coordinates(processed_img, text, pyt_conf, lang)
        return coordinates

    def locate_multiple_text_coordinates(self, processed_img, text, pyt_conf='--psm 6', lang='eng'):
        """
        Locates the coordiantes of more than one instance of the provided text. This keyword can also be used if there is only
        one occurrance of the text. A list of coordinates found is return, each index stores a tuple (x, y).
        If nothing is found, None is returned.

        See `introduction` for details about pyt_conf and lang arguments.

        Please note: as of version 1.2.0 this keyword only finds the coordinates of a single word. This will not
        work for sentances.
        """
        verify_valid_image(processed_img)
        multiple_coordinates = return_multiple_text_coordinates(processed_img, text, pyt_conf, lang)
        return multiple_coordinates

    def locate_text_bounds(self, processed_img, text, pyt_conf='--psm 6', lang='eng'):
        """
        Locates the bounds found around the provided text. This keyword gets the first occurrance of the text.
        Use ``Locate Multiple Text Bounds`` if there is more than one occurrance of the text.
        A tuple of the bounds is returned. Returns None if nothing is found.

        Example:
        | ${result}=    Locate Text Bounds    ${processed_img}    OK
        | ${x}=    Set Variable    ${result}[0]
        | ${y}=    Set Variable    ${result}[1]
        | ${w}=    Set Variable    ${result}[2]
        | ${h}=    Set Variable    ${result}[3]

        Bounds refer to the box around the word "OK".
        - x represents the bound furthest to the left.
        - y represents the top of the bound.
        - w represents the width of the bound.
        - h represents the height of the bound.

        See `introduction` for details about pyt_conf and lang arguments.

        Please note: as of version 1.2.0 this keyword only finds the coordinates of a single word. This will not
        work for sentances.
        """
        verify_valid_image(processed_img)
        bounds = return_text_bounds(processed_img, text, pyt_conf, lang)
        return bounds

    def locate_multiple_text_bounds(self, processed_img, text, pyt_conf='--psm 6', lang='eng'):
        """
        Locates the bounds found around more than one instance of the provided text. This keyword can also be used if there is one occurrance
        of the text. A list of tuples containing the bounds are returned if the text is found. Returns None if nothing is found.
        
        See ``Locate Text Bounds`` documentation for an example of what each index in the tuple corresponds to.

        See `introduction` for details about pyt_conf and lang arguments.

        Please note: as of version 1.2.0 this keyword only finds the coordinates of a single word. This will not
        work for sentances.
        """
        verify_valid_image(processed_img)
        multiple_bounds = return_multiple_text_bounds(processed_img, text, pyt_conf, lang)
        return multiple_bounds
