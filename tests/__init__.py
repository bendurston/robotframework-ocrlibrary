"""
tests module
"""
from .test_binary_image_transformation_keywords \
    import (TestKeywordGetBinaryImage, TestKeywordGetToZeroImage, TestKeywordGetTruncImage, 
    TestKeywordApplyErosionToImage, TestKeywordAppyDilationToImage, TestKeywordAppyGradientToImage,
    TestKeywordApplyOpeningToImage, TestKeywordAppyClosingToImage, TestKeywordAppyTopHatToImage,
    TestKeywordApplyBlackHatToImage)

from .test_changing_colourspace_tranformation_keywords \
    import (TestKeywordConvertImageToGrayScale, TestKeywordCovertImageToHSV, TestKeywordMaskColour,
    TestKeywordMaskColours)

from .test_content_location_keywords \
    import (TestKeywordLocateTextCoordinates, TestKeywordLocateMultipleTextCoordinates, TestKeywordLocateTextBounds,
    TestKeywordLocateMultipleTextBounds)

from .test_content_validation_keywords \
    import (TestKeywordValidateImageContent)

from .test_read_and_save_images_keywords \
    import (TestKeywordReadImage, TestKeywordSaveImage)

from .test_smoothing_image_transformation_keywords \
    import (TestKeywordAppyFilter2DToImage, TestKeywordApplyMedianFilteringToImage, TestKeywordApplyAveragingBlurToImage,
    TestKeywordApplyGaussianBlurToImage)

__all__ = [
    "TestKeywordGetBinaryImage",
    "TestKeywordGetToZeroImage",
    "TestKeywordGetTruncImage",
    "TestKeywordApplyErosionToImage",
    "TestKeywordAppyDilationToImage",
    "TestKeywordAppyGradientToImage",
    "TestKeywordApplyOpeningToImage",
    "TestKeywordAppyClosingToImage",
    "TestKeywordAppyTopHatToImage",
    "TestKeywordApplyBlackHatToImage",
    "TestKeywordConvertImageToGrayScale",
    "TestKeywordCovertImageToHSV",
    "TestKeywordMaskColour",
    "TestKeywordMaskColours",
    "TestKeywordLocateTextCoordinates",
    "TestKeywordLocateMultipleTextCoordinates",
    "TestKeywordLocateTextBounds",
    "TestKeywordLocateMultipleTextBounds",
    "TestKeywordValidateImageContent",
    "TestKeywordReadImage",
    "TestKeywordSaveImage",
    "TestKeywordAppyFilter2DToImage",
    "TestKeywordApplyMedianFilteringToImage",
    "TestKeywordApplyAveragingBlurToImage",
    "TestKeywordApplyGaussianBlurToImage"
]
