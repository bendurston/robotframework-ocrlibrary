"""
Module to test keywords within BinaryImageTransformationKeywords class.
"""
import unittest
import cv2
import numpy as np

from OCRLibrary.keywords.binary_image_transformation import BinaryImageTransformationKeywords as bitk
from OCRLibrary.utils.exceptions.exceptions \
    import (InvalidKernelSize, InvalidKernelType, InvalidIteration, InvalidImageArgument)

class BaseBinaryImageTransformationKeywords(unittest.TestCase):
    """
    Base Class for testing BinaryImageTransformationKeywords
    """
    @classmethod
    def setUpClass(cls):
        cls.keyword = bitk()
        cls.processed_image = cv2.imread('tests/images/locate_text_coordinates2.png')
        cls.invalid_image = 'invalid_image.png'

    @classmethod
    def tearDownClass(cls):
        del cls.keyword
        del cls.processed_image
        del cls.invalid_image

class TestKeywordApplyErosionToImage(BaseBinaryImageTransformationKeywords):
    """
    TestKeywordApplyErosionToImage Class
    """
    def test_01_apply_erosion_to_image(self):
        """
        End to end flow of Apply Erosion To Image keyword.
        """
        erosion_image = self.keyword.apply_erosion_to_image(self.processed_image, (2, 2), 0)
        self.assertTrue(isinstance(erosion_image, np.ndarray))
        erosion_image = self.keyword.apply_erosion_to_image(self.processed_image, [1, 1], 1)
        self.assertTrue(isinstance(erosion_image, np.ndarray))
        erosion_image = self.keyword.apply_erosion_to_image(self.processed_image, ("1.1", "1.1"), 2)
        self.assertTrue(isinstance(erosion_image, np.ndarray))

    def test_02_apply_erosion_to_image(self):
        """
        Invalid image argument raises InvalidImageArgument.
        """
        with self.assertRaises(InvalidImageArgument):
            self.keyword.apply_erosion_to_image(self.invalid_image, (1, 1))

    def test_03_apply_erosion_to_image(self):
        """
        Invalid kernel size argument raises InvalidKernelSize.
        """
        with self.assertRaises(InvalidKernelSize):
            self.keyword.apply_erosion_to_image(self.processed_image, None, 0)
        with self.assertRaises(InvalidKernelSize):
            self.keyword.apply_erosion_to_image(self.processed_image, 3, 0)
        with self.assertRaises(InvalidKernelSize):
            self.keyword.apply_erosion_to_image(self.processed_image, "string", 0)
        with self.assertRaises(InvalidKernelSize):
            self.keyword.apply_erosion_to_image(self.processed_image, (10, -1), 0)
        with self.assertRaises(InvalidKernelSize):
            self.keyword.apply_erosion_to_image(self.processed_image, (-10, 1), 0)
        with self.assertRaises(InvalidKernelSize):
            self.keyword.apply_erosion_to_image(self.processed_image, (0, 0), 0)

    def test_04_apply_erosion_to_image(self):
        """
        Invalid iteration argument raises InvalidIteration
        """
        with self.assertRaises(InvalidIteration):
            self.keyword.apply_erosion_to_image(self.processed_image, (1, 1), 0, -1)
        with self.assertRaises(InvalidIteration):
            self.keyword.apply_erosion_to_image(self.processed_image, (1, 1), 0, 0)
        with self.assertRaises(InvalidIteration):
            self.keyword.apply_erosion_to_image(self.processed_image, (1, 1), 0, "string")
        with self.assertRaises(InvalidIteration):
            self.keyword.apply_erosion_to_image(self.processed_image, (1, 1), 0, 1.1)
        with self.assertRaises(InvalidIteration):
            self.keyword.apply_erosion_to_image(self.processed_image, (1, 1), 0, None)

    def test_05_apply_erosion_to_image(self):
        """
        Invalid kernel type argument raises InvalidKernelType
        """
        with self.assertRaises(InvalidKernelType):
            self.keyword.apply_erosion_to_image(self.processed_image, (1, 1), -1)
        with self.assertRaises(InvalidKernelType):
            self.keyword.apply_erosion_to_image(self.processed_image, (1, 1), 1.1)
        with self.assertRaises(InvalidKernelType):
            self.keyword.apply_erosion_to_image(self.processed_image, (1, 1), None)
        with self.assertRaises(InvalidKernelType):
            self.keyword.apply_erosion_to_image(self.processed_image, (1, 1), "1")

