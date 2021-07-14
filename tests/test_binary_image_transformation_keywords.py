"""
Module to test keywords within BinaryImageTransformationKeywords class.
"""
import unittest
import cv2
import numpy as np

from OCRLibrary.keywords.binary_image_transformation import ImageThresholdingKeywords as itk
from OCRLibrary.keywords.binary_image_transformation import MorphologicalTransformationKeywords  as mtk
from OCRLibrary.utils.exceptions.exceptions \
    import (InvalidImagePath, InvalidThresholdValue, InvalidKernelSize, InvalidKernelType, InvalidIteration, InvalidImageArgument)

class BaseImageThresholdingKeywords(unittest.TestCase):
    """
    Base Class for testing BinaryImageTransformationKeywords
    """
    @classmethod
    def setUpClass(cls):
        cls.keyword = itk()
        cls.img_path = 'tests/images/locate_text_coordinates1.png'
        cls.invalid_img_path = 'invalid/path/to/image.png'

    @classmethod
    def tearDownClass(cls):
        del cls.keyword
        del cls.img_path
        del cls.invalid_img_path

class BaseMorphologicalTransformationKeywords(unittest.TestCase):
    """
    Base Class for testing BaseMorphologicalTransformationKeywords
    """
    @classmethod
    def setUpClass(cls):
        cls.keyword = mtk()
        cls.processed_image = cv2.imread('tests/images/locate_text_coordinates2.png')
        cls.invalid_image = 'invalid_image.png'

    @classmethod
    def tearDownClass(cls):
        del cls.keyword
        del cls.processed_image
        del cls.invalid_image

class TestKeywordGetBinaryImage(BaseImageThresholdingKeywords):
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

class TestKeywordGetToZeroImage(BaseImageThresholdingKeywords):
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

class TestKeywordGetTruncImage(BaseImageThresholdingKeywords):
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

class TestKeywordApplyErosionToImage(BaseMorphologicalTransformationKeywords):
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

class TestKeywordAppyDilationToImage(BaseMorphologicalTransformationKeywords):
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

class TestKeywordApplyOpeningToImage(BaseMorphologicalTransformationKeywords):
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

class TestKeywordAppyClosingToImage(BaseMorphologicalTransformationKeywords):
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

class TestKeywordAppyGradientToImage(BaseMorphologicalTransformationKeywords):
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

class TestKeywordAppyTopHatToImage(BaseMorphologicalTransformationKeywords):
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

class TestKeywordApplyBlackHatToImage(BaseMorphologicalTransformationKeywords):
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
