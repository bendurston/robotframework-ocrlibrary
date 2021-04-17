### Check if lower level mask functions work with both tuple hsv values and int bgr values.


### Tests for all image processing keywords.. Gets and Applies

import unittest
import cv2
import numpy
from OCRLibrary.OCRLibraryKeywords \
    import (Get_Gray_Scale_Image, Get_Binary_Image, Get_To_Zero_Image, Get_Trunc_Image,
    Read_Image, Save_Image, Convert_Image_To_HSV, Mask_Colour, Mask_Colours, Apply_Erosion_To_Image,
    Apply_Dilation_To_Image, Apply_Opening_To_Image, Apply_Closing_To_Image, Apply_Gradient_To_Image,
    Apply_Top_Hat_To_Image, Apply_Black_Hat_To_Image, Apply_Filter2D_To_Image, Apply_Median_Filtering_To_Image,
    Apply_Averaging_Blur_To_Image, Apply_Gaussian_Blur_To_Image)
from OCRLibrary.utils.exceptions.exceptions \
    import (InvalidImagePath, InvalidThresholdValue, InvalidImageArgument,
    InvalidBGRBoundArguments, InvalidHSVBoundArguments, InvalidKernelSize, InvalidKernelType, InvalidIteration)

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

class TestBinaryImageTransformation(unittest.TestCase):
    """
    TestBinaryImageTransformation class
    """

    def setUp(self):
        self.processed_image = cv2.imread('tests/images/locate_text_coordinates2.png')

    def tearDown(self):
        del self.processed_image

    def test_01_apply_erosion_to_image(self):
        """
        End to end flow of Apply Erosion To Image keyword.
        """
        erosion_image = Apply_Erosion_To_Image(self.processed_image, (1, 1), 0)
        self.assertTrue(isinstance(erosion_image, numpy.ndarray))
        erosion_image = Apply_Erosion_To_Image(self.processed_image, (1, 1), 1)
        self.assertTrue(isinstance(erosion_image, numpy.ndarray))
        erosion_image = Apply_Erosion_To_Image(self.processed_image, (1, 1), 2)
        self.assertTrue(isinstance(erosion_image, numpy.ndarray))

    def test_02_apply_erosion_to_image(self):
        """
        Invalid kernel size argument raises InvalidKernelSize.
        """
        with self.assertRaises(InvalidKernelSize):
            Apply_Erosion_To_Image(self.processed_image, None, 0)
        with self.assertRaises(InvalidKernelSize):
            Apply_Erosion_To_Image(self.processed_image, 3, 0)
        with self.assertRaises(InvalidKernelSize):
            Apply_Erosion_To_Image(self.processed_image, "string", 0)
        with self.assertRaises(InvalidKernelSize):
            Apply_Erosion_To_Image(self.processed_image, (10, -1), 0)
        with self.assertRaises(InvalidKernelSize):
            Apply_Erosion_To_Image(self.processed_image, (-10, 1), 0)
        with self.assertRaises(InvalidKernelSize):
            Apply_Erosion_To_Image(self.processed_image, (0, 0), 0)

    def test_03_apply_erosion_to_image(self):
        """
        Invalid iteration argument raises InvalidIteration
        """
        with self.assertRaises(InvalidIteration):
            Apply_Erosion_To_Image(self.processed_image, (1, 1), 0, -1)
        with self.assertRaises(InvalidIteration):
            Apply_Erosion_To_Image(self.processed_image, (1, 1), 0, 0)
        with self.assertRaises(InvalidIteration):
            Apply_Erosion_To_Image(self.processed_image, (1, 1), 0, "string")
        with self.assertRaises(InvalidIteration):
            Apply_Erosion_To_Image(self.processed_image, (1, 1), 0, 1.1)
        with self.assertRaises(InvalidIteration):
            Apply_Erosion_To_Image(self.processed_image, (1, 1), 0, None)

    def test_04_apply_erosion_to_image(self):
        """
        Invalid kernel type argument raises InvalidKernelType
        """
        with self.assertRaises(InvalidKernelType):
            Apply_Erosion_To_Image(self.processed_image, (1, 1), -1)
        with self.assertRaises(InvalidKernelType):
            Apply_Erosion_To_Image(self.processed_image, (1, 1), 1.1)
        with self.assertRaises(InvalidKernelType):
            Apply_Erosion_To_Image(self.processed_image, (1, 1), None)
        with self.assertRaises(InvalidKernelType):
            Apply_Erosion_To_Image(self.processed_image, (1, 1), "1")

    def test_01_apply_dilation_to_image(self):
        """
        End to end flow of Apply Dilation To Image keyword.
        """
        dilation_image = Apply_Dilation_To_Image(self.processed_image, (1, 1), 0)
        self.assertTrue(isinstance(dilation_image, numpy.ndarray))
        dilation_image = Apply_Dilation_To_Image(self.processed_image, (1, 1), 1)
        self.assertTrue(isinstance(dilation_image, numpy.ndarray))
        dilation_image = Apply_Dilation_To_Image(self.processed_image, (1, 1), 2)
        self.assertTrue(isinstance(dilation_image, numpy.ndarray))

    def test_02_apply_dilation_to_image(self):
        """
        Invalid kernel size argument raises InvalidKernelSize.
        """
        with self.assertRaises(InvalidKernelSize):
            Apply_Erosion_To_Image(self.processed_image, None, 0)
        with self.assertRaises(InvalidKernelSize):
            Apply_Dilation_To_Image(self.processed_image, 3, 0)
        with self.assertRaises(InvalidKernelSize):
            Apply_Dilation_To_Image(self.processed_image, "string", 0)
        with self.assertRaises(InvalidKernelSize):
            Apply_Dilation_To_Image(self.processed_image, (10, -1), 0)
        with self.assertRaises(InvalidKernelSize):
            Apply_Dilation_To_Image(self.processed_image, (-10, 1), 0)
        with self.assertRaises(InvalidKernelSize):
            Apply_Dilation_To_Image(self.processed_image, (0, 0), 0)

    def test_03_apply_dilation_to_image(self):
        """
        Invalid iteration argument raises InvalidIteration
        """
        with self.assertRaises(InvalidIteration):
            Apply_Dilation_To_Image(self.processed_image, (1, 1), 0, -1)
        with self.assertRaises(InvalidIteration):
            Apply_Dilation_To_Image(self.processed_image, (1, 1), 0, 0)
        with self.assertRaises(InvalidIteration):
            Apply_Dilation_To_Image(self.processed_image, (1, 1), 0, "string")
        with self.assertRaises(InvalidIteration):
            Apply_Dilation_To_Image(self.processed_image, (1, 1), 0, 1.1)
        with self.assertRaises(InvalidIteration):
            Apply_Dilation_To_Image(self.processed_image, (1, 1), 0, None)

    def test_04_apply_dilation_to_image(self):
        """
        Invalid kernel type argument raises InvalidKernelType
        """
        with self.assertRaises(InvalidKernelType):
            Apply_Dilation_To_Image(self.processed_image, (1, 1), -1)
        with self.assertRaises(InvalidKernelType):
            Apply_Dilation_To_Image(self.processed_image, (1, 1), 1.1)
        with self.assertRaises(InvalidKernelType):
            Apply_Dilation_To_Image(self.processed_image, (1, 1), None)
        with self.assertRaises(InvalidKernelType):
            Apply_Dilation_To_Image(self.processed_image, (1, 1), "1")

    def test_01_apply_opening_to_image(self):
        """
        End to end flow of Apply Opening To Image keyword.
        """
        opening_image = Apply_Opening_To_Image(self.processed_image, (1, 1), 0)
        self.assertTrue(isinstance(opening_image, numpy.ndarray))
        opening_image = Apply_Opening_To_Image(self.processed_image, (1, 1), 1)
        self.assertTrue(isinstance(opening_image, numpy.ndarray))
        opening_image = Apply_Opening_To_Image(self.processed_image, (1, 1), 2)
        self.assertTrue(isinstance(opening_image, numpy.ndarray))

    def test_02_apply_opening_to_image(self):
        """
        Invalid kernel size argument raises InvalidKernelSize.
        """
        with self.assertRaises(InvalidKernelSize):
            Apply_Opening_To_Image(self.processed_image, None, 0)
        with self.assertRaises(InvalidKernelSize):
            Apply_Opening_To_Image(self.processed_image, 3, 0)
        with self.assertRaises(InvalidKernelSize):
            Apply_Opening_To_Image(self.processed_image, "string", 0)
        with self.assertRaises(InvalidKernelSize):
            Apply_Opening_To_Image(self.processed_image, (10, -1), 0)
        with self.assertRaises(InvalidKernelSize):
            Apply_Opening_To_Image(self.processed_image, (-10, 1), 0)
        with self.assertRaises(InvalidKernelSize):
            Apply_Opening_To_Image(self.processed_image, (0, 0), 0)

    def test_03_apply_opening_to_image(self):
        """
        Invalid iteration argument raises InvalidIteration
        """
        with self.assertRaises(InvalidIteration):
            Apply_Opening_To_Image(self.processed_image, (1, 1), 0, -1)
        with self.assertRaises(InvalidIteration):
            Apply_Opening_To_Image(self.processed_image, (1, 1), 0, 0)
        with self.assertRaises(InvalidIteration):
            Apply_Opening_To_Image(self.processed_image, (1, 1), 0, "string")
        with self.assertRaises(InvalidIteration):
            Apply_Opening_To_Image(self.processed_image, (1, 1), 0, 1.1)
        with self.assertRaises(InvalidIteration):
            Apply_Opening_To_Image(self.processed_image, (1, 1), 0, None)

    def test_04_apply_opening_to_image(self):
        """
        Invalid kernel type argument raises InvalidKernelType
        """
        with self.assertRaises(InvalidKernelType):
            Apply_Opening_To_Image(self.processed_image, (1, 1), -1)
        with self.assertRaises(InvalidKernelType):
            Apply_Opening_To_Image(self.processed_image, (1, 1), 1.1)
        with self.assertRaises(InvalidKernelType):
            Apply_Opening_To_Image(self.processed_image, (1, 1), None)
        with self.assertRaises(InvalidKernelType):
            Apply_Opening_To_Image(self.processed_image, (1, 1), "1")

    def test_01_apply_closing_to_image(self):
        """
        End to end flow of Apply Closing To Image keyword.
        """
        closing_image = Apply_Opening_To_Image(self.processed_image, (1, 1), 0)
        self.assertTrue(isinstance(closing_image, numpy.ndarray))
        closing_image = Apply_Opening_To_Image(self.processed_image, (1, 1), 1)
        self.assertTrue(isinstance(closing_image, numpy.ndarray))
        closing_image = Apply_Opening_To_Image(self.processed_image, (1, 1), 2)
        self.assertTrue(isinstance(closing_image, numpy.ndarray))

    def test_02_apply_closing_to_image(self):
        """
        Invalid kernel size argument raises InvalidKernelSize.
        """
        with self.assertRaises(InvalidKernelSize):
            Apply_Closing_To_Image(self.processed_image, None, 0)
        with self.assertRaises(InvalidKernelSize):
            Apply_Closing_To_Image(self.processed_image, 3, 0)
        with self.assertRaises(InvalidKernelSize):
            Apply_Closing_To_Image(self.processed_image, "string", 0)
        with self.assertRaises(InvalidKernelSize):
            Apply_Closing_To_Image(self.processed_image, (10, -1), 0)
        with self.assertRaises(InvalidKernelSize):
            Apply_Closing_To_Image(self.processed_image, (-10, 1), 0)
        with self.assertRaises(InvalidKernelSize):
            Apply_Closing_To_Image(self.processed_image, (0, 0), 0)

    def test_03_apply_closing_to_image(self):
        """
        Invalid iteration argument raises InvalidIteration
        """
        with self.assertRaises(InvalidIteration):
            Apply_Closing_To_Image(self.processed_image, (1, 1), 0, -1)
        with self.assertRaises(InvalidIteration):
            Apply_Closing_To_Image(self.processed_image, (1, 1), 0, 0)
        with self.assertRaises(InvalidIteration):
            Apply_Closing_To_Image(self.processed_image, (1, 1), 0, "string")
        with self.assertRaises(InvalidIteration):
            Apply_Closing_To_Image(self.processed_image, (1, 1), 0, 1.1)
        with self.assertRaises(InvalidIteration):
            Apply_Closing_To_Image(self.processed_image, (1, 1), 0, None)

    def test_04_apply_closing_to_image(self):
        """
        Invalid kernel type argument raises InvalidKernelType
        """
        with self.assertRaises(InvalidKernelType):
            Apply_Closing_To_Image(self.processed_image, (1, 1), -1)
        with self.assertRaises(InvalidKernelType):
            Apply_Closing_To_Image(self.processed_image, (1, 1), 1.1)
        with self.assertRaises(InvalidKernelType):
            Apply_Closing_To_Image(self.processed_image, (1, 1), None)
        with self.assertRaises(InvalidKernelType):
            Apply_Closing_To_Image(self.processed_image, (1, 1), "1")

    def test_01_apply_gradient_to_image(self):
        """
        End to end flow of Apply Gradient To Image keyword.
        """
        gradient_image = Apply_Gradient_To_Image(self.processed_image, (1, 1), 0)
        self.assertTrue(isinstance(gradient_image, numpy.ndarray))
        gradient_image = Apply_Gradient_To_Image(self.processed_image, (1, 1), 1)
        self.assertTrue(isinstance(gradient_image, numpy.ndarray))
        gradient_image = Apply_Gradient_To_Image(self.processed_image, (1, 1), 2)
        self.assertTrue(isinstance(gradient_image, numpy.ndarray))

    def test_02_apply_gradient_to_image(self):
        """
        Invalid kernel size argument raises InvalidKernelSize.
        """
        with self.assertRaises(InvalidKernelSize):
            Apply_Gradient_To_Image(self.processed_image, None, 0)
        with self.assertRaises(InvalidKernelSize):
            Apply_Gradient_To_Image(self.processed_image, 3, 0)
        with self.assertRaises(InvalidKernelSize):
            Apply_Gradient_To_Image(self.processed_image, "string", 0)
        with self.assertRaises(InvalidKernelSize):
            Apply_Gradient_To_Image(self.processed_image, (10, -1), 0)
        with self.assertRaises(InvalidKernelSize):
            Apply_Gradient_To_Image(self.processed_image, (-10, 1), 0)
        with self.assertRaises(InvalidKernelSize):
            Apply_Gradient_To_Image(self.processed_image, (0, 0), 0)

    def test_03_apply_gradient_to_image(self):
        """
        Invalid iteration argument raises InvalidIteration
        """
        with self.assertRaises(InvalidIteration):
            Apply_Gradient_To_Image(self.processed_image, (1, 1), 0, -1)
        with self.assertRaises(InvalidIteration):
            Apply_Gradient_To_Image(self.processed_image, (1, 1), 0, 0)
        with self.assertRaises(InvalidIteration):
            Apply_Gradient_To_Image(self.processed_image, (1, 1), 0, "string")
        with self.assertRaises(InvalidIteration):
            Apply_Gradient_To_Image(self.processed_image, (1, 1), 0, 1.1)
        with self.assertRaises(InvalidIteration):
            Apply_Gradient_To_Image(self.processed_image, (1, 1), 0, None)

    def test_04_apply_gradient_to_image(self):
        """
        Invalid kernel type argument raises InvalidKernelType
        """
        with self.assertRaises(InvalidKernelType):
            Apply_Gradient_To_Image(self.processed_image, (1, 1), -1)
        with self.assertRaises(InvalidKernelType):
            Apply_Gradient_To_Image(self.processed_image, (1, 1), 1.1)
        with self.assertRaises(InvalidKernelType):
            Apply_Gradient_To_Image(self.processed_image, (1, 1), None)
        with self.assertRaises(InvalidKernelType):
            Apply_Gradient_To_Image(self.processed_image, (1, 1), "1")

    def test_01_apply_top_hat_to_image(self):
        """
        End to end flow of Apply Top Hat To Image keyword.
        """
        top_hat_image = Apply_Top_Hat_To_Image(self.processed_image, (1, 1), 0)
        self.assertTrue(isinstance(top_hat_image, numpy.ndarray))
        top_hat_image = Apply_Top_Hat_To_Image(self.processed_image, (1, 1), 1)
        self.assertTrue(isinstance(top_hat_image, numpy.ndarray))
        top_hat_image = Apply_Top_Hat_To_Image(self.processed_image, (1, 1), 2)
        self.assertTrue(isinstance(top_hat_image, numpy.ndarray))

    def test_02_apply_top_hat_to_image(self):
        """
        Invalid kernel size argument raises InvalidKernelSize.
        """
        with self.assertRaises(InvalidKernelSize):
            Apply_Top_Hat_To_Image(self.processed_image, None, 0)
        with self.assertRaises(InvalidKernelSize):
            Apply_Top_Hat_To_Image(self.processed_image, 3, 0)
        with self.assertRaises(InvalidKernelSize):
            Apply_Top_Hat_To_Image(self.processed_image, "string", 0)
        with self.assertRaises(InvalidKernelSize):
            Apply_Top_Hat_To_Image(self.processed_image, (10, -1), 0)
        with self.assertRaises(InvalidKernelSize):
            Apply_Top_Hat_To_Image(self.processed_image, (-10, 1), 0)
        with self.assertRaises(InvalidKernelSize):
            Apply_Top_Hat_To_Image(self.processed_image, (0, 0), 0)

    def test_03_apply_top_hat_to_image(self):
        """
        Invalid iteration argument raises InvalidIteration
        """
        with self.assertRaises(InvalidIteration):
            Apply_Top_Hat_To_Image(self.processed_image, (1, 1), 0, -1)
        with self.assertRaises(InvalidIteration):
            Apply_Top_Hat_To_Image(self.processed_image, (1, 1), 0, 0)
        with self.assertRaises(InvalidIteration):
            Apply_Top_Hat_To_Image(self.processed_image, (1, 1), 0, "string")
        with self.assertRaises(InvalidIteration):
            Apply_Top_Hat_To_Image(self.processed_image, (1, 1), 0, 1.1)
        with self.assertRaises(InvalidIteration):
            Apply_Top_Hat_To_Image(self.processed_image, (1, 1), 0, None)

    def test_04_apply_top_hat_to_image(self):
        """
        Invalid kernel type argument raises InvalidKernelType
        """
        with self.assertRaises(InvalidKernelType):
            Apply_Top_Hat_To_Image(self.processed_image, (1, 1), -1)
        with self.assertRaises(InvalidKernelType):
            Apply_Top_Hat_To_Image(self.processed_image, (1, 1), 1.1)
        with self.assertRaises(InvalidKernelType):
            Apply_Top_Hat_To_Image(self.processed_image, (1, 1), None)
        with self.assertRaises(InvalidKernelType):
            Apply_Top_Hat_To_Image(self.processed_image, (1, 1), "1")

    def test_01_apply_black_hat_to_image(self):
        """
        End to end flow of Apply Black Hat To Image keyword.
        """
        black_hat_image = Apply_Black_Hat_To_Image(self.processed_image, (1, 1), 0)
        self.assertTrue(isinstance(black_hat_image, numpy.ndarray))
        black_hat_image = Apply_Black_Hat_To_Image(self.processed_image, (1, 1), 1)
        self.assertTrue(isinstance(black_hat_image, numpy.ndarray))
        black_hat_image = Apply_Black_Hat_To_Image(self.processed_image, (1, 1), 2)
        self.assertTrue(isinstance(black_hat_image, numpy.ndarray))

    def test_02_apply_black_hat_to_image(self):
        """
        Invalid kernel size argument raises InvalidKernelSize.
        """
        with self.assertRaises(InvalidKernelSize):
            Apply_Black_Hat_To_Image(self.processed_image, None, 0)
        with self.assertRaises(InvalidKernelSize):
            Apply_Black_Hat_To_Image(self.processed_image, 3, 0)
        with self.assertRaises(InvalidKernelSize):
            Apply_Black_Hat_To_Image(self.processed_image, "string", 0)
        with self.assertRaises(InvalidKernelSize):
            Apply_Black_Hat_To_Image(self.processed_image, (10, -1), 0)
        with self.assertRaises(InvalidKernelSize):
            Apply_Black_Hat_To_Image(self.processed_image, (-10, 1), 0)
        with self.assertRaises(InvalidKernelSize):
            Apply_Black_Hat_To_Image(self.processed_image, (0, 0), 0)

    def test_03_apply_black_hat_to_image(self):
        """
        Invalid iteration argument raises InvalidIteration
        """
        with self.assertRaises(InvalidIteration):
            Apply_Black_Hat_To_Image(self.processed_image, (1, 1), 0, -1)
        with self.assertRaises(InvalidIteration):
            Apply_Black_Hat_To_Image(self.processed_image, (1, 1), 0, 0)
        with self.assertRaises(InvalidIteration):
            Apply_Black_Hat_To_Image(self.processed_image, (1, 1), 0, "string")
        with self.assertRaises(InvalidIteration):
            Apply_Black_Hat_To_Image(self.processed_image, (1, 1), 0, 1.1)
        with self.assertRaises(InvalidIteration):
            Apply_Black_Hat_To_Image(self.processed_image, (1, 1), 0, None)

    def test_04_apply_black_hat_to_image(self):
        """
        Invalid kernel type argument raises InvalidKernelType
        """
        with self.assertRaises(InvalidKernelType):
            Apply_Black_Hat_To_Image(self.processed_image, (1, 1), -1)
        with self.assertRaises(InvalidKernelType):
            Apply_Black_Hat_To_Image(self.processed_image, (1, 1), 1.1)
        with self.assertRaises(InvalidKernelType):
            Apply_Black_Hat_To_Image(self.processed_image, (1, 1), None)
        with self.assertRaises(InvalidKernelType):
            Apply_Black_Hat_To_Image(self.processed_image, (1, 1), "1")