class TestKeywordAppyDilationToImage(BaseBinaryImageTransformationKeywords):
    """
    TestKeywordAppyDilationToImage Class
    """
    def test_01_apply_dilation_to_image(self):
        """
        End to end flow of Apply Dilation To Image keyword.
        """
        dilation_image = self.keyword.apply_dilation_to_image(self.processed_image, (2, 2), 0)
        self.assertTrue(isinstance(dilation_image, np.ndarray))
        dilation_image = self.keyword.apply_dilation_to_image(self.processed_image, [1, 1], 1)
        self.assertTrue(isinstance(dilation_image, np.ndarray))
        dilation_image = self.keyword.apply_dilation_to_image(self.processed_image, ("1.1", "1.1"), 2)
        self.assertTrue(isinstance(dilation_image, np.ndarray))

    def test_02_apply_dilation_to_image(self):
        """
        Invalid image argument raises InvalidImageArgument.
        """
        with self.assertRaises(InvalidImageArgument):
            self.keyword.apply_dilation_to_image(self.invalid_image, (1, 1))

    def test_03_apply_dilation_to_image(self):
        """
        Invalid kernel size argument raises InvalidKernelSize.
        """
        with self.assertRaises(InvalidKernelSize):
            self.keyword.apply_dilation_to_image(self.processed_image, None, 0)
        with self.assertRaises(InvalidKernelSize):
            self.keyword.apply_dilation_to_image(self.processed_image, 3, 0)
        with self.assertRaises(InvalidKernelSize):
            self.keyword.apply_dilation_to_image(self.processed_image, "string", 0)
        with self.assertRaises(InvalidKernelSize):
            self.keyword.apply_dilation_to_image(self.processed_image, (10, -1), 0)
        with self.assertRaises(InvalidKernelSize):
            self.keyword.apply_dilation_to_image(self.processed_image, (-10, 1), 0)
        with self.assertRaises(InvalidKernelSize):
            self.keyword.apply_dilation_to_image(self.processed_image, (0, 0), 0)

    def test_04_apply_dilation_to_image(self):
        """
        Invalid iteration argument raises InvalidIteration
        """
        with self.assertRaises(InvalidIteration):
            self.keyword.apply_dilation_to_image(self.processed_image, (1, 1), 0, -1)
        with self.assertRaises(InvalidIteration):
            self.keyword.apply_dilation_to_image(self.processed_image, (1, 1), 0, 0)
        with self.assertRaises(InvalidIteration):
            self.keyword.apply_dilation_to_image(self.processed_image, (1, 1), 0, "string")
        with self.assertRaises(InvalidIteration):
            self.keyword.apply_dilation_to_image(self.processed_image, (1, 1), 0, 1.1)
        with self.assertRaises(InvalidIteration):
            self.keyword.apply_dilation_to_image(self.processed_image, (1, 1), 0, None)

    def test_05_apply_dilation_to_image(self):
        """
        Invalid kernel type argument raises InvalidKernelType
        """
        with self.assertRaises(InvalidKernelType):
            self.keyword.apply_dilation_to_image(self.processed_image, (1, 1), -1)
        with self.assertRaises(InvalidKernelType):
            self.keyword.apply_dilation_to_image(self.processed_image, (1, 1), 1.1)
        with self.assertRaises(InvalidKernelType):
            self.keyword.apply_dilation_to_image(self.processed_image, (1, 1), None)
        with self.assertRaises(InvalidKernelType):
            self.keyword.apply_dilation_to_image(self.processed_image, (1, 1), "1")

