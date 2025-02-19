#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

from setuptools import find_packages
from setuptools import setup


def read(fname):
    with open(os.path.join(os.path.dirname(__file__), fname)) as f:
        return f.read().strip()


def readline(fname):
    with open(os.path.join(os.path.dirname(__file__), fname)) as f:
        return f.readline().strip()


PACKAGENAME: str = "kuat"

setup(
    name=PACKAGENAME,
    version=readline("version.txt"),
    author=["Emanuele Ballarin", "NVIDIA"],
    author_email="emanuele@ballarin.cc",
    url="https://github.com/emaballarin/kuat",
    description="Quaternions in PyTorch (part of NVIDIA Kaolin)",
    long_description=read("quaternions.md"),
    long_description_content_type="text/markdown",
    keywords=[
        "Deep Learning",
        "Machine Learning",
        "Computer Vision",
        "Differentiable Programming",
        "Mathematics",
        "Computer Graphics",
        "Robotics",
    ],
    license="Apache License, Version 2.0",
    packages=[
        package for package in find_packages() if package.startswith(PACKAGENAME)
    ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Environment :: Console",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
    ],
    python_requires=">=3.10",
    install_requires=[
        "torch>=2",
    ],
    include_package_data=True,
    zip_safe=True,
)