# class TestColourImageProcessing(unittest.TestCase):
#     """
#     TestColourImageProcessing class
#     """
#     def setUp(self):
#         pass

#     def tearDown(self):
#         pass

class TestColourImageTransformation(unittest.TestCase):
    """
    TestColourImageTransformation class
    """
    def setUp(self):
        self.processed_image = cv2.imread('tests/images/locate_text_coordinates1.png')
        self.invalid_image = 'path/to/invalid/image.png'
        self.mask_img_bgr = cv2.imread('tests/images/test_colour_masking.png')
        self.mask_img_hsv = cv2.cvtColor(self.mask_img_bgr, cv2.COLOR_BGR2HSV)
        self.mask_multi_img_bgr = cv2.imread('tests/images/test_multi_colour_masking.png')
        self.mask_multi_img_hsv = cv2.cvtColor(self.mask_multi_img_bgr, cv2.COLOR_BGR2HSV)

    def tearDown(self):
        del self.processed_image
        del self.invalid_image
        del self.mask_img_bgr
        del self.mask_img_hsv
        del self.mask_multi_img_bgr
        del self.mask_multi_img_hsv

    def test_01_convert_image_to_hsv(self):
        """
        End to end flow of Convert Image To HSV keyword.
        """
        hsv_image = Convert_Image_To_HSV(self.processed_image)
        self.assertTrue(isinstance(hsv_image, numpy.ndarray))

    def test_02_convert_image_to_hsv(self):
        """
        Invalid image argument raised InvalidImageArgument
        """
        with self.assertRaises(InvalidImageArgument):
            Convert_Image_To_HSV(self.invalid_image)

    def test_01_mask_colour(self):
        """
        End to end flow of Mask Colour keyword.
        """
        masked_bgr_img = Mask_Colour(self.mask_img_bgr, (100, 0, 0), (255, 0, 0), 0)
        masked_hsv_img = Mask_Colour(self.mask_img_hsv, (0, 75, 75), (0, 100, 100), 1)
        self.assertTrue(isinstance(masked_bgr_img, numpy.ndarray))
        self.assertTrue(isinstance(masked_hsv_img, numpy.ndarray))

    def test_02_mask_colour(self):
        """
        Invalid image argument raises InvalidImageArgument.
        """
        with self.assertRaises(InvalidImageArgument):
            Mask_Colour(self.invalid_image,(100, 0, 0), (255, 0, 0), 0)

    def test_03_mask_colour(self):
        """
        Invalid bounds raises InvalidBGRBoundArguments.
        """
        with self.assertRaises(InvalidBGRBoundArguments):
            Mask_Colour(self.mask_img_bgr, (0, 0, 0), (0, 0, 2560), 0)
        with self.assertRaises(InvalidBGRBoundArguments):
            Mask_Colour(self.mask_img_hsv, (0, 0, -2), (0, 0, 255), 0)
        with self.assertRaises(InvalidBGRBoundArguments):
            Mask_Colour(self.mask_img_bgr, (0, 0, 100), (0, "0", 100), 0)

    def test_04_mask_colour(self):
        """
        Invalid bounds raises InvalidHSVBoundArguments.
        """
        with self.assertRaises(InvalidHSVBoundArguments):
            Mask_Colour(self.mask_img_hsv, (0, 0, 0), (0, 0, 2560), 1)
        with self.assertRaises(InvalidHSVBoundArguments):
            Mask_Colour(self.mask_img_hsv, (0, 0, -2), (0, 0, 255), 1)
        with self.assertRaises(InvalidHSVBoundArguments):
            Mask_Colour(self.mask_img_hsv, (0, 0, 100), (0, "0", 100), 1)

    def test_01_mask_colours(self):
        """
        End to end flow of Mask Colours keyword.
        """
        masked_multi_bgr_img = Mask_Colours(self.mask_multi_img_bgr, (100, 0, 0), (255, 0, 0), (0, 0, 100), (0, 0, 255), 0)
        masked_multi_hsv_img = Mask_Colours(self.mask_multi_img_hsv, (0, 75, 75), (0, 100, 100), (50, 75, 75), (60, 100, 100), 1)
        self.assertTrue(isinstance(masked_multi_bgr_img, numpy.ndarray))
        self.assertTrue(isinstance(masked_multi_hsv_img, numpy.ndarray))

    def test_02_mask_colours(self):
        """
        Invalid image argument raises InvalidImageArgument.
        """
        with self.assertRaises(InvalidImageArgument):
            Mask_Colours(self.invalid_image,(100, 0, 0), (255, 0, 0), (100, 0, 0), (255, 0, 0), 0)

    def test_03_mask_colours(self):
        """
        Invalid bounds raises InvalidBGRBoundArguments
        """
        with self.assertRaises(InvalidBGRBoundArguments):
            Mask_Colours(self.mask_multi_img_bgr, (0, 0, 0), (0, 0, 2560), (0, 0, 0), (0, 0, 25), 0)
        with self.assertRaises(InvalidBGRBoundArguments):
            Mask_Colours(self.mask_multi_img_bgr, (0, 0, -2), (0, 0, 255), (0, 0, 0), (0, 0, 25), 0)
        with self.assertRaises(InvalidBGRBoundArguments):
            Mask_Colours(self.mask_multi_img_bgr, (0, 0, 100), (0, "0", 100), (0, 0, 0), (0, 0, 25), 0)

    def test_04_mask_colours(self):
        """
        Invalid bounds raises InvalidHSVBoundArguments
        """
        with self.assertRaises(InvalidHSVBoundArguments):
            Mask_Colours(self.mask_multi_img_hsv, (0, 0, 0), (0, 0, 2560), (0, 0, 0), (0, 0, 25), 1)
        with self.assertRaises(InvalidHSVBoundArguments):
            Mask_Colours(self.mask_multi_img_hsv, (0, 0, -2), (0, 0, 255), (0, 0, 0), (0, 0, 25), 1)
        with self.assertRaises(InvalidHSVBoundArguments):
            Mask_Colours(self.mask_multi_img_hsv, (0, 0, 100), (0, "0", 100), (0, 0, 0), (0, 0, 25), 1)