class TestKeywordApplyOpeningToImage(BaseBinaryImageTransformationKeywords):
    """
    TestKeywordApplyOpeningToImage Class
    """
    def test_01_apply_opening_to_image(self):
        """
        End to end flow of Apply Opening To Image keyword.
        """
        opening_image = self.keyword.apply_opening_to_image(self.processed_image, (2, 2), 0)
        self.assertTrue(isinstance(opening_image, np.ndarray))
        opening_image = self.keyword.apply_opening_to_image(self.processed_image, [1, 1], 1)
        self.assertTrue(isinstance(opening_image, np.ndarray))
        opening_image = self.keyword.apply_opening_to_image(self.processed_image, ("1.1", "1.1"), 2)
        self.assertTrue(isinstance(opening_image, np.ndarray))

    def test_02_apply_opening_to_image(self):
        """
        Invalid image argument raises InvalidImageArgument.
        """
        with self.assertRaises(InvalidImageArgument):
            self.keyword.apply_opening_to_image(self.invalid_image, (1, 1))

    def test_03_apply_opening_to_image(self):
        """
        Invalid kernel size argument raises InvalidKernelSize.
        """
        with self.assertRaises(InvalidKernelSize):
            self.keyword.apply_opening_to_image(self.processed_image, None, 0)
        with self.assertRaises(InvalidKernelSize):
            self.keyword.apply_opening_to_image(self.processed_image, 3, 0)
        with self.assertRaises(InvalidKernelSize):
            self.keyword.apply_opening_to_image(self.processed_image, "string", 0)
        with self.assertRaises(InvalidKernelSize):
            self.keyword.apply_opening_to_image(self.processed_image, (10, -1), 0)
        with self.assertRaises(InvalidKernelSize):
            self.keyword.apply_opening_to_image(self.processed_image, (-10, 1), 0)
        with self.assertRaises(InvalidKernelSize):
            self.keyword.apply_opening_to_image(self.processed_image, (0, 0), 0)

    def test_04_apply_opening_to_image(self):
        """
        Invalid iteration argument raises InvalidIteration
        """
        with self.assertRaises(InvalidIteration):
            self.keyword.apply_opening_to_image(self.processed_image, (1, 1), 0, -1)
        with self.assertRaises(InvalidIteration):
            self.keyword.apply_opening_to_image(self.processed_image, (1, 1), 0, 0)
        with self.assertRaises(InvalidIteration):
            self.keyword.apply_opening_to_image(self.processed_image, (1, 1), 0, "string")
        with self.assertRaises(InvalidIteration):
            self.keyword.apply_opening_to_image(self.processed_image, (1, 1), 0, 1.1)
        with self.assertRaises(InvalidIteration):
            self.keyword.apply_opening_to_image(self.processed_image, (1, 1), 0, None)

    def test_05_apply_opening_to_image(self):
        """
        Invalid kernel type argument raises InvalidKernelType
        """
        with self.assertRaises(InvalidKernelType):
            self.keyword.apply_opening_to_image(self.processed_image, (1, 1), -1)
        with self.assertRaises(InvalidKernelType):
            self.keyword.apply_opening_to_image(self.processed_image, (1, 1), 1.1)
        with self.assertRaises(InvalidKernelType):
            self.keyword.apply_opening_to_image(self.processed_image, (1, 1), None)
        with self.assertRaises(InvalidKernelType):
            self.keyword.apply_opening_to_image(self.processed_image, (1, 1), "1")

