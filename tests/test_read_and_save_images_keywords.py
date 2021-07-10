"""
Module to test keywords within GenericImageProcessingKeywords class.
"""

import unittest
import cv2
import numpy as np
from robot.libraries.BuiltIn import RobotNotRunningError

from OCRLibrary.keywords.read_and_save_images import ReadImageKeywords as rik
from OCRLibrary.keywords.read_and_save_images import SaveImageKeywords as sik
from OCRLibrary.utils.exceptions.exceptions import InvalidImagePath

class BaseReadImageKeywords(unittest.TestCase):
    """
    Base Class for testing ReadImageKeywords
    """
    @classmethod
    def setUpClass(cls):
        cls.keyword = rik()
        cls.valid_image_path = 'tests/images/test_colour_masking.png'
        cls.invalid_image_path = 'invalid/path/to/image.png'

    @classmethod
    def tearDownClass(cls):
        del cls.keyword
        del cls.valid_image_path
        del cls.invalid_image_path

class BaseSaveImageKeywords(unittest.TestCase):
    """
    Base Class for testing SaveImageKeywords
    """
    @classmethod
    def setUpClass(cls):
        cls.keyword = sik()
        cls.processed_image = cv2.imread('tests/images/test_colour_masking.png')
        cls.invalid_path_to_image_dir = 'invalid/path/to/image/dir/'
        cls.valid_path_to_image_dir = 'tests/images/save_result.png'

    @classmethod
    def tearDownClass(cls):
        del cls.keyword
        del cls.processed_image
        del cls.invalid_path_to_image_dir
        del cls.valid_path_to_image_dir

class TestKeywordReadImage(BaseReadImageKeywords):
    """
    TestKeywordReadImage Class
    """
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

class TestKeywordSaveImage(BaseSaveImageKeywords):
    """
    TestKeywordSaveImage Class

    Test cases require to except RobotNotRunningError because the keyword is not called from robot.
    """
    def test_01_save_image(self):
        """
        End to end flow of Save Image keyword with unspecified image path.
        """
        try:
            self.assertTrue(self.keyword.save_image(self.processed_image))
        except RobotNotRunningError:
            pass

    def test_02_save_image(self):
        """
        End to end flow of Save Image keyword with specified image path.
        """
        try:
            self.assertTrue(self.keyword.save_image(self.processed_image, self.valid_path_to_image_dir))
        except RobotNotRunningError:
            pass

    def test_03_save_image(self):
        """
        Invalid image path to raise InvalidImagePath
        """
        try:
            with self.assertRaises(InvalidImagePath):
                self.keyword.save_image(self.processed_image, self.invalid_path_to_image_dir)
        except RobotNotRunningError:
            pass
