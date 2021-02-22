# Robot Framework OCR Library
A robot framework library that is capable of processing images, validating text, and locating specified text by coordinates within images.

## Custom configurations for reading images.
You can add any combination of these configurations in a string to use as an argument `config=` in `pytesseract.image_to_string()`.

### Page segmentation modes
Page segmentation modes provide different ways a poage of text can be analyzed. Here is a list of supported page segmentation modes:
+ 0     Origentation and script detection only.
+ 1     Automatic page segmentation with OSD.
+ 2     Automatic page segmentation, but no OSD, or OCR.
+ 3     Fully automatic page segmentation, but no OSD. (Default)
+ 4     Assume a single column o ftext of variable sizes.
+ 5     Assume a single uniform block of vertically aligned text.
+ 6     Assume a single uniform block of text.
+ 7     Treat the image as a single text line.
+ 8     Treat the image as a single word.
+ 9     Treat the image as a single word in a circle.
+ 10    Treat the image as a single character.
+ 11    Sparse text. Find as muuch text as possible in no particular order.
+ 12    Sparse text with OSD.
+ 13    Raw line. Treat the image as a single text line, by passing hacks that are Tesseract-specific.

To change your page segmentation mode, add `--psm <mode>` to your custom configuration string. 

### OCR Engine Modes
Select the OCR engine modes to be used by pytesseract:
+ 0    Legacy engine only.
+ 1    Neural nets LSTM engine only.
+ 2    Legacy + LSTM engines.
+ 3    Default, based on what is available.

To change your ocr engine mode, add `--oem <mode>` to your custom configuration string.

### Whitelisting Characters
This configuration specifies which characters to detect.
Add the characters you want to detect to the string: `c- tessedit_char_whitelist=`.
An example to only detect lowercase letters: `c- tessedit_char_whitelist=abcdefghijklmnopqrstuvwxyz`

### Blacklisting Characters
Opposite to whitelisting characters, this configurations lets you specify which characters to not detect.
Add the characters you want to not detect to the string: `c- tessedit_char_blacklist=`
An example to not detect special characters: `c- tessedit_char_whitelist=!@#$%^&*()`

## Image Processing in OpenCV
Please note this library will not contain all image preprocessing available by OpenCV. 
This library assumes the images are screenshots from devices, so images would be clear and do not require 
processing such as geometric transformations.

### Changing Colour Spaces
There are currently two functions available that will change an images colour: 
+ `convert_BGR_to_HSV(img, colour)` extracts the given colour or colours from the BGR image
+ `convert_BGR_to_GRAY(img)` converts a BGR image to a gray scale image

### Image Thresholding
[Image Thresholding Reference From OpenCV](https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_thresholding/py_thresholding.html#thresholding)

Image thresholding is used to convert **gray scale images** to **binary images**. The gray scale image is processed
and each pixel is checked, if the pixel is greater than the threshold value it is assigned a 1, else it is assigned a 0.
1 and 0 represent white and black but depends on the thresholding function to determine which is which. 
Note: these functions will mostlikely fail if the image argument is not gray scale.

#### Image Thresholding without OTSU
All of the following functions take similar arguments and return similar values.
The first argument is the gray scale image, the second argument is the threshold value which is used to classify the pixel values.
The second argument is the max value which represents the value to be given if the pixel value is more than (sometimes less than) the
threshold value. The fourth argument is the different image thresholding style.
Available Functions:
+ `thresholding_binary()`
+ `thresholding_binary_inv()`
+ `thresholding_thrunc()`
+ `thresholding_tozero()`
+ `thresholding_tozero_inv()`
Here is a reference of the results of the above functions:

![alt text](https://github.com/bendurston/robotframework-ocrlibrary/blob/main/docs/images/image_thresholding_without_otsu.png)
