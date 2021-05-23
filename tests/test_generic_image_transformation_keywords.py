"""
Module to test keywords within GenericImageTransformationKeywords class.
"""
import unittest
import cv2
import numpy as np

from OCRLibrary.keywords.generic_image_transformation import GenericImageTransformationKeywords as gitk
from OCRLibrary.utils.exceptions.exceptions \
    import (InvalidKernelSize, InvalidKernelType, InvalidDepthArgument, InvalidImageArgument)

class BaseGenericImageTransformationKeywords(unittest.TestCase):
    """
    Base Class for testing GenericImageTransformationKeywords
    """
    @classmethod
    def setUpClass(cls):
        cls.keyword = gitk()
        cls.processed_image = cv2.imread('tests/images/locate_text_coordinates2.png')
        cls.invalid_image = 'invalid_image.png'

    @classmethod
    def tearDownClass(cls):
        del cls.keyword
        del cls.processed_image
        del cls.invalid_image

class TestKeywordAppyFilter2DToImage(BaseGenericImageTransformationKeywords):
    """
    TestKeywordAppyFilter2DToImage Class
    """
    def test_01_apply_filter2d_to_image(self):
        """
        End to end flow of Apply Filter2D To Image keyword.
        """
        filter2d_image = self.keyword.apply_filter2D_to_image(self.processed_image, (1, 1), 0)
        self.assertTrue(isinstance(filter2d_image, np.ndarray))
        filter2d_image = self.keyword.apply_filter2D_to_image(self.processed_image, [1.1, 1.1], 1)
        self.assertTrue(isinstance(filter2d_image, np.ndarray))
        filter2d_image = self.keyword.apply_filter2D_to_image(self.processed_image, ("1", "1"), 2)
        self.assertTrue(isinstance(filter2d_image, np.ndarray))
        filter2d_image = self.keyword.apply_filter2D_to_image(self.processed_image, ("2", "2"), 2)
        self.assertTrue(isinstance(filter2d_image, np.ndarray))

    def test_02_apply_filter2d_to_image(self):
        """
        Invalid image argument raised InvalidImageArgument
        """
        with self.assertRaises(InvalidImageArgument):
            self.keyword.apply_filter2D_to_image(self.invalid_image, (1, 1))

    def test_03_apply_filter2d_to_image(self):
        """
        Invalid kernel size argument raises InvalidKernelSize.  
        """
        with self.assertRaises(InvalidKernelSize):
            self.keyword.apply_filter2D_to_image(self.processed_image, None, 0)
        with self.assertRaises(InvalidKernelSize):
            self.keyword.apply_filter2D_to_image(self.processed_image, 3, 0)
        with self.assertRaises(InvalidKernelSize):
            self.keyword.apply_filter2D_to_image(self.processed_image, "string", 0)
        with self.assertRaises(InvalidKernelSize):
            self.keyword.apply_filter2D_to_image(self.processed_image, (10, -1), 0)
        with self.assertRaises(InvalidKernelSize):
            self.keyword.apply_filter2D_to_image(self.processed_image, (-10, 1), 0)
        with self.assertRaises(InvalidKernelSize):
            self.keyword.apply_filter2D_to_image(self.processed_image, (0, 0), 0)

    def test_04_apply_filter2d_to_image(self):
        """
        Invalid depth argument raises InvalidDepthArgument.
        """
        with self.assertRaises(InvalidDepthArgument):
            self.keyword.apply_filter2D_to_image(self.processed_image, (1, 1), 0, 1)
        with self.assertRaises(InvalidDepthArgument):
            self.keyword.apply_filter2D_to_image(self.processed_image, (1, 1), 0, None)

    def test_05_apply_filter2d_to_image(self):
        """
        Invalid kernel type argument raises InvalidKernelType
        """
        with self.assertRaises(InvalidKernelType):
            self.keyword.apply_filter2D_to_image(self.processed_image, (1, 1), -1)

class TestKeywordApplyMedianFilteringToImage(BaseGenericImageTransformationKeywords):
    """
    TestKeywordApplyMedianFilteringToImage Class
    """
    def test_01_apply_median_filtering_to_image(self):
        """
        End to end flow of Apply Median Filtering To Image keyword.
        """
        median_filtering_image = self.keyword.apply_median_filtering_to_image(self.processed_image, 1)
        self.assertTrue(isinstance(median_filtering_image, np.ndarray))
        median_filtering_image = self.keyword.apply_median_filtering_to_image(self.processed_image, "1")
        self.assertTrue(isinstance(median_filtering_image, np.ndarray))

    def test_02_apply_median_filtering_to_image(self):
        """
        Invalid image argument raised InvalidImageArgument
        """
        with self.assertRaises(InvalidImageArgument):
            self.keyword.apply_median_filtering_to_image(self.invalid_image, 0)

    def test_03_apply_median_filtering_to_image(self):
        """
        Invalid non tuple kernel size raises InvalidKernelSize.
        """
        with self.assertRaises(InvalidKernelSize):
            self.keyword.apply_median_filtering_to_image(self.processed_image, 0)
        with self.assertRaises(InvalidKernelSize):
            self.keyword.apply_median_filtering_to_image(self.processed_image, None)
        with self.assertRaises(InvalidKernelSize):
            self.keyword.apply_median_filtering_to_image(self.processed_image, 2)
        with self.assertRaises(InvalidKernelSize):
            self.keyword.apply_median_filtering_to_image(self.processed_image, -1)

