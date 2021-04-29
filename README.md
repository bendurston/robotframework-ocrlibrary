# Robot Framework OCR Library
A robot framework library that is capable of processing images, validating text, and locating specified text by coordinates within images.

[![Build](https://github.com/bendurston/robotframework-ocrlibrary/actions/workflows/build.yml/badge.svg)](https://github.com/bendurston/robotframework-ocrlibrary/actions/workflows/build.yml)

## Keyword Documentation
You can find the [keyword documentation here](https://bendurston.github.io/OCRLibrary.html).


## Installation and Usage
- OCRLibrary can be run on Python 3.6, 3.7, 3.8, and 3.9.
- To install, run `pip install robotframework-OCRLibrary`

### Dependencies
OCRLibrary uses two dependencies, opencv-python and pytesseract.
Pytesseract has more dependencies. Depending on your OS and current packages, this may not work after a pip install.

#### OpenCV Python
To install opencv-python, run `pip install opencv-python`.
Please see [opencv-python's installation and usage section](https://github.com/opencv/opencv-python#installation-and-usage) if this does not work.

#### Pytesseract
To install pytesseract, run `pip install pytesseract`.
Please see [pytesseracts installation section](https://github.com/madmaze/pytesseract#installation) if this
does not work.

Pytesseract requires Google's Tesseract OCR software. For installation of tesseract for Linux, MacOS or Windows please see [the following installation guide](https://tesseract-ocr.github.io/tessdoc/Installation.html).

### Usage
Once OCRLibrary is installed, along with its dependencies, add `Library    OCRLibrary` to your robot file to use.

## Custom configurations for reading images.
You can add any combination of the following to the `pyt_conf` string argument.

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
Please see any of the following links for more information on image processing using OpenCV:
- [Changing Colour Spaces](https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_colorspaces/py_colorspaces.html#converting-colorspaces)
- [Thresholding](https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_thresholding/py_thresholding.html#thresholding)
- [Smoothing Images](https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_filtering/py_filtering.html#filtering)
- [Morphological Transformations](https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_morphological_ops/py_morphological_ops.html#morphological-ops)

## Contributing
When contributing please adhere to the following.

To start off, if you find a bug, please submit an issue.
If you want to fix something or improve upon something, fork the repo, and create a new branch.
Once you have made the changes and have written unit tests or updated the regression tests (please use pythons Unittest when testing), make a pull request.
