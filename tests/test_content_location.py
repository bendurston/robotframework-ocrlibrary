"""
Module for Content Location tests.
"""

import unittest
import cv2
from OCRLibrary.OCRLibraryKeywords import Locate_Text_Coordinates, Locate_Multiple_Text_Coordinates, Locate_Text_Bounds, Locate_Multiple_Text_Bounds
from OCRLibrary.utils.exceptions.exceptions import InvalidImageArgument, ContentNotFound

class TestContentLocation(unittest.TestCase):
    """
    TestContentLocation class
    """
    def setUp(self):
        """
        Test fixture set up.
        """
        self.processed_image = cv2.imread('tests/images/locate_text_coordinates1.png')
        self.text = "Ok"

    def tearDown(self):
        """
        Test fixture tear down.
        """
        del self.processed_image
        del self.text

    def test_01_locate_text_coordinates(self):
        """
        End to end flow of Locate_Text_Coordinates function. All correct arguments.
        """
        expected_x_center = 944
        expected_y_center = 538
        actual_x, actual_y = Locate_Text_Coordinates(self.processed_image, self.text)
        self.assertAlmostEqual(actual_x, expected_x_center, delta=5)
        self.assertAlmostEqual(actual_y, expected_y_center, delta=5)

    def test_02_locate_text_coordinates(self):
        """
        Pass in incorrect image
        """
        with self.assertRaises(InvalidImageArgument):
            Locate_Text_Coordinates(None, self.text)

    def test_03_locate_text_coordinates(self):
        """
        Text was not found error
        """
        pass

    def test_01_locate_text_bounds(self):
        """
        End to end flow of Locate_Text_Bounds function. All correct arguments.
        """
        expected_x_bound = 900
        expected_y_bound = 510
        expected_w_bound = 84
        expected_h_bound = 45
        actual_x, actual_y, actual_w, actual_h = Locate_Text_Bounds(self.processed_image, self.text)
        self.assertAlmostEqual(actual_x, expected_x_bound, delta=5)
        self.assertAlmostEqual(actual_y, expected_y_bound, delta=5)
        self.assertAlmostEqual(actual_w, expected_w_bound, delta=5)
        self.assertAlmostEqual(actual_h, expected_h_bound, delta=5)

    def test_02_locate_text_bounds(self):
        """
        Pass in incorrect iamge
        """
        with self.assertRaises(InvalidImageArgument):
            Locate_Text_Bounds(None, self.text)

    def test_03_locate_text_bounds(self):
        """
        Text was not found error
        """
        pass