import unittest
import cv2
from OCRLibrary.OCRLibraryKeywords import Validate_Image_Content
from OCRLibrary.utils.exceptions.exceptions import *
class TestContentValidation(unittest.TestCase):

    def test_01_validate_image_content(self):
        """
        End to end flow of function. All correct arguments.
        """
        expected_content = "This is a test of test case 1 for validating image content"
        processed_image = cv2.imread('tests/images/validate_image_content_test1.png')
        self.assertTrue(Validate_Image_Content(processed_image, expected_content))

    def test_02_validate_image_content(self):
        """
        Raise InvalidImageArgument by providing incorrect processed_image.
        """
        expected_content = "This is a test of test case 1 for validating image content"
        processed_image = None
        with self.assertRaises(InvalidImageArgument):
            Validate_Image_Content(processed_image, expected_content)

    def test_03_validate_image_content(self):
        """
        Raise ContentNotFound by providing incorrect expected_content.
        """
        expected_content = "Some content that is not in the image."
        processed_image = cv2.imread('tests/images/validate_image_content_test1.png')
        with self.assertRaises(ContentNotFound):
            Validate_Image_Content(processed_image, expected_content)

