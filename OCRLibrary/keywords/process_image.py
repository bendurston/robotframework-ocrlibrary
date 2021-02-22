"""
Keywords to process any image.
"""

gray_image_processing_options = {
    0 : process_to_binary_image,
    1 : binary_inv,
    2 : binary_otsu,
    3 : binary_inv_otsu
    4 : tozero,
    5 : tozero_inv
    6 : tozero_otsu,
    7 : tozero_inv_otsu,
    8 : trunc,
    9 : trunc_otsu
}

colour_image_processing_options = {}

## write functions to do the processing as well as display the processing (i.e. save the processed image to a dir).