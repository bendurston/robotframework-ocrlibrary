"""
tests module
"""
from .test_binary_image_transformation_keywords \
    import (TestKeywordApplyErosionToImage, TestKeywordAppyDilationToImage, TestKeywordAppyGradientToImage,
    TestKeywordApplyOpeningToImage, TestKeywordAppyClosingToImage, TestKeywordAppyTopHatToImage,
    TestKeywordApplyBlackHatToImage)
from .test_binary_image_processing_keywords \
    import (TestKeywordGetBinaryImage, TestKeywordGetGrayScaleImage, TestKeywordGetToZeroImage, TestKeywordGetTruncImage)
from .test_colour_image_processing_keywords \
    import (TestKeywordCovertImageToHSV, TestKeywordMaskColour, TestKeywordMaskColours)
from .test_generic_image_transformation_keywords \
    import (TestKeywordApplyAveragingBlurToImage, TestKeywordApplyGaussianBlurToImage, TestKeywordApplyMedianFilteringToImage,
    TestKeywordAppyFilter2DToImage)
from .test_generic_image_processing_keywords \
    import (TestKeywordReadImage, TestKeywordSaveImage)
from .test_content_validation_keywords \
    import (TestKeywordValidateImageContent)
from .test_content_location_keywords \
    import (TestKeywordLocateTextCoordinates, TestKeywordLocateMultipleTextCoordinates, TestKeywordLocateTextBounds,
    TestKeywordLocateMultipleTextBounds)

__all__ = ["TestKeywordApplyErosionToImage",
            "TestKeywordApplyErosionToImage",
            "TestKeywordAppyDilationToImage",
            "TestKeywordAppyGradientToImage",
            "TestKeywordApplyOpeningToImage",
            "TestKeywordAppyClosingToImage",
            "TestKeywordAppyTopHatToImage",
            "TestKeywordApplyBlackHatToImage",
            "TestKeywordGetBinaryImage",
            "TestKeywordGetGrayScaleImage",
            "TestKeywordGetToZeroImage",
            "TestKeywordGetTruncImage",
            "TestKeywordCovertImageToHSV",
            "TestKeywordMaskColour",
            "TestKeywordMaskColours",
            "TestKeywordApplyAveragingBlurToImage",
            "TestKeywordApplyGaussianBlurToImage",
            "TestKeywordApplyMedianFilteringToImage",
            "TestKeywordAppyFilter2DToImage",
            "TestKeywordReadImage",
            "TestKeywordSaveImage",
            "TestKeywordValidateImageContent",
            "TestKeywordLocateTextCoordinates",
            "TestKeywordLocateMultipleTextCoordinates",
            "TestKeywordLocateTextBounds",
            "TestKeywordLocateMultipleTextBounds"]
