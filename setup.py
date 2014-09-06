#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys


try:
    from setuptools import setup
    from setuptools.command.test import test as TestCommand
except ImportError:
    from distutils.core import setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

#readme = open('README.rst').read()
#history = open('HISTORY.rst').read().replace('.. :changelog:', '')

#class PyTest(TestCommand):
#    def finalize_options(self):
#        TestCommand.finalize_options(self)
#        self.test_args = []
#        self.test_suite = True
#
#    def run_tests(self):
#        import pytest
#        errcode = pytest.main(self.test_args)
#        sys.exit(errcode)

setup(
    name='pydraft',
    version='0.1.0',
    description='A simple Flask powered static-blog generator',
    long_description='',#readme + '\n\n' + history,
    author='Wayne Werner',
    author_email='waynejwerner@gmail.com',
    url='https://github.com/waynew/pydraft',
    packages=[
        'pydraft',
    ],
    scripts=['scripts/pydraft'],
    #cmdclass={'test': PyTest},
    package_dir={'pydraft': 'pydraft'},
    include_package_data=True,
    install_requires=[
    ],
    license="BSD",
    zip_safe=False,
    keywords='draft flask blog publish',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        #"Programming Language :: Python :: 2",
        #'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
    ],
    #test_suite='tests',
    #tests_require=['pytest'],
)
