from django.conf import settings
from django.core import exceptions
from django.core.cache import cache
from pyquery import PyQuery as pq
from urllib2 import HTTPError, URLError, Request, urlopen, quote
from urllib import urlencode


conf = {}

class GadgetError(Exception):
    def __init__(self, msg):
        self.msg = 'FogBugz Gadget says... %s' % msg

    def __str__(self):
        return repr(self.msg)

def _configure():
    """
    Checks Django settings for necessary configuration variables.
    """
    try:
        conf['api_root'] = settings.FOG_API_ROOT
        conf['email'] = settings.FOG_EMAIL
        conf['password'] = settings.FOG_PASSWORD
        conf['project'] = settings.FOG_PROJECT
        conf['primary_contact'] = settings.FOG_PRIMARY_CONTACT
    except AttributeError:
        raise exceptions.ImproperlyConfigured

def _send(query):
    # for some reason we have to grab the XML doc manually before passing to pyquery;
    # the token isn't grabbed otherwise
    try:
        request = Request(conf['api_root'], urlencode(query.items()))
        xml = pq(urlopen(request).read())
        return xml
    except HTTPError, e:
        raise GadgetError('Error code: %s (check app settings)' % e.code)
    except URLError, e:
        raise GadgetError('Failed to reach server: %s (check app settings)' % e.reason)

def _logon():
    reply = _send({
        'cmd': 'logon',
        'email': conf['email'],
        'password': conf['password'] })

    if reply('error'):
        raise GadgetError(reply)

    token = reply('token').html()

    if token is None:
        raise GadgetError('No token provided, login unsuccessful')

    return token

def _logoff(token):
    _send({
        'token=': token,
        'cmd': 'logoff' })

def get_priorities():
    """
    Returns priority values for use in a choice field.
    Values are pulled from FogBugz if not found in cache.
    """
    if cache.get('priorities') is not None:
        return cache.get('priorities')

    if not conf:
        _configure()

    token = _logon()
    reply = _send({
        'token': token,
        'cmd': 'listPriorities' })

    if reply('error'):
        raise GadgetError(reply)

    choices, initial = [], None

    for elem in reply('priority'):
        val = pq(elem).find('ixPriority').html()
        name = val + ' - ' + pq(elem).find('sPriority').html()

        choices.append((val, name))

        if pq(elem).find('fDefault').html() == 'true':
            initial = val

    _logoff(token)

    cache.set('priorities', (choices, initial))
    return choices, initial

def submit_ticket(data):
    """
    Returns a case number upon successfull submission of a ticket.
    Cleaned form data is expected.
    """
    if not conf:
        _configure()

    token = _logon()

    reply = _send({
        'cmd': 'new',
        'token': token,
        'sProject': conf['project'],
        'sPrimary': conf['primary_contact'],
        'sTitle': data['title'],
        'ixPriority': data['priority'],
        'sEvent': data['message'] })

    case = reply('case').attr('ixBug')

    if reply('error'):
        raise GadgetError(reply)

    _logoff(token)
    return case
