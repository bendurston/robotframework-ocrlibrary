"""
Text locating module.
"""

from pytesseract import image_to_data, Output

def return_text_coordinates(img, text, pyt_conf, lang):
    """
    This keyword is find the coordinates of text in an image.
    """
    data = image_to_data(img, output_type=Output.DICT, config=pyt_conf, lang=lang)
    boxes = len(data['level'])
    for i in range(boxes):
        text_from_image = data['text'][i]
        if text_from_image == text:
            box_bounds = (int(data['left'][i]), int(data['top'][i]), int(data['width'][i]), int(data['height'][i]))
            x = box_bounds[0] + box_bounds[2]/2
            y = box_bounds[1] + box_bounds[3]/2
            return x, y
    return None

def return_multiple_text_coordinates(img, text, pyt_conf, lang):
    """
    To be used when there are multiple occurrences of the same text you wish to find.
    """
    data = image_to_data(img, output_type=Output.DICT, config=pyt_conf, lang=lang)
    boxes = len(data['level'])
    list_of_coordinates = []
    for i in range(boxes):
        text_from_image = data['text'][i]
        if text_from_image == text:
            box_bounds = (int(data['left'][i]), int(data['top'][i]), int(data['width'][i]), int(data['height'][i]))
            x = box_bounds[0] + box_bounds[2]/2
            y = box_bounds[1] + box_bounds[3]/2
            coordinates = (x, y)
            list_of_coordinates.append(coordinates)
    if not list_of_coordinates:
        return None
    return list_of_coordinates

def return_text_bounds(img, text, pyt_conf, lang):
    """
    This keyword is find the coordinates of text in an image.
    """
    data = image_to_data(img, output_type=Output.DICT, config=pyt_conf, lang=lang)
    boxes = len(data['level'])
    for i in range(boxes):
        text_from_image = data['text'][i]
        if text_from_image == text:
            box_bounds = (int(data['left'][i]), int(data['top'][i]), int(data['width'][i]), int(data['height'][i]))
            return box_bounds
    return None

def return_multiple_text_bounds(img, text, pyt_conf, lang):
    """
    To be used when there are multiple occurrences of the same text you wish to find.
    """
    data = image_to_data(img, output_type=Output.DICT, config=pyt_conf, lang=lang)
    boxes = len(data['level'])
    list_of_box_bounds = []
    for i in range(boxes):
        text_from_image = data['text'][i]
        if text_from_image == text:
            box_bounds = (int(data['left'][i]), int(data['top'][i]), int(data['width'][i]), int(data['height'][i]))
            list_of_box_bounds.append(box_bounds)
    if not list_of_box_bounds:
        return None
    return list_of_box_bounds
