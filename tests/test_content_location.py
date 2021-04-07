"""
Module for Content Location tests.
"""

import unittest
import cv2
from OCRLibrary.OCRLibraryKeywords import Locate_Text_Coordinates, Locate_Multiple_Text_Coordinates, Locate_Text_Bounds, Locate_Multiple_Text_Bounds

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
        self.expected_x_center = 944
        self.expected_y_center = 538
        self.expected_x_bound = 900
        self.expected_y_bound = 510
        self.expected_w_bound = 84
        self.expected_h_bound = 45

    def tearDown(self):
        """
        Test fixture tear down.
        """
        del self.processed_image
        del self.text
        del self.expected_x_center
        del self.expected_y_center
        del self.expected_x_bound
        del self.expected_y_bound
        del self.expected_w_bound
        del self.expected_h_bound

    def test_01_locate_text_coordinates(self):
        """
        End to end flow of Locate_Text_Coordinates function. All correct arguments.
        """
        actual_x, actual_y = Locate_Text_Coordinates(self.processed_image, self.text)
        self.assertAlmostEqual(actual_x, self.expected_x_center, delta=5)
        self.assertAlmostEqual(actual_y, self.expected_y_center, delta=5)


    def test_01_locate_text_bounds(self):
        """
        End to end flow of Locate_Text_Bounds function. All correct arguments.
        """
        actual_x, actual_y, actual_w, actual_h = Locate_Text_Bounds(self.processed_image, self.text)
        self.assertAlmostEqual(actual_x, self.expected_x_bound, delta=5)
        self.assertAlmostEqual(actual_y, self.expected_y_bound, delta=5)
        self.assertAlmostEqual(actual_w, self.expected_w_bound, delta=5)
        self.assertAlmostEqual(actual_h, self.expected_h_bound, delta=5)