class TestKeywordAppyClosingToImage(BaseBinaryImageTransformationKeywords):
    """
    TestKeywordAppyClosingToImage Class
    """
    def test_01_apply_closing_to_image(self):
        """
        End to end flow of Apply Closing To Image keyword.
        """
        closing_image = self.keyword.apply_closing_to_image(self.processed_image, (2, 2), 0)
        self.assertTrue(isinstance(closing_image, np.ndarray))
        closing_image = self.keyword.apply_closing_to_image(self.processed_image, [1, 1], 1)
        self.assertTrue(isinstance(closing_image, np.ndarray))
        closing_image = self.keyword.apply_closing_to_image(self.processed_image, ("1.1", "1.1"), 2)
        self.assertTrue(isinstance(closing_image, np.ndarray))

    def test_02_apply_closing_to_image(self):
        """
        Invalid image argument raises InvalidImageArgument.
        """
        with self.assertRaises(InvalidImageArgument):
            self.keyword.apply_closing_to_image(self.invalid_image, (1, 1))

    def test_03_apply_closing_to_image(self):
        """
        Invalid kernel size argument raises InvalidKernelSize.
        """
        with self.assertRaises(InvalidKernelSize):
            self.keyword.apply_closing_to_image(self.processed_image, None, 0)
        with self.assertRaises(InvalidKernelSize):
            self.keyword.apply_closing_to_image(self.processed_image, 3, 0)
        with self.assertRaises(InvalidKernelSize):
            self.keyword.apply_closing_to_image(self.processed_image, "string", 0)
        with self.assertRaises(InvalidKernelSize):
            self.keyword.apply_closing_to_image(self.processed_image, (10, -1), 0)
        with self.assertRaises(InvalidKernelSize):
            self.keyword.apply_closing_to_image(self.processed_image, (-10, 1), 0)
        with self.assertRaises(InvalidKernelSize):
            self.keyword.apply_closing_to_image(self.processed_image, (0, 0), 0)

    def test_04_apply_closing_to_image(self):
        """
        Invalid iteration argument raises InvalidIteration
        """
        with self.assertRaises(InvalidIteration):
            self.keyword.apply_closing_to_image(self.processed_image, (1, 1), 0, -1)
        with self.assertRaises(InvalidIteration):
            self.keyword.apply_closing_to_image(self.processed_image, (1, 1), 0, 0)
        with self.assertRaises(InvalidIteration):
            self.keyword.apply_closing_to_image(self.processed_image, (1, 1), 0, "string")
        with self.assertRaises(InvalidIteration):
            self.keyword.apply_closing_to_image(self.processed_image, (1, 1), 0, 1.1)
        with self.assertRaises(InvalidIteration):
            self.keyword.apply_closing_to_image(self.processed_image, (1, 1), 0, None)

    def test_05_apply_closing_to_image(self):
        """
        Invalid kernel type argument raises InvalidKernelType
        """
        with self.assertRaises(InvalidKernelType):
            self.keyword.apply_closing_to_image(self.processed_image, (1, 1), -1)
        with self.assertRaises(InvalidKernelType):
            self.keyword.apply_closing_to_image(self.processed_image, (1, 1), 1.1)
        with self.assertRaises(InvalidKernelType):
            self.keyword.apply_closing_to_image(self.processed_image, (1, 1), None)
        with self.assertRaises(InvalidKernelType):
            self.keyword.apply_closing_to_image(self.processed_image, (1, 1), "1")

class TestKeywordAppyGradientToImage(BaseBinaryImageTransformationKeywords):
    """
    TestKeywordAppyGradientToImage Class
    """
    def test_01_apply_gradient_to_image(self):
        """
        End to end flow of Apply Gradient To Image keyword.
        """
        gradient_image = self.keyword.apply_gradient_to_image(self.processed_image, (2, 2), 0)
        self.assertTrue(isinstance(gradient_image, np.ndarray))
        gradient_image = self.keyword.apply_gradient_to_image(self.processed_image, [1, 1], 1)
        self.assertTrue(isinstance(gradient_image, np.ndarray))
        gradient_image = self.keyword.apply_gradient_to_image(self.processed_image, ("1.1", "1.1"), 2)
        self.assertTrue(isinstance(gradient_image, np.ndarray))

    def test_02_apply_gradient_to_image(self):
        """
        Invalid image argument raises InvalidImageArgument.
        """
        with self.assertRaises(InvalidImageArgument):
            self.keyword.apply_gradient_to_image(self.invalid_image, (1, 1))

    def test_03_apply_gradient_to_image(self):
        """
        Invalid kernel size argument raises InvalidKernelSize.
        """
        with self.assertRaises(InvalidKernelSize):
            self.keyword.apply_gradient_to_image(self.processed_image, None, 0)
        with self.assertRaises(InvalidKernelSize):
            self.keyword.apply_gradient_to_image(self.processed_image, 3, 0)
        with self.assertRaises(InvalidKernelSize):
            self.keyword.apply_gradient_to_image(self.processed_image, "string", 0)
        with self.assertRaises(InvalidKernelSize):
            self.keyword.apply_gradient_to_image(self.processed_image, (10, -1), 0)
        with self.assertRaises(InvalidKernelSize):
            self.keyword.apply_gradient_to_image(self.processed_image, (-10, 1), 0)
        with self.assertRaises(InvalidKernelSize):
            self.keyword.apply_gradient_to_image(self.processed_image, (0, 0), 0)

    def test_04_apply_gradient_to_image(self):
        """
        Invalid iteration argument raises InvalidIteration
        """
        with self.assertRaises(InvalidIteration):
            self.keyword.apply_gradient_to_image(self.processed_image, (1, 1), 0, -1)
        with self.assertRaises(InvalidIteration):
            self.keyword.apply_gradient_to_image(self.processed_image, (1, 1), 0, 0)
        with self.assertRaises(InvalidIteration):
            self.keyword.apply_gradient_to_image(self.processed_image, (1, 1), 0, "string")
        with self.assertRaises(InvalidIteration):
            self.keyword.apply_gradient_to_image(self.processed_image, (1, 1), 0, 1.1)
        with self.assertRaises(InvalidIteration):
            self.keyword.apply_gradient_to_image(self.processed_image, (1, 1), 0, None)

    def test_05_apply_gradient_to_image(self):
        """
        Invalid kernel type argument raises InvalidKernelType
        """
        with self.assertRaises(InvalidKernelType):
            self.keyword.apply_gradient_to_image(self.processed_image, (1, 1), -1)
        with self.assertRaises(InvalidKernelType):
            self.keyword.apply_gradient_to_image(self.processed_image, (1, 1), 1.1)
        with self.assertRaises(InvalidKernelType):
            self.keyword.apply_gradient_to_image(self.processed_image, (1, 1), None)
        with self.assertRaises(InvalidKernelType):
            self.keyword.apply_gradient_to_image(self.processed_image, (1, 1), "1")

