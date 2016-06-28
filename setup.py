#!/usr/bin/env python

from setuptools import setup, find_packages


setup(
    name="fortnox",
    version="0.0.1",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[],
    tests_require=[],
    entry_points={
        'console_scripts':[]
    },
    license='MIT',
    description='Python library for interacting with Fortnox via thier REST API.',
    long_description=open("README.md").read(),
    maintainer='Philip Johansson',
    maintainer_email='philip.johansson@hotmail.se',
    author='Philip Johansson',
    author_email='philip.johansson@hotmail.se',
    provides=["fortnox"],
    url='https://github.com/phille97/python-fortnox',
    bugtrack_url='https://github.com/phille97/python-fortnox/issues',
    home_page='https://github.com/phille97/python-fortnox',
    keywords='fortnox rest api',

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Other Environment',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
