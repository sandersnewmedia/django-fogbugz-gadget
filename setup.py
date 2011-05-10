#!/usr/bin/env python

from distutils.core import setup

setup(
    name='Django FogBugz Gadget',
    version='1.0',
    description='A small Django app which allows your users to submit bugs to FogBugz.',
    author='Sanders New Media',
    author_email='hello@sandersnewmedia.com',
    url='http://github.com/sandersnewmedia/fogbugz',
    packages=['fogbugz_gadget'],
    requires=['Django 1.3','pyquery 0.6.1'],
    license='MIT',
    classifiers=[
        'Framework :: Django',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Customer Service',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Bug Tracking',
    ]
)