class TestKeywordAppyTopHatToImage(BaseBinaryImageTransformationKeywords):
    """
    TestKeywordAppyTopHatToImage Class
    """
    def test_01_apply_top_hat_to_image(self):
        """
        End to end flow of Apply Top Hat To Image keyword.
        """
        top_hat_image = self.keyword.apply_top_hat_to_image(self.processed_image, (2, 2), 0)
        self.assertTrue(isinstance(top_hat_image, np.ndarray))
        top_hat_image = self.keyword.apply_top_hat_to_image(self.processed_image, [1, 1], 1)
        self.assertTrue(isinstance(top_hat_image, np.ndarray))
        top_hat_image = self.keyword.apply_top_hat_to_image(self.processed_image, ("1.1", "1.1"), 2)
        self.assertTrue(isinstance(top_hat_image, np.ndarray))

    def test_02_apply_top_hat_to_image(self):
        """
        Invalid image argument raises InvalidImageArgument.
        """
        with self.assertRaises(InvalidImageArgument):
            self.keyword.apply_top_hat_to_image(self.invalid_image, (1, 1))

    def test_03_apply_top_hat_to_image(self):
        """
        Invalid kernel size argument raises InvalidKernelSize.
        """
        with self.assertRaises(InvalidKernelSize):
            self.keyword.apply_top_hat_to_image(self.processed_image, None, 0)
        with self.assertRaises(InvalidKernelSize):
            self.keyword.apply_top_hat_to_image(self.processed_image, 3, 0)
        with self.assertRaises(InvalidKernelSize):
            self.keyword.apply_top_hat_to_image(self.processed_image, "string", 0)
        with self.assertRaises(InvalidKernelSize):
            self.keyword.apply_top_hat_to_image(self.processed_image, (10, -1), 0)
        with self.assertRaises(InvalidKernelSize):
            self.keyword.apply_top_hat_to_image(self.processed_image, (-10, 1), 0)
        with self.assertRaises(InvalidKernelSize):
            self.keyword.apply_top_hat_to_image(self.processed_image, (0, 0), 0)

    def test_04_apply_top_hat_to_image(self):
        """
        Invalid iteration argument raises InvalidIteration
        """
        with self.assertRaises(InvalidIteration):
            self.keyword.apply_top_hat_to_image(self.processed_image, (1, 1), 0, -1)
        with self.assertRaises(InvalidIteration):
            self.keyword.apply_top_hat_to_image(self.processed_image, (1, 1), 0, 0)
        with self.assertRaises(InvalidIteration):
            self.keyword.apply_top_hat_to_image(self.processed_image, (1, 1), 0, "string")
        with self.assertRaises(InvalidIteration):
            self.keyword.apply_top_hat_to_image(self.processed_image, (1, 1), 0, 1.1)
        with self.assertRaises(InvalidIteration):
            self.keyword.apply_top_hat_to_image(self.processed_image, (1, 1), 0, None)

    def test_05_apply_top_hat_to_image(self):
        """
        Invalid kernel type argument raises InvalidKernelType
        """
        with self.assertRaises(InvalidKernelType):
            self.keyword.apply_top_hat_to_image(self.processed_image, (1, 1), -1)
        with self.assertRaises(InvalidKernelType):
            self.keyword.apply_top_hat_to_image(self.processed_image, (1, 1), 1.1)
        with self.assertRaises(InvalidKernelType):
            self.keyword.apply_top_hat_to_image(self.processed_image, (1, 1), None)
        with self.assertRaises(InvalidKernelType):
            self.keyword.apply_top_hat_to_image(self.processed_image, (1, 1), "1")

