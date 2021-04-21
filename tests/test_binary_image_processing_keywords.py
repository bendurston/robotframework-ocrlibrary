"""
Module to test keywords within BinaryImageProcessingKeywords class.
"""
import unittest
import numpy as np

from OCRLibrary.keywords.binary_image_processing import BinaryImageProcessingKeywords as bipk
from OCRLibrary.utils.exceptions.exceptions import InvalidImagePath, InvalidThresholdValue

class BaseBinaryImageProcessingKeywords(unittest.TestCase):
    """
    Base Class for testing BinaryImageProcessingKeywords
    """
    @classmethod
    def setUpClass(cls):
        cls.keyword = bipk()
        cls.img_path = 'tests/images/locate_text_coordinates1.png'
        cls.invalid_img_path = 'invalid/path/to/image.png'

    @classmethod
    def tearDownClass(cls):
        del cls.keyword
        del cls.img_path
        del cls.invalid_img_path

class TestKeywordGetGrayScaleImage(BaseBinaryImageProcessingKeywords):
    """
    TestKeywordGetGrayScaleImage Class
    """
    def test_01_get_gray_scale_image(self):
        """
        End to end flow of Get Gray Scale Image keyword. All correct arguments.
        """
        gray_scale_image = self.keyword.get_gray_scale_image(self.img_path)
        self.assertTrue(isinstance(gray_scale_image, np.ndarray))

    def test_02_get_gray_scale_image(self):
        """
        Invalid image path to raise InvalidImagePath.
        """
        with self.assertRaises(InvalidImagePath):
            self.keyword.get_gray_scale_image(self.invalid_img_path)

class TestKeywordGetBinaryImage(BaseBinaryImageProcessingKeywords):
    """
    TestKeywordGetBinaryImage Class
    """
    def test_01_get_binary_image(self):
        """
        End to end test of Get Binary Image keyword.
        """
        binary_image = self.keyword.get_binary_image(self.img_path)
        binary_image_otsu = self.keyword.get_binary_image(self.img_path, True)
        self.assertTrue(isinstance(binary_image, np.ndarray))
        self.assertTrue(isinstance(binary_image_otsu[0], float))
        self.assertTrue(isinstance(binary_image_otsu[1], np.ndarray))

    def test_02_get_binary_image(self):
        """
        Invalid image path to raise InvalidImagePath.
        """
        with self.assertRaises(InvalidImagePath):
            self.keyword.get_binary_image(self.invalid_img_path)

    def test_03_get_binary_image(self):
        """
        Invalid threshold values to raise InvalidThesholdValue.
        """
        with self.assertRaises(InvalidThresholdValue):
            self.keyword.get_binary_image(self.img_path, False, False, None, None)
        with self.assertRaises(InvalidThresholdValue):
            self.keyword.get_binary_image(self.img_path, False, False, "255", None)
        with self.assertRaises(InvalidThresholdValue):
            self.keyword.get_binary_image(self.img_path, False, False, None, "127")
        with self.assertRaises(InvalidThresholdValue):
            self.keyword.get_binary_image(self.img_path, False, False, "255", "127")
        with self.assertRaises(InvalidThresholdValue):
            self.keyword.get_binary_image(self.img_path, False, False, 255, None)
        with self.assertRaises(InvalidThresholdValue):
            self.keyword.get_binary_image(self.img_path, False, False, None, 127)

class TestKeywordGetToZeroImage(BaseBinaryImageProcessingKeywords):
    """
    TestKeywordGetToZeroImage Class
    """
    def test_01_get_to_zero_image(self):
        """
        End to end test of Get To Zero Image keyword.
        """
        to_zero_image = self.keyword.get_to_zero_image(self.img_path)
        to_zero_image_otsu = self.keyword.get_to_zero_image(self.img_path, True)
        self.assertTrue(isinstance(to_zero_image, np.ndarray))
        self.assertTrue(isinstance(to_zero_image_otsu[0], float))
        self.assertTrue(isinstance(to_zero_image_otsu[1], np.ndarray))

    def test_02_get_to_zero_image(self):
        """
        Invalid image path to raise InvalidImagePath.
        """
        with self.assertRaises(InvalidImagePath):
            self.keyword.get_to_zero_image(self.invalid_img_path)

    def test_03_get_to_zero_image(self):
        """
        Invalid threshold values to raise InvalidThresholdValue.
        """
        with self.assertRaises(InvalidThresholdValue):
            self.keyword.get_to_zero_image(self.img_path, False, False, None, None)
        with self.assertRaises(InvalidThresholdValue):
            self.keyword.get_to_zero_image(self.img_path, False, False, "255", None)
        with self.assertRaises(InvalidThresholdValue):
            self.keyword.get_to_zero_image(self.img_path, False, False, None, "127")
        with self.assertRaises(InvalidThresholdValue):
            self.keyword.get_to_zero_image(self.img_path, False, False, "255", "127")
        with self.assertRaises(InvalidThresholdValue):
            self.keyword.get_to_zero_image(self.img_path, False, False, 255, None)
        with self.assertRaises(InvalidThresholdValue):
            self.keyword.get_to_zero_image(self.img_path, False, False, None, 127)

class TestKeywordGetTruncImage(BaseBinaryImageProcessingKeywords):
    """
    TestKeywordGetTruncImage Class
    """
    def test_01_get_trunc_image(self):
        """
        End to end test of Get Trunc Image keyword.
        """
        trunc_image = self.keyword.get_trunc_image(self.img_path)
        trunc_image_otsu = self.keyword.get_trunc_image(self.img_path, True)
        self.assertTrue(isinstance(trunc_image, np.ndarray))
        self.assertTrue(isinstance(trunc_image_otsu[0], float))
        self.assertTrue(isinstance(trunc_image_otsu[1], np.ndarray))

    def test_02_get_trunc_image(self):
        """
        Invalid image path to raise InvalidImagePath.
        """
        with self.assertRaises(InvalidImagePath):
            self.keyword.get_trunc_image(self.invalid_img_path)

    def test_03_get_trunc_image(self):
        """
        Invalid threshold values to raise InvalidThresholdValue.
        """
        with self.assertRaises(InvalidThresholdValue):
            self.keyword.get_trunc_image(self.img_path, False, None, None)
        with self.assertRaises(InvalidThresholdValue):
            self.keyword.get_trunc_image(self.img_path, False, "255", None)
        with self.assertRaises(InvalidThresholdValue):
            self.keyword.get_trunc_image(self.img_path, False, None, "127")
        with self.assertRaises(InvalidThresholdValue):
            self.keyword.get_trunc_image(self.img_path, False, "255", "127")
        with self.assertRaises(InvalidThresholdValue):
            self.keyword.get_trunc_image(self.img_path, False, 255, None)
        with self.assertRaises(InvalidThresholdValue):
            self.keyword.get_trunc_image(self.img_path, False, None, 127)
