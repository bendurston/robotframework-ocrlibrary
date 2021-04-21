"""
Module to test keywords within ContentLocationKeywords class.
"""
import unittest
import cv2

from OCRLibrary.keywords.content_location import ContentLocationKeywords as clk
from OCRLibrary.utils.exceptions.exceptions \
    import (InvalidImageArgument)

class BaseContentLocationKeywords(unittest.TestCase):
    """
    Base Class for testing BinaryImageProcessingKeywords
    """
    @classmethod
    def setUpClass(cls):
        cls.keyword = clk()
        cls.processed_image = cv2.imread('tests/images/locate_text_coordinates1.png')
        cls.processed_image_multi = cv2.imread('tests/images/locate_text_coordinates2.png')
        cls.text = "Ok"
        cls.text_multi = "Hello"

    @classmethod
    def tearDownClass(cls):
        del cls.keyword
        del cls.processed_image
        del cls.processed_image_multi
        del cls.text
        del cls.text_multi

class TestKeywordLocateTextCoordinates(BaseContentLocationKeywords):
    """
    TestKeywordLocateTextCoordinates Class
    """
    def test_01_locate_text_coordinates(self):
        """
        End to end flow of Locate_Text_Coordinates function. All correct arguments.
        """
        expected_x_center = 944
        expected_y_center = 538
        actual_x, actual_y = self.keyword.locate_text_coordinates(self.processed_image, self.text)
        self.assertAlmostEqual(actual_x, expected_x_center, delta=5)
        self.assertAlmostEqual(actual_y, expected_y_center, delta=5)

    def test_02_locate_text_coordinates(self):
        """
        Pass in incorrect image
        """
        with self.assertRaises(InvalidImageArgument):
            self.keyword.locate_text_coordinates(None, self.text)

    def test_03_locate_text_coordinates(self):
        """
        Text was not found error
        """
        self.assertEqual(None, self.keyword.locate_text_coordinates(self.processed_image, "Invalid Text"))

class TestKeywordLocateMultipleTextCoordinates(BaseContentLocationKeywords):
    """
    TestKeywordLocateMultipleTextCoordinates Class
    """
    def test_01_locate_multiple_text_coordinates(self):
        """
        End to end flow of Locate Multiple Text Coordinates function. All arguments are correct.
        """
        expected_x = [380, 1380]
        expected_y = [335, 1335]
        result = self.keyword.locate_multiple_text_coordinates(self.processed_image_multi, self.text_multi)
        num_of_results = len(result) - 1
        for i in range(0, num_of_results):
            self.assertAlmostEqual(result[i][0], expected_x[i], delta=5)
            self.assertAlmostEqual(result[i][1], expected_y[i], delta=5)

    def test_02_locate_multiple_text_coordinates(self):
        """
        Pass in incorrect image
        """
        with self.assertRaises(InvalidImageArgument):
            self.keyword.locate_multiple_text_coordinates(None, self.text)

    def test_03_locate_multiple_text_coordinates(self):
        """
        Text was not found error
        """
        self.assertEqual(None, self.keyword.locate_multiple_text_coordinates(self.processed_image, "Invalid Text"))

class TestKeywordLocateTextBounds(BaseContentLocationKeywords):
    """
    TestKeywordLocateTextBounds Class
    """
    def test_01_locate_text_bounds(self):
        """
        End to end flow of Locate_Text_Bounds function. All correct arguments.
        """
        expected_x_bound = 900
        expected_y_bound = 510
        expected_w_bound = 84
        expected_h_bound = 45
        actual_x, actual_y, actual_w, actual_h = self.keyword.locate_text_bounds(self.processed_image, self.text)
        self.assertAlmostEqual(actual_x, expected_x_bound, delta=5)
        self.assertAlmostEqual(actual_y, expected_y_bound, delta=5)
        self.assertAlmostEqual(actual_w, expected_w_bound, delta=5)
        self.assertAlmostEqual(actual_h, expected_h_bound, delta=5)

    def test_02_locate_text_bounds(self):
        """
        Pass in incorrect iamge
        """
        with self.assertRaises(InvalidImageArgument):
            self.keyword.locate_text_bounds(None, self.text)

    def test_03_locate_text_bounds(self):
        """
        Text was not found error
        """
        self.assertEqual(None, self.keyword.locate_text_bounds(self.processed_image, "Invalid"))

class TestKeywordLocateMultipleTextBounds(BaseContentLocationKeywords):
    """
    TestKeywordLocateMultipleTextBounds Class
    """
    def test_01_locate_multiple_text_bounds(self):
        """
        End to end flow of Locate_Text_Bounds function. All correct arguments.
        """
        expected_x = [305, 1305]
        expected_y = [305, 710]
        expected_w = [150, 145]
        expected_h = [60, 45]
        result = self.keyword.locate_multiple_text_bounds(self.processed_image_multi, self.text_multi)
        num_of_results = len(result) - 1
        for i in range(0, num_of_results):
            self.assertAlmostEqual(result[i][0], expected_x[i], delta=5)
            self.assertAlmostEqual(result[i][1], expected_y[i], delta=5)
            self.assertAlmostEqual(result[i][2], expected_w[i], delta=5)
            self.assertAlmostEqual(result[i][3], expected_h[i], delta=5)

    def test_02_locate_multiple_text_bounds(self):
        """
        Pass in incorrect iamge
        """
        with self.assertRaises(InvalidImageArgument):
            self.keyword.locate_multiple_text_bounds(None, self.text)

    def test_03_locate_multiple_text_bounds(self):
        """
        Text was not found error
        """
        self.assertEqual(None, self.keyword.locate_multiple_text_bounds(self.processed_image, "Invalid"))
