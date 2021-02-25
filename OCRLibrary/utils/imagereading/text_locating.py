import cv2
import pytesseract
from pytesseract import Output

def locate_text(img, text):
    """
    This keyword is find the coordinates of text in an image.
    """
    data = pytesseract.image_to_data(img, output_type=Output.DICT, config='--psm 6', lang='eng')
    num_boxes = len(data['level'])
    text = text.lower()
    for i in range(num_boxes):
            text_data = data['text'][i].lower()
            if text_data == text:
                (x, y, w, h) = (data['left'][i], data['top'][i], data['width'][i], data['height'][i])
                # May have to fix return statement if there are multiple pieces of the same text
                return (x, y, w, h)
                """
                To find middle of returned box.
                x = int(location[0]) + int((location[2]/2))
                y = int(location[1]) + int((location[3]/2))
                """