"""
Module for Content Validation tests.
"""

import unittest
import cv2
from OCRLibrary.OCRLibraryKeywords import Validate_Image_Content
from OCRLibrary.utils.exceptions.exceptions import InvalidImageArgument, ContentNotFound

class TestContentValidation(unittest.TestCase):
    """
    TestContentValidation class
    """
    def setUp(self):
        """
        Test fixture set up.
        """
        self.processed_image = cv2.imread('tests/images/validate_image_content_test1.png')
        self.correct_expected_content = "This is a test of test case 1 for validating image content"
        self.incorrect_expected_content = "Some content that is not in the image."
     
    def tearDown(self):
        """
        Test fixture tear down.
        """
        del self.processed_image
        del self.correct_expected_content
        del self.incorrect_expected_content

    def test_01_validate_image_content(self):
        """
        End to end flow of function. All correct arguments.
        """
        self.assertTrue(Validate_Image_Content(self.processed_image, self.correct_expected_content))

    def test_02_validate_image_content(self):
        """
        Raise InvalidImageArgument by providing incorrect processed_image.
        """
        with self.assertRaises(InvalidImageArgument):
            Validate_Image_Content(None, self.correct_expected_content)

    def test_03_validate_image_content(self):
        """
        Raise ContentNotFound by providing incorrect expected_content.
        """
        with self.assertRaises(ContentNotFound):
            Validate_Image_Content(self.processed_image, self.incorrect_expected_content)
