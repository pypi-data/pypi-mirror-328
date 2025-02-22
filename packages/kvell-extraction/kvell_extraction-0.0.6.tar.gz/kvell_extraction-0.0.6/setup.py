"""
This is the setup.py file for the kvell_extraction package.
"""

import sys
import warnings
from typing import List

import setuptools

try:
    from get_pypi_latest_version import GetPyPiLatestVersion

    VERSION_NUM = "0.0.6"
    obtainer = GetPyPiLatestVersion()
    try:
        latest_version = obtainer("kvell_extraction")
        if latest_version:
            VERSION_NUM = obtainer.version_add_one(latest_version)
    except ValueError:
        warnings.warn("First time package submission")
except ImportError:
    VERSION_NUM = "0.0.6"
    warnings.warn("get_pypi_latest_version not available, using default version")


def get_readme():
    """
    Get the README.md file
    """
    readme_path = "README.md"
    with open(readme_path, "r", encoding="utf-8") as f:
        readme = f.read()
    return readme


setuptools.setup(
    name="kvell_extraction",
    version=VERSION_NUM,
    platforms="Any",
    description="Tools of extracting PDF content based on RapidOCR",
    long_description=get_readme(),
    long_description_content_type="text/markdown",
    author="KvelKrishna",
    packages=["kvell_extraction"],
    install_requires=[
        "PyMuPDF",
        "filetype",
        "rapidocr_onnxruntime",
        "spire.doc",
        "polars",
        "fastexcel",
        "python-pptx",
    ],
    entry_points={
        "console_scripts": ["kvell_extraction=kvell_extraction.main:main"],
    },
    extras_require={
        "onnxruntime": ["rapidocr_onnxruntime"],
    },
)
