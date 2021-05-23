import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setuptools.setup(
    name="robotframework-ocrlibrary",
    version="1.2.0",
    author="Ben Durston",
    author_email="bengdurston@gmail.com",
    description="A robot framework library that utilizes OpenCV image processing and pytesseract OCR.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bendurston/robotframework-ocrlibrary",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