class TestKeywordApplyAveragingBlurToImage(BaseGenericImageTransformationKeywords):
    """
    TestKeywordApplyAveragingBlurToImage Class
    """
    def test_01_apply_averaging_blur_to_image(self):
        """
        End to end flow of Apply Averaging Blur To Image keyword.
        """
        averaging_blur_image = self.keyword.apply_averaging_blur_to_image(self.processed_image, (1, 1))
        self.assertTrue(isinstance(averaging_blur_image, np.ndarray))
        averaging_blur_image = self.keyword.apply_averaging_blur_to_image(self.processed_image, (1.1, 1.1))
        self.assertTrue(isinstance(averaging_blur_image, np.ndarray))
        averaging_blur_image = self.keyword.apply_averaging_blur_to_image(self.processed_image, [1.1, 1.1])
        self.assertTrue(isinstance(averaging_blur_image, np.ndarray))
        averaging_blur_image = self.keyword.apply_averaging_blur_to_image(self.processed_image, ["2.1", "1.1"])
        self.assertTrue(isinstance(averaging_blur_image, np.ndarray))

    def test_02_apply_averaging_blur_to_image(self):
        """
        Invalid image argument raised InvalidImageArgument
        """
        with self.assertRaises(InvalidImageArgument):
            self.keyword.apply_averaging_blur_to_image(self.invalid_image, (1, 1))

    def test_03_apply_averaging_blur_to_image(self):
        """
        Invalid kernel size argument raises InvalidKernelSize.
        """
        with self.assertRaises(InvalidKernelSize):
            self.keyword.apply_averaging_blur_to_image(self.processed_image, None)
        with self.assertRaises(InvalidKernelSize):
            self.keyword.apply_averaging_blur_to_image(self.processed_image, 3)
        with self.assertRaises(InvalidKernelSize):
            self.keyword.apply_averaging_blur_to_image(self.processed_image, "string")
        with self.assertRaises(InvalidKernelSize):
            self.keyword.apply_averaging_blur_to_image(self.processed_image, (10, -1))
        with self.assertRaises(InvalidKernelSize):
            self.keyword.apply_averaging_blur_to_image(self.processed_image, (-10, 1))
        with self.assertRaises(InvalidKernelSize):
            self.keyword.apply_averaging_blur_to_image(self.processed_image, (0, 0))

class TestKeywordApplyGaussianBlurToImage(BaseGenericImageTransformationKeywords):
    """
    TestKeywordApplyGaussianBlurToImage Class
    """
    def test_01_apply_gaussian_blur_to_image(self):
        """
        End to end flow of Apply Gaussian Blur To Image keyword.
        """
        gaussian_image = self.keyword.apply_gaussian_blur_to_image(self.processed_image, (1,1))
        self.assertTrue(isinstance(gaussian_image, np.ndarray))
        gaussian_image = self.keyword.apply_gaussian_blur_to_image(self.processed_image, [1, 1])
        self.assertTrue(isinstance(gaussian_image, np.ndarray))
        gaussian_image = self.keyword.apply_gaussian_blur_to_image(self.processed_image, ("1.1","1.1"))
        self.assertTrue(isinstance(gaussian_image, np.ndarray))

    def test_02_apply_gaussian_blur_to_image(self):
        """
        Invalid image argument raised InvalidImageArgument
        """
        with self.assertRaises(InvalidImageArgument):
            self.keyword.apply_gaussian_blur_to_image(self.invalid_image, (1, 1))

    def test_03_apply_gaussian_blur_to_image(self):
        """
        Invalid kernel size argument raises InvalidKernelSize.
        """
        with self.assertRaises(InvalidKernelSize):
            self.keyword.apply_gaussian_blur_to_image(self.processed_image, None)
        with self.assertRaises(InvalidKernelSize):
            self.keyword.apply_gaussian_blur_to_image(self.processed_image, 3)
        with self.assertRaises(InvalidKernelSize):
            self.keyword.apply_gaussian_blur_to_image(self.processed_image, "string")
        with self.assertRaises(InvalidKernelSize):
            self.keyword.apply_gaussian_blur_to_image(self.processed_image, (10, -1))
        with self.assertRaises(InvalidKernelSize):
            self.keyword.apply_gaussian_blur_to_image(self.processed_image, (-10, 1))
        with self.assertRaises(InvalidKernelSize):
            self.keyword.apply_gaussian_blur_to_image(self.processed_image, (0, 0))
        with self.assertRaises(InvalidKernelSize):
            self.keyword.apply_gaussian_blur_to_image(self.processed_image, (1, 2))
