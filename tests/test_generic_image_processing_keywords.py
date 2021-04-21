"""
Module to test keywords within GenericImageProcessingKeywords class.
"""

import unittest
import cv2
import numpy as np

from OCRLibrary.keywords.generic_image_processing import GenericImageProcessingKeywords as gipk
from OCRLibrary.utils.exceptions.exceptions import InvalidImagePath

class BaseGenericImageProcessingKeywords(unittest.TestCase):
    """
    Base Class for testing GenericImageProcessingKeywords
    """
    @classmethod
    def setUpClass(cls):
        cls.keyword = gipk()
        cls.processed_image = cv2.imread('tests/images/test_colour_masking.png')

    @classmethod
    def tearDownClass(cls):
        del cls.keyword
        del cls.processed_image

class TestKeywordReadImage(BaseGenericImageProcessingKeywords):
    """
    TestKeywordReadImage Class
    """
    def setUp(self):
        self.valid_image_path = 'tests/images/test_colour_masking.png'
        self.invalid_image_path = 'invalid/path/to/image.png'

    def tearDown(self):
        del self.valid_image_path
        del self.invalid_image_path

    def test_01_read_image(self):
        """
        End to end flow of Read Image keyword.
        """
        read_image = self.keyword.read_image(self.valid_image_path)
        self.assertTrue(isinstance(read_image, np.ndarray))

    def test_02_read_image(self):
        """
        Invalid image path to raise InvalidImagePath
        """
        with self.assertRaises(InvalidImagePath):
            self.keyword.read_image(self.invalid_image_path)

class TestKeywordSaveImage(BaseGenericImageProcessingKeywords):
    """
    TestKeywordSaveImage Class
    """
    def setUp(self):
        self.invalid_path_to_image_dir = 'invalid/path/to/image/dir/'
        self.img_name = 'test_image.png'
        self.valid_path_to_image_dir = 'tests/images/save_result.png'

    def tearDown(self):
        del self.invalid_path_to_image_dir
        del self.img_name
        del self.valid_path_to_image_dir

    def test_01_save_image(self):
        """
        End to end flow of Save Image keyword.
        """
        self.assertTrue(self.keyword.save_image(self.valid_path_to_image_dir, self.processed_image))

    def test_02_save_image(self):
        """
        Invalid image path to raise InvalidImagePath
        """
        with self.assertRaises(InvalidImagePath):
            self.keyword.save_image(self.invalid_path_to_image_dir, self.img_name)
