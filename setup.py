#!/usr/bin/env python

from distutils.core import setup


setup(
    name='Django FogBugz Gadget',
    version='1.0',
    description='A small Django app which allows your users to submit bugs to FogBugz.',
    author='Sanders New Media',
    author_email='hello@sandersnewmedia.com',
    url='http://github.com/sandersnewmedia/fogbugz',
    packages=['django_fogbugz_gadget'],
    package_data={
        'django_fogbugz_gadget':[ 
            'templates/django_fogbugz_gadget/submit_bug.html',
            'static/django_fogbugz_gadget/css/style.css',
            'static/django_fogbugz_gadget/js/jquery-1.6.min.js',
            'static/django_fogbugz_gadget/js/script.js',
        ]
    },
    requires=['Django (>=1.3)','pyquery (>=0.6.1)'],
    license='MIT',
    classifiers=[
        'Framework :: Django',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Customer Service',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Bug Tracking',
    ],
)
