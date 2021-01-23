# Robot Framework OCR Library
A robot framework library that is capable of validating text in images, and locating specified text by coordinates within images.

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
