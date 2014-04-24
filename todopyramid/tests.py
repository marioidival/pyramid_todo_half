import unittest
from pyramid import testing
from pyramid.i18n import TranslationStringFactory
from pymongo import MongoClient

_ = TranslationStringFactory('todopyramid')


class ViewTests(unittest.TestCase):

    def setUp(self):
        self.request = testing.DummyRequest()
        self.db = MongoClient().test_todopyramid
        self.request.db = self.db
        testing.setUp(request=self.request)

    def tearDown(self):
        testing.tearDown()

    def test_my_index(self):
        from todopyramid.views import index
        response = index(self.request)
        self.assertEqual(response['todolist'], list(self.db.todolist.find()))

    def test_my_new_todo(self):
        from todopyramid.views import new
        resp = new(self.request)
        self.assertEqual(resp['todo'], {})


class FunctionalTest(unittest.TestCase):
    def setUp(self):
        from pyramid.paster import bootstrap
        app = bootstrap('development.ini')
        from webtest import TestApp
        self.client = TestApp(app['app'])

    def test_index_status(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_int, 200)

    def test_new_status(self):
        resp = self.client.get('/new')
        self.assertEqual(resp.status_int, 200)
