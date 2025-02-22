from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = "0.0.2"
DESCRIPTION = "A library for TikTok audio processing"
LONG_DESCRIPTION = "sintok is a Python package designed to process and analyze audio from TikTok videos. It provides tools for extracting, enhancing, and modifying sound from TikTok content."

# Setting up
setup(
    name="sintok",
    version=VERSION,
    author="sintok Developers",
    author_email="support@sintok.com",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    keywords=["tiktok", "audio", "sound processing", "music analysis", "speech enhancement"],
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "Topic :: Multimedia :: Sound/Audio :: Analysis",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[],
)
