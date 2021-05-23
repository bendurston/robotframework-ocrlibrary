"""
Module to test keywords within ColourImageProcessingKeywords class.
"""
import unittest
import cv2
import numpy as np

from OCRLibrary.keywords.colour_image_processing import ColourImageProcessingKeywords as cipk
from OCRLibrary.utils.exceptions.exceptions \
    import (InvalidImageArgument, InvalidColourBoundArguments)

class BaseColourImageProcessingKeywords(unittest.TestCase):
    """
    Base Class for testing ColourImageProcessingKeywords
    """
    @classmethod
    def setUpClass(cls):
        cls.keyword = cipk()
        cls.invalid_image = 'path/to/invalid/image.png'

    @classmethod
    def tearDownClass(cls):
        del cls.keyword
        del cls.invalid_image

class TestKeywordCovertImageToHSV(BaseColourImageProcessingKeywords):
    """
    TestKeywordCovertImageToHSV Class
    """
    def setUp(self):
        self.processed_image = cv2.imread('tests/images/locate_text_coordinates1.png')

    def tearDown(self):
        del self.processed_image

    def test_01_convert_image_to_hsv(self):
        """
        End to end flow of Convert Image To HSV keyword.
        """
        hsv_image = self.keyword.convert_image_to_HSV(self.processed_image)
        self.assertTrue(isinstance(hsv_image, np.ndarray))

    def test_02_convert_image_to_hsv(self):
        """
        Invalid image argument raised InvalidImageArgument.
        """
        with self.assertRaises(InvalidImageArgument):
            self.keyword.convert_image_to_HSV(self.invalid_image)

class TestKeywordMaskColour(BaseColourImageProcessingKeywords):
    """
    TestKeywordsMaskColour Class
    """
    def setUp(self):
        self.mask_img_bgr = cv2.imread('tests/images/test_colour_masking.png')
        self.mask_img_hsv = cv2.cvtColor(self.mask_img_bgr, cv2.COLOR_BGR2HSV)

    def tearDown(self):
        del self.mask_img_bgr
        del self.mask_img_hsv

    def test_01_mask_colour(self):
        """
        End to end flow of Mask Colour keyword.
        """
        masked_bgr_img = self.keyword.mask_colour(self.mask_img_bgr, (100, 0, 0), (255, 0, 0))
        masked_hsv_img = self.keyword.mask_colour(self.mask_img_hsv, (0, 75, 75), (0, 100, 100))
        self.assertTrue(isinstance(masked_bgr_img, np.ndarray))
        self.assertTrue(isinstance(masked_hsv_img, np.ndarray))

    def test_02_mask_colour(self):
        """
        Invalid image argument raises InvalidImageArgument.
        """
        with self.assertRaises(InvalidImageArgument):
            self.keyword.mask_colour(self.invalid_image,(100, 0, 0), (255, 0, 0))

    def test_03_mask_colour(self):
        """
        Invalid bounds raises InvalidColourBoundArguments.
        """
        with self.assertRaises(InvalidColourBoundArguments):
            self.keyword.mask_colour(self.mask_img_bgr, (0, 0, 0), (0, 0, 2560))
        with self.assertRaises(InvalidColourBoundArguments):
            self.keyword.mask_colour(self.mask_img_hsv, (0, 0, -2), (0, 0, 255))

class TestKeywordMaskColours(BaseColourImageProcessingKeywords):
    """
    TestKeywordMaskColours Class
    """
    def setUp(self):
        self.mask_multi_img_bgr = cv2.imread('tests/images/test_multi_colour_masking.png')
        self.mask_multi_img_hsv = cv2.cvtColor(self.mask_multi_img_bgr, cv2.COLOR_BGR2HSV)

    def tearDown(self):
        del self.mask_multi_img_bgr
        del self.mask_multi_img_hsv

    def test_01_mask_colours(self):
        """
        End to end flow of Mask Colours keyword.
        """
        masked_multi_bgr_img = self.keyword.mask_colours(self.mask_multi_img_bgr, (100, 0, 0), (255, 0, 0), (0, 0, 100), (0, 0, 255))
        masked_multi_hsv_img = self.keyword.mask_colours(self.mask_multi_img_hsv, (0, 75, 75), (0, 100, 100), (50, 75, 75), (60, 100, 100))
        self.assertTrue(isinstance(masked_multi_bgr_img, np.ndarray))
        self.assertTrue(isinstance(masked_multi_hsv_img, np.ndarray))

    def test_02_mask_colours(self):
        """
        Invalid image argument raises InvalidImageArgument.
        """
        with self.assertRaises(InvalidImageArgument):
            self.keyword.mask_colours(self.invalid_image,(100, 0, 0), (255, 0, 0), (100, 0, 0), (255, 0, 0))

    def test_03_mask_colours(self):
        """
        Invalid bounds raises InvalidColourBoundArguments.
        """
        with self.assertRaises(InvalidColourBoundArguments):
            self.keyword.mask_colours(self.mask_multi_img_bgr, (0, 0, 0), (0, 0, 2560), (0, 0, 0), (0, 0, 25))
        with self.assertRaises(InvalidColourBoundArguments):
            self.keyword.mask_colours(self.mask_multi_img_bgr, (0, 0, -2), (0, 0, 255), (0, 0, 0), (0, 0, 25))
