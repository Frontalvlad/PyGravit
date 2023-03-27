#!/usr/bin/env python

from io import open
from setuptools import setup

"""
:authors: Frontalvlad
:license: GNU General Public License v3.0
:copyright: (c) 2023 Frontalvlad
"""

version = '0.2.1'

with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='pygravit',
    version=version,

    author='Frontalvlad',
    author_email='frontalvlad@vk.com',

    description=(
        u'Module for managing accounts in GravitLauncher Database'
    ),
    long_description=long_description,
    long_description_content_type='text/markdown',

    url='https://github.com/Frontalvlad-GitHub/PyGravit',
    download_url='https://github.com/Frontalvlad-GitHub/PyGravit/releases/tag/v{}'.format(version),

    license='GNU General Public License v3.0',

    packages=['pygravit'],
    install_requires=['mysql-connector-python', 'bcrypt'],
)
