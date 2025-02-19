from setuptools import setup, find_packages
import os

# Read the contents of the README.md file
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="PyForShort",
    version="1.0.1",
    description="A package for creating shortcuts",
    long_description=long_description,
    long_description_content_type="text/markdown",  # Specify markdown format for README.md
    author="Roshan D Roy",
    author_email="roshandeepuroy@gmail.com",
    url="https://github.com/R-D-R248/PyForShort",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[],
    python_requires=">=3.6",
)
