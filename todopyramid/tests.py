import unittest
from pyramid import testing
from pyramid.i18n import TranslationStringFactory

_ = TranslationStringFactory('todopyramid')


class ViewTests(unittest.TestCase):

    def setUp(self):
        testing.setUp()

    def tearDown(self):
        testing.tearDown()

    def test_my_view(self):
        from todopyramid.views import index
        request = testing.DummyRequest()
        response = index(request)
        self.assertEqual(response['project'], 'todopyramid')