class TestBasicImageKeywords(unittest.TestCase):
    """
    TestBasicImageKeywords class
    """
    def setUp(self):
        self.processed_image = cv2.imread('tests/images/test_colour_masking.png')
        self.valid_image_path = 'tests/images/test_colour_masking.png'
        self.invalid_image_path = 'invalid/path/to/image.png'
        self.invalid_path_to_image_dir = 'invalid/path/to/image/dir/'
        self.img_name = 'test_image.png'
        self.valid_path_to_image_dir = 'tests/images/save_result.png'

    def tearDown(self):
        del self.processed_image
        del self.valid_image_path
        del self.invalid_image_path
        del self.invalid_path_to_image_dir
        del self.img_name
        del self.valid_path_to_image_dir

    def test_01_read_image(self):
        """
        End to end flow of Read Image keyword.
        """
        read_image = Read_Image(self.valid_image_path)
        self.assertTrue(isinstance(read_image, numpy.ndarray))

    def test_02_read_image(self):
        """
        Invalid image path to raise InvalidImagePath
        """
        with self.assertRaises(InvalidImagePath):
            Read_Image(self.invalid_image_path)

    def test_01_save_image(self):
        """
        End to end flow of Save Image keyword.
        """
        self.assertTrue(Save_Image(self.valid_path_to_image_dir, self.processed_image))

    def test_02_save_image(self):
        """
        Invalid image path to raise InvalidImagePath
        """
        with self.assertRaises(InvalidImagePath):
            Save_Image(self.invalid_path_to_image_dir, self.img_name)
