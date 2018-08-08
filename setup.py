#!/usr/bin/env python
# Gradiant's Biometrics Team <biometrics.support@gradiant.org>
# Copyright (C) 2017+ Gradiant, Vigo, Spain

from setuptools import setup, find_packages
from version import *

setup(
    name='bob.chapter.hobpad2.facepadprotocols',
    version=get_version(),
    description='Bob package for reproduce the experiments carried out in the chapter Challenges of Face Presentation Attack Detection in Real Scenarios in the Handbook of Biometric Anti-Spoofing 2',
    url='http://pypi.python.org/pypi/bob.chapter.hobpad2.facepadprotocols',
    license='BSD-3',
    author='Biometrics Team (Gradiant)',
    author_email='biometrics.support@gradiant.org',
    long_description=open('README.md').read(),
    keywords='chapter hobpad2 challenges pad real scenarios',

    # This line is required for any distutils based packaging.
    packages=find_packages(),
    include_package_data=True,
    zip_safe=True,

    install_requires=[
      "setuptools",
    ],

    entry_points={
        'console_scripts': [
            'reproducible_research.py = bob.chapter.hobpad2.facepadprotocols.scripts.reproducible_research:main',
            'download_scores.py = bob.chapter.hobpad2.facepadprotocols.scripts.download_scores:main',
            'retrieve_results.py = bob.chapter.hobpad2.facepadprotocols.scripts.retrieve_results:main',
        ],
    },
)
