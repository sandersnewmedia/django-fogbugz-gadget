[Django FogBugz Gadget](http://github.com/sandersnewmedia/django-fogbugz-gadget)
================================================================================

Overview
--------
Django FogBogz Gadget is a small Django app which allows your users to submit cases to FogBugz directly from your site.

Installation
------------
    $ sudo python setup.py install

Usage
-----
Django Settings

    INSTALLED_APPS = (
    ...
    'django_fogbugz_gadget'
    )

    TEMPLATE_CONTEXT_PROCESSORS = (
    ...
    'django_fogbugz_gadget.context_processors.forms',
    )

    # URL for submitting requests
    FOG_API_ROOT = 'https://example.django_fogbugz.com/api.asp?'

    FOG_PROJECT = 'Microsoft Windows'
    FOG_PRIMARY_CONTACT = 'Steve Balmer'

    # Submissions come from this user
    FOG_EMAIL = 'steve@example.com'
    FOG_PASSWORD = 'password'

Django URLs 

    urlpatterns = patterns('',
        ...
        (r'^submit_bug$', 'django_fogbugz_gadget.views.submit_bug'),
    )

Sample Template 

    <!DOCTYPE HTML>
    <html>
        <head>
            ...
            <link rel="stylesheet" href="{{ STATIC_URL }}django_fogbugz_gadget/css/style.css">
            <script src="{{ STATIC_URL }}django_fogbugz_gadget/js/jquery-1.6.min.js"></script>
            <script src="{{ STATIC_URL }}django_fogbugz_gadget/js/script.js"></script>
        </head>

        <body>
            ...
            {% include "django_fogbugz_gadget/submit_bug.html" %}
        </body>
    </html>

MORE INFO
---------
- Client's browser info is added automatically to all bug submissions
- Django FogBugz Gadget uses Django's cache framework
- Error messages are emailed to site admins
