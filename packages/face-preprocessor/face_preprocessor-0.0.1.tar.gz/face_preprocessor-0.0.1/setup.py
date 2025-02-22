"""
Setup configuration for face_preprocessor package.
"""
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="face_preprocessor",
    version="0.0.1",
    author="Kiran babu ",
    author_email="kiran2babu@gmail.com",
    description="A package for face detection and preprocessing in images",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kiranbab/face_preprocessor",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Scientific/Engineering :: Image Recognition",
    ],
    python_requires=">=3.7",
    install_requires=[
        "opencv-python>=4.5.0",
        "torch>=1.7.0",
        "numpy>=1.19.0",
        "retinaface>=0.0.5",
        "Pillow>=8.0.0",
        "tqdm>=4.45.0",
    ],
)