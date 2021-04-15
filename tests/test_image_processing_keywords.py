### Check if lower level mask functions work with both tuple hsv values and int bgr values.


### Tests for all image processing keywords.. Gets and Applies

import unittest
import cv2
import numpy
from OCRLibrary.OCRLibraryKeywords \
    import (Get_Gray_Scale_Image, Get_Binary_Image, Get_To_Zero_Image, Get_Trunc_Image)
from OCRLibrary.utils.exceptions.exceptions import InvalidImagePath, InvalidThresholdValue

class TestBinaryImageProcessing(unittest.TestCase):
    """
    TestContentLocation class
    """
    def setUp(self):
        self.img_path = 'tests/images/locate_text_coordinates1.png'
        self.invalid_img_path = 'invalid/path/to/image.png'

    def tearDown(self):
        del self.img_path
        del self.invalid_img_path

    def test_01_get_gray_scale_image(self):
        """
        End to end flow of Get Gray Scale Image keyword. All correct arguments.
        """
        gray_scale_image = Get_Gray_Scale_Image(self.img_path)
        self.assertTrue(isinstance(gray_scale_image, numpy.ndarray))

    def test_02_get_gray_scale_image(self):
        """
        Invalid image path to raise InvalidImagePath.
        """
        with self.assertRaises(InvalidImagePath):
            Get_Gray_Scale_Image(self.invalid_img_path)

    def test_01_get_binary_image(self):
        """
        End to end test of Get Binary Image keyword.
        """
        binary_image = Get_Binary_Image(self.img_path)
        binary_image_otsu = Get_Binary_Image(self.img_path, True)
        self.assertTrue(isinstance(binary_image, numpy.ndarray))
        self.assertTrue(isinstance(binary_image_otsu[0], float))
        self.assertTrue(isinstance(binary_image_otsu[1], numpy.ndarray))

    def test_02_get_binary_image(self):
        """
        Invalid image path to raise InvalidImagePath.
        """
        with self.assertRaises(InvalidImagePath):
            Get_Binary_Image(self.invalid_img_path)

    def test_03_get_binary_image(self):
        """
        Invalid threshold values to raise InvalidThesholdValue.
        """
        with self.assertRaises(InvalidThresholdValue):
            Get_Binary_Image(self.img_path, False, False, None, None)
        with self.assertRaises(InvalidThresholdValue):
            Get_Binary_Image(self.img_path, False, False, "255", None)
        with self.assertRaises(InvalidThresholdValue):
            Get_Binary_Image(self.img_path, False, False, None, "127")
        with self.assertRaises(InvalidThresholdValue):
            Get_Binary_Image(self.img_path, False, False, "255", "127")
        with self.assertRaises(InvalidThresholdValue):
            Get_Binary_Image(self.img_path, False, False, 255, None)
        with self.assertRaises(InvalidThresholdValue):
            Get_Binary_Image(self.img_path, False, False, None, 127)

    def test_01_get_to_zero_image(self):
        """
        End to end test of Get To Zero Image keyword.
        """
        to_zero_image = Get_To_Zero_Image(self.img_path)
        to_zero_image_otsu = Get_To_Zero_Image(self.img_path, True)
        self.assertTrue(isinstance(to_zero_image, numpy.ndarray))
        self.assertTrue(isinstance(to_zero_image_otsu[0], float))
        self.assertTrue(isinstance(to_zero_image_otsu[1], numpy.ndarray))

    def test_02_get_to_zero_image(self):
        """
        Invalid image path to raise InvalidImagePath.
        """
        with self.assertRaises(InvalidImagePath):
            Get_To_Zero_Image(self.invalid_img_path)

    def test_03_get_to_zero_image(self):
        """
        Invalid threshold values to raise InvalidThresholdValue.
        """
        with self.assertRaises(InvalidThresholdValue):
            Get_To_Zero_Image(self.img_path, False, False, None, None)
        with self.assertRaises(InvalidThresholdValue):
            Get_To_Zero_Image(self.img_path, False, False, "255", None)
        with self.assertRaises(InvalidThresholdValue):
            Get_To_Zero_Image(self.img_path, False, False, None, "127")
        with self.assertRaises(InvalidThresholdValue):
            Get_To_Zero_Image(self.img_path, False, False, "255", "127")
        with self.assertRaises(InvalidThresholdValue):
            Get_To_Zero_Image(self.img_path, False, False, 255, None)
        with self.assertRaises(InvalidThresholdValue):
            Get_To_Zero_Image(self.img_path, False, False, None, 127)

    def test_01_get_trunc_image(self):
        """
        End to end test of Get Trunc Image keyword.
        """
        trunc_image = Get_Trunc_Image(self.img_path)
        trunc_image_otsu = Get_Trunc_Image(self.img_path, True)
        self.assertTrue(isinstance(trunc_image, numpy.ndarray))
        self.assertTrue(isinstance(trunc_image_otsu[0], float))
        self.assertTrue(isinstance(trunc_image_otsu[1], numpy.ndarray))

    def test_02_get_trunc_image(self):
        """
        Invalid image path to raise InvalidImagePath.
        """
        with self.assertRaises(InvalidImagePath):
            Get_Trunc_Image(self.invalid_img_path)

    def test_03_get_trunc_image(self):
        """
        Invalid threshold values to raise InvalidThresholdValue.
        """
        with self.assertRaises(InvalidThresholdValue):
            Get_Trunc_Image(self.img_path, False, None, None)
        with self.assertRaises(InvalidThresholdValue):
            Get_Trunc_Image(self.img_path, False, "255", None)
        with self.assertRaises(InvalidThresholdValue):
            Get_Trunc_Image(self.img_path, False, None, "127")
        with self.assertRaises(InvalidThresholdValue):
            Get_Trunc_Image(self.img_path, False, "255", "127")
        with self.assertRaises(InvalidThresholdValue):
            Get_Trunc_Image(self.img_path, False, 255, None)
        with self.assertRaises(InvalidThresholdValue):
            Get_Trunc_Image(self.img_path, False, None, 127)

# class TestBinaryImageTransformation(unittest.TestCase):
#     """
#     TestBinaryImageTransformation class
#     """

# class TestColourImageProcessing(unittest.TestCase):
#     """
#     TestColourImageProcessing class
#     """
#     def setUp(self):
#         pass

#     def tearDown(self):
#         pass

# class TestColourImageTransformation(unittest.TestCase):
#     """
#     TestColourImageTransformation class
#     """
#     def setUp(self):
#         pass

#     def tearDown(self):
#         pass
    