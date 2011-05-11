#!/usr/bin/env python

from distutils.core import setup

setup(
    name='django-fogbugz-gadget',
    version='0.1',
    description='A small Django app which allows your users to submit cases to FogBugz directly from your site.',
    author='Sanders New Media',
    author_email='hello@sandersnewmedia.com',
    url='http://github.com/sandersnewmedia/django-fogbugz-gadget',
    download_url='https://github.com/downloads/sandersnewmedia/django-fogbugz-gadget/django-fogbugz-gadget-0.1.tar.gz',
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
