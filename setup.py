#!/usr/bin/python
# -*- coding: utf-8 -*-

# This file is part of easyNav-pi-voice.
# https://github.com/easyNav/easyNav-pi-voice

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2014 Joel Tong me@joeltong.org


from setuptools import setup, find_packages
from easyNav_pi_voice import __version__

tests_require = [
    'mock',
    'nose',
    'coverage',
    'yanc',
    'preggy',
    'tox',
    'ipdb',
    'coveralls',
    'sphinx',
]

setup(
    name='easyNav-pi-voice',
    version=__version__,
    description='Voice daemon for easyNav',
    long_description='''
Voice daemon for easyNav
''',
    keywords='easyNav voice daemon ',
    author='Joel Tong',
    author_email='me@joeltong.org',
    url='https://github.com/easyNav/easyNav-pi-voice',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: Unix',
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: Implementation :: PyPy",
        'Operating System :: OS Independent',
    ],
    packages=find_packages(),
    include_package_data=False,
    install_requires=[
        # add your dependencies here
        # remember to use 'package-name>=x.y.z,<x.y+1.0' notation (this way you get bugfixes)
        "easyNav-pi-dispatcher",
        "smokesignal>=0.5"
    ],
    dependency_links=[
        "git+ssh://git@github.com:easyNav/easyNav-pi-dispatcher.git"
    ],
    extras_require={
        'tests': tests_require,
    },
    entry_points={
        'console_scripts': [
            # add cli scripts here in this form:
            'easyNav-pi-voice=easyNav_pi_voice.voiceDaemon:runMain'
            # 'easyNav-pi-voice=easyNav_pi_voice.cli:main',
        ],
    },
)
