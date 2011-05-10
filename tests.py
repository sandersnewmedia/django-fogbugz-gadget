from django.conf import settings 
from django.core import exceptions
import unittest
import utils

class TestExceptionHandling(unittest.TestCase):
    def setUp(self):

        # these bogus values should cause errors 
        settings.FOG_API_ROOT = 'http://1234.org'
        settings.FOG_EMAIL = 'fake@fake.com'

        # properly formatted test data
        self.cleaned_data = {'priority': u'3', 'message': u'TEST MESSAGE', 'title': u'TEST'}

    def test_get_priorities(self):
        self.assertRaises(utils.FogBugzError, utils.get_priorities)

    def test_submit_ticket(self):
        self.assertRaises(utils.FogBugzError, utils.submit_ticket, self.cleaned_data)

if __name__ == '__main__':
    unittest.main()
