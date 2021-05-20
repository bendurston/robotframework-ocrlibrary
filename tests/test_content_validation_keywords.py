"""
Module to test keywords within ContentValidationKeywords class.
"""
import unittest
import cv2

from OCRLibrary.keywords.content_validation import ContentValidationKeywords as cvk
from OCRLibrary.utils.exceptions.exceptions \
    import (InvalidImageArgument, ContentNotFound)

class BaseContentValidationKeywords(unittest.TestCase):
    """
    Base Class for testing BinaryImageProcessingKeywords
    """
    @classmethod
    def setUpClass(cls):
        cls.keyword = cvk()
        cls.processed_image = cv2.imread('tests/images/validate_image_content_test1.png')
        cls.correct_expected_content = "This is a test of test case 1 for validating image content"
        cls.incorrect_expected_content = "Some content that is not in the image."

    @classmethod
    def tearDownClass(cls):
        del cls.keyword
        del cls.processed_image
        del cls.correct_expected_content
        del cls.incorrect_expected_content

class TestKeywordValidateImageContent(BaseContentValidationKeywords):
    """
    TestKeywordValidateImageContent Class
    """
    def test_01_validate_image_content(self):
        """
        End to end flow of function. All correct arguments.
        """
        self.assertTrue(self.keyword.validate_image_content(self.processed_image, self.correct_expected_content))

    def test_02_validate_image_content(self):
        """
        Raise InvalidImageArgument by providing incorrect processed_image.
        """
        with self.assertRaises(InvalidImageArgument):
            self.keyword.validate_image_content(None, self.correct_expected_content)

    def test_03_validate_image_content(self):
        """
        Raise ContentNotFound by providing incorrect expected_content.
        """
        with self.assertRaises(ContentNotFound):
            self.keyword.validate_image_content(self.processed_image, self.incorrect_expected_content)

class TestKeywordGetImageContent(BaseContentValidationKeywords):
    """
    TestKeywordGetImageContent Class
    """
    def test_01_get_image_content(self):
        """
        End to end flow of function. All correct arguments.
        """
        content = self.keyword.get_image_content(self.processed_image)
        self.assertTrue(isinstance(content, str))

    def test_02_get_image_content(self):
        """
        Raise InvalidImageArgument by providing incorrect processed_image.
        """
        with self.assertRaises(InvalidImageArgument):
            self.keyword.get_image_content(None)
