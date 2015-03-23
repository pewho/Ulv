#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
from setuptools import setup, find_packages
import ulv
 
setup(
    name='ulv',
    version=ulv.__version__,
    packages=find_packages(),
    author="Pewho Lewok",
    author_email="pewhoo@gmail.com",
    description="csv parser lib wrapper",
    long_description=open('README.md').read(),
    include_package_data=True,
    url='https://github.com/pewho/Ulv',
    classifiers=[
        "Programming Language :: Python",
        "Development Status :: 1 - Planning",
        "License :: OSI Approved",
        "Natural Language :: French",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Topic :: Parser",
    ],
    license="MIT"
)