#!/usr/bin/env python

from setuptools import setup

setup(
    name='selenose-screenshots',
    version='0.0.1',
    author='Maikel Wever',
    author_email='maikelwever@gmail.com',
    description='Nose plugin to take selenium screenshot on webdriver exceptions',
    packages=['selenose_screenshots'],
    entry_points={
        'nose.plugins.0.10': [
            'selenose-screenshots = selenose_screenshots:SeleNoseScreenshots'
        ]
    },
    url='http://github.com/maikelwever/selenose-screenshots',
    license='GNU General Public License 3.0 (GPL 3.0)',
    keywords='nose selenium selenose screenshot',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License 3.0 (GPL 3.0)',
        'Operating System :: POSIX',
        'Topic :: Software Development :: Quality Assurance',
        'Topic :: Software Development :: Testing',
        'Topic :: Utilities',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5'],
    install_requires=['selenose'],
)
