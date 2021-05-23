*** Settings ***
Library    OCRLibrary

*** Keywords ***
###
Using Read Image
    [Arguments]     ${path}
    ${read_image}=    Read Image      ${path} 
    [Return]   ${read_image}

Using Save Image
    [Arguments]     ${read_image}
    Save Image     /home/usr/Desktop/someName.png      ${read_image}
###
###
Using Apply Averaging Blur To Image
    [Arguments]     ${processed_img}
    ${kernel}=    Create List    1    2
    ${img}=    Apply Averaging Blur To Image    ${processed_img}    ${kernel}
    [Return]    ${img}

Using Apply Black Hat To Image
    [Arguments]     ${processed_img}
    ${kernel}=    Create List    1    2
    ${img}=    Apply Black Hat To Image    ${processed_img}    ${kernel}    2     5
    [Return]    ${img}

Using Apply Closing To Image
    [Arguments]     ${processed_img}
    ${kernel}=    Create List    1    2
    ${img}=    Apply Closing To Image    ${processed_img}    ${kernel}
    [Return]    ${img}

Using Apply Dilation To Image
    [Arguments]     ${processed_img}
    ${kernel}=    Create List    1    2
    ${img}=    Apply Dilation To Image    ${processed_img}    ${kernel}   1   10
    [Return]    ${img}

Using Apply Erosion To Image
    [Arguments]     ${processed_img}
    ${kernel}=    Create List    1    2
    ${img}=    Apply Erosion To Image    ${processed_img}    ${kernel}
    [Return]    ${img}

Using Apply Opening To Image
    [Arguments]     ${processed_img}
    ${kernel}=    Create List    1    1
    ${img}=    Apply Opening To Image    ${processed_img}    ${kernel}
    [Return]    ${img}

Using Apply Top Hat To Image
    [Arguments]     ${processed_img}
    ${kernel}=    Create List    5    5
    ${img}=    Apply Top Hat To Image    ${processed_img}    ${kernel}
    [Return]    ${img}
###
###
Using Apply Gaussian Blur To Image
    [Arguments]     ${processed_img}
    ${kernel}=    Create List    1    5
    ${img}=    Apply Gaussian Blur To Image    ${processed_img}    ${kernel}
    [Return]    ${img}
###
###
Using Apply Median Filtering To Image
    [Arguments]     ${processed_img}
    ${img}=    Apply Median Filtering To Image    ${processed_img}    3
    [Return]    ${img}
###
###
Using Apply Filter2D To Image
    [Arguments]     ${processed_img}
    ${kernel}=    Create List    1    2
    ${img}=    Apply Filter2D To Image    ${processed_img}    ${kernel}    2   -5
    [Return]    ${img}
###
###
Using Get Image Content
    [Arguments]     ${processed_img}
    ${content}=    Get Image Content    ${processed_img}    --psm 6 --oem 1     eng
    [Return]    ${content}
###
###
Using Get Gray Scale Image
    [Arguments]     ${path}
    ${img}=     Get Gray Scale Image    ${path}
    [Return]    ${img}

Using Get Binary Image
    [Arguments]     ${path}
    ${img}=      Get Binary Image    ${path}     ${TRUE}     255    170    
    [Return]    ${img}[1]

Using Get To Zero Image
    [Arguments]     ${path}
    ${result}=      Get To Zero Image    ${path}     ${TRUE}
    ${optimal_threshold}=    Set Variable   ${result}[0]
    ${img}=     Set Variable     ${result}[1]
    [Return]    ${img}

Using Get Trunc Image
    [Arguments]     ${path}
    ${img}=      Get Trunc Image    ${path}     ${FALSE}     255    170    
    [Return]    ${img}
###
Using Convert Image To HSV
    [Arguments]     ${processed_img}
    ${hsv_img}=     Convert Image To HSV    ${processed_img}
    [Return]    ${hsv_img}
###
###
Using Validate Image Content
    [Arguments]     ${processed_img}
    Validate Image Content    ${processed_img}     Google      --psm 6 --oem 1     eng

Using Locate Multiple Text Bounds
    [Arguments]     ${processed_img}
    ${expected_Texts}=      Create List     Google
    ${result}=     Locate Multiple Text Bounds    ${processed_img}     ${expected_Texts}      --psm 6 --oem 1     eng
    [Return]    ${result}

Using Locate Multiple Text Coordinates
    [Arguments]     ${processed_img}
    ${expected_Texts}=      Create List     Google
    ${result}=     Locate Multiple Text Coordinates    ${processed_img}     ${expected_Texts}      --psm 6 --oem 1     eng
    [Return]    ${result}

Using Locate Text Bounds
    [Arguments]     ${processed_img}
    ${result}=     Locate Text Bounds   ${processed_img}     Google      --psm 6 --oem 1     eng
    [Return]    ${result}

Using Locate Text Coordinates
    [Arguments]     ${processed_img}
    ${result}=     Locate Text Coordinates    ${processed_img}     Google      --psm 6 --oem 1     eng
    [Return]    ${result}
###
###
Using Mask Colour
    [Arguments]     ${processed_img}
    ${lower}=   Create List     0   0   200
    ${upper}=   Create List     0   0   255
    ${masked_img}=      Mask Colour     ${processed_img}    ${lower}    ${upper}
    [Return]    ${masked_img}

Using Mask Colours
    [Arguments]     ${processed_img}
    ${lower1}=   Create List     0   0   200
    ${upper1}=   Create List     0   0   255
    ${lower2}=   Create List     0   200   0
    ${upper2}=   Create List     0   255   0
    ${masked_img}=      Mask Colours     ${processed_img}    ${lower1}    ${upper1}  ${lower2}   ${upper2}
    [Return]    ${masked_img}
###