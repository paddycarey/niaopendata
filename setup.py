#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


setup(
    name='niaopendata',
    version='0.0.1',
    description='niaopendata is a Python client for the Northern Ireland Assembly Open Data API',
    long_description=open('README.rst').read(),
    author='Patrick Carey',
    author_email='paddy@wackwack.co.uk',
    url='https://github.com/paddycarey/niaopendata',
    packages=['niaopendata'],
    package_dir={'niaopendata': 'niaopendata'},
    include_package_data=True,
    install_requires=['requests >= 2', 'xmltodict >= 0.9'],
    license="MIT",
    zip_safe=False,
    keywords='NI Northern Ireland Assembly Open Data',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
    ],
)
