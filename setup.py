#!/usr/bin/env python
# coding:utf-8 vi:et:ts=2

# pyparadox distribute install.
# Copyright 2013 Grigory Petrov
# See LICENSE for details.

from setuptools import setup, find_packages


tests_require = [
]

setup(
    name='pyparadox',
    version='1.0.0',
    description="Simple tool that mirrors Paradox database as SQLite at runtime.",
    long_description=open('README.rst').read(),
    classifiers  = [
      ('Development Status :: 1 - Planning'),
      ('Environment :: Console'),
      ('Intended Audience :: Developers'),
      ('License :: OSI Approved :: GNU General Public License v3 (GPLv3)'),
      ('Natural Language :: English'),
      ('Operating System :: OS Independent'),
      ('Programming Language :: Python :: 2.7'),
      ('Topic :: Software Development :: Libraries'),
    ],
    extras_require={
        'tests': tests_require,
    },
    keywords=['paradox', 'sqlite'],
    author="Grigory Petrov",
    author_email="grigory.v.p@gmail.com",
    url='https://github.com/eyeofhell/pyparadox',
    license='GPLv3',
    packages=['pyparadox'],
    include_package_data=True,
    zip_safe=False,
)

