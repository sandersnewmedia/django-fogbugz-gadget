from django.conf import settings 
from django.core import exceptions
import unittest
import utils

class TestFogBugzApp(unittest.TestCase):
    def setUp(self):
        settings.FOG_API_ROOT = 'http://www.fake.com/fakeness?'
        settings.FOG_EMAIL = 'fake@fake.com'
        settings.FOG_PASSWORD = '1234'
        settings.FOG_PROJECT = 'Fakeness'
        settings.FOG_PRIMARY_CONTACT = 'John Smith'

        self.cleaned_data = {'priority': u'3', 'message': u'TEST MESSAGE', 'title': u'TEST'}

    def test_configure(self):
        utils._configure()
        #self.assertRaises(exceptions.ImproperlyConfigured, utils._configure)
        pass

    def test_logon(self):
        self.assertRaises(utils.FogBugzError, utils._logon)

    def test_get_priorities(self):
        self.assertRaises(utils.FogBugzError, utils.get_priorities)

    def test_submit_ticket(self):
        self.assertRaises(utils.FogBugzError, utils.submit_ticket, self.cleaned_data)

if __name__ == '__main__':
    unittest.main()
