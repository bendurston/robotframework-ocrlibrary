# Robot Framework OCR Library
A robot framework library that is capable of processing images, validating text, and locating specified text by coordinates within images.

[![Build](https://github.com/bendurston/robotframework-ocrlibrary/actions/workflows/build.yml/badge.svg)](https://github.com/bendurston/robotframework-ocrlibrary/actions/workflows/build.yml) [![Version](https://img.shields.io/badge/Version-2.0.0-blue)](https://img.shields.io/badge/Version-2.0.0-blue) [![Licence](https://img.shields.io/badge/Licence-Apache%202.0-blue)](https://img.shields.io/badge/Licence-Apache%202.0-blue) [![Downloads](https://static.pepy.tech/personalized-badge/robotframework-ocrlibrary?period=total&units=international_system&left_color=grey&right_color=blue&left_text=Downloads)](https://pepy.tech/project/robotframework-ocrlibrary)

## Keyword Documentation
You can find the [keyword documentation here](https://bendurston.github.io/OCRLibrary.html).

## Installation and Usage
- OCRLibrary can be run on Python 3.6, 3.7, 3.8, and 3.9.
- To install, run `pip install robotframework-ocrlibrary`

### Dependencies
OCRLibrary uses two dependencies downloadable through the pip package manager, opencv-python and pytesseract. As well as Tesseract OCR.

#### Tesseract
OCRLibrary requires Google's Tesseract OCR software. 
##### Linux
To install tesseract on Linux, run `sudo apt install tesseract-ocr`

##### MacOS
To install tesseract on MacOS, run `brew install tesseract`

##### Windows
To install tesseract on Windows, download one of the installers from [UB-Mannhiem/tesseract](https://github.com/UB-Mannheim/tesseract/wiki)
Once installed add the path to the tesseract folder (ex: C:\User\Program/ Files\tesseract) to your environment variables.

##### Download verification
Run the command `tesseract -v` to confirm that tesseract was downloaded successfully.

##### More installation instructions
For more detailed installation instructions of tesseract please see [the following installation guide](https://tesseract-ocr.github.io/tessdoc/Installation.html).

#### OpenCV Python
To install opencv-python, run `pip install opencv-python`.
Please see [opencv-python's installation and usage section](https://github.com/opencv/opencv-python#installation-and-usage) for more information.

#### Pytesseract
To install pytesseract, run `pip install pytesseract`.
Please see [pytesseracts installation section](https://github.com/madmaze/pytesseract#installation) for more information.

### Usage
Once OCRLibrary is installed, along with its dependencies, add `Library    OCRLibrary` to your robot file to use.

#### Installing Languages
You can see which languages are available by running `tesseract --list-langs`. You can do the following to install more languages. [Here is a list of supported languages, language codes and tessdata files](https://tesseract-ocr.github.io/tessdoc/Data-Files#data-files-for-version-400-november-29-2016).

##### Linux
To install all languages on Linux, run `sudo apt install tesseract-ocr-all`.

To install a specific language on Linux, run `sudo apt install tesseract-ocr-<lang>`. Where `<lang>` is the language code.

##### MacOS
To install all language on MacOS, run `brew install tesseract-lang`.

##### Windows
To download a language on Windows, you must install the trained model for your desired language. [This repo has many language models to download](https://github.com/tesseract-ocr/tessdata/). Here are [more tessdata files](https://tesseract-ocr.github.io/tessdoc/Data-Files#data-files-for-version-400-november-29-2016). Once downloaded, place the trained model in the tessdata directory (i.e. where the tesseract.exe is located).

### Custom configurations for reading images
You can add any combination of the following to the `pyt_conf` string argument.

#### Page segmentation modes
Page segmentation modes provide different ways a page of text can be analyzed. Here is a list of supported page segmentation modes:

| Mode | Description |
|------|-------------|
| 0    | Origentation and script detection only. |
| 1    | Automatic page segmentation with OSD.   |
| 2    | Automatic page segmentation, but no OSD, or OCR.    |
| 3    | Fully automatic page segmentation, but no OSD. (Default)    |
| 4    | Assume a single column of text of variable sizes.   |
| 5    | Assume a single uniform block of vertically aligned text.   |
| 6    | Assume a single uniform block of text.  |
| 7    | Treat the image as a single text line.  |
| 8    | Treat the image as a single word.   |
| 9    | Treat the image as a single word in a circle.   |
| 10   | Treat the image as a single character.  |
| 11   | Sparse text. Find as muuch text as possible in no particular order. |
| 12   | Sparse text with OSD.   |
| 13   | Raw line. Treat the image as a single text line, by passing hacks that are Tesseract-specific.  |

To change your page segmentation mode, add `--psm <mode>` to your custom configuration string. 

#### OCR Engine Modes
Select the OCR engine modes to be used by pytesseract:
| Mode | Description |
|------|-------------|
| 0    | Legacy engine only.  |
| 1    | Neural nets LSTM engine only.    |
| 2    | Legacy + LSTM engines.   |
| 3    | Default, based on what is available. |

To change your ocr engine mode, add `--oem <mode>` to your custom configuration string.

#### Whitelisting Characters
This configuration specifies which characters to detect.
Add the characters you want to detect to the string: `-c tessedit_char_whitelist=`.
An example to only detect lowercase letters: `-c tessedit_char_whitelist=abcdefghijklmnopqrstuvwxyz`

#### Blacklisting Characters
Opposite to whitelisting characters, this configurations lets you specify which characters to not detect.
Add the characters you want to not detect to the string: `-c tessedit_char_blacklist=`
An example to not detect special characters: `-c tessedit_char_whitelist=!@#$%^&*()`

#### Other Configurations
[Visit this site](https://muthu.co/all-tesseract-ocr-options/) for a complete list of Tesseract configuration parameters.

##### Example of custom configuration string usage
In this example, the content will be returned from the processed image using page segmentation mode 6 and it will ignore all numbers.
`${content}=    Get Image Content   ${processed_image}  --psm 6 -c tessedit_char_blacklist=0123456789`

## Image processing using OpenCV
Please see any of the following links for more information on image processing using OpenCV:
- [Changing Colour Spaces](https://docs.opencv.org/4.5.2/df/d9d/tutorial_py_colorspaces.html)
- [Thresholding](https://docs.opencv.org/4.5.2/d7/d4d/tutorial_py_thresholding.html)
- [Smoothing Images](https://docs.opencv.org/4.5.2/d4/d13/tutorial_py_filtering.html)
- [Morphological Transformations](https://docs.opencv.org/4.5.2/d9/d61/tutorial_py_morphological_ops.html)

## Contributing
Thank you for thinking of contributing to the robotframework-ocrlibrary!

When contributing please adhere to the following.

If you find a bug, please submit an issue.

If you want to fix something or improve upon something, fork the repo, and create a new branch.
Once you have made the changes and have written unit tests or updated the regression tests (please use pythons Unittest when testing), make a pull request.

Please put the files in the appropriate directories with the appropriate names. The image processing features fall under any of [these categories](https://docs.opencv.org/4.5.2/d2/d96/tutorial_py_table_of_contents_imgproc.html), please name the file to resemble that category (see [existing files](https://github.com/bendurston/robotframework-ocrlibrary/tree/main/OCRLibrary/utils/imageprocessing/imagetransformation) for examples), or add to an existing file.