class TestKeywordApplyBlackHatToImage(BaseBinaryImageTransformationKeywords):
    """
    TestKeywordApplyBlackHatToImage Class
    """
    def test_01_apply_black_hat_to_image(self):
        """
        End to end flow of Apply Black Hat To Image keyword.
        """
        black_hat_image = self.keyword.apply_black_hat_to_image(self.processed_image, (2, 2), 0)
        self.assertTrue(isinstance(black_hat_image, np.ndarray))
        black_hat_image = self.keyword.apply_black_hat_to_image(self.processed_image, [1, 1], 1)
        self.assertTrue(isinstance(black_hat_image, np.ndarray))
        black_hat_image = self.keyword.apply_black_hat_to_image(self.processed_image, ("1.1", "1.1"), 2)
        self.assertTrue(isinstance(black_hat_image, np.ndarray))

    def test_02_apply_black_hat_to_image(self):
        """
        Invalid image argument raises InvalidImageArgument.
        """
        with self.assertRaises(InvalidImageArgument):
            self.keyword.apply_black_hat_to_image(self.invalid_image, (1, 1))

    def test_03_apply_black_hat_to_image(self):
        """
        Invalid kernel size argument raises InvalidKernelSize.
        """
        with self.assertRaises(InvalidKernelSize):
            self.keyword.apply_black_hat_to_image(self.processed_image, None, 0)
        with self.assertRaises(InvalidKernelSize):
            self.keyword.apply_black_hat_to_image(self.processed_image, 3, 0)
        with self.assertRaises(InvalidKernelSize):
            self.keyword.apply_black_hat_to_image(self.processed_image, "string", 0)
        with self.assertRaises(InvalidKernelSize):
            self.keyword.apply_black_hat_to_image(self.processed_image, (10, -1), 0)
        with self.assertRaises(InvalidKernelSize):
            self.keyword.apply_black_hat_to_image(self.processed_image, (-10, 1), 0)
        with self.assertRaises(InvalidKernelSize):
            self.keyword.apply_black_hat_to_image(self.processed_image, (0, 0), 0)

    def test_04_apply_black_hat_to_image(self):
        """
        Invalid iteration argument raises InvalidIteration
        """
        with self.assertRaises(InvalidIteration):
            self.keyword.apply_black_hat_to_image(self.processed_image, (1, 1), 0, -1)
        with self.assertRaises(InvalidIteration):
            self.keyword.apply_black_hat_to_image(self.processed_image, (1, 1), 0, 0)
        with self.assertRaises(InvalidIteration):
            self.keyword.apply_black_hat_to_image(self.processed_image, (1, 1), 0, "string")
        with self.assertRaises(InvalidIteration):
            self.keyword.apply_black_hat_to_image(self.processed_image, (1, 1), 0, 1.1)
        with self.assertRaises(InvalidIteration):
            self.keyword.apply_black_hat_to_image(self.processed_image, (1, 1), 0, None)

    def test_05_apply_black_hat_to_image(self):
        """
        Invalid kernel type argument raises InvalidKernelType
        """
        with self.assertRaises(InvalidKernelType):
            self.keyword.apply_black_hat_to_image(self.processed_image, (1, 1), -1)
        with self.assertRaises(InvalidKernelType):
            self.keyword.apply_black_hat_to_image(self.processed_image, (1, 1), 1.1)
        with self.assertRaises(InvalidKernelType):
            self.keyword.apply_black_hat_to_image(self.processed_image, (1, 1), None)
        with self.assertRaises(InvalidKernelType):
            self.keyword.apply_black_hat_to_image(self.processed_image, (1, 1), "1")
