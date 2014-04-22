import unittest
from pyramid import testing
from pyramid.i18n import TranslationStringFactory
from pymongo import MongoClient

_ = TranslationStringFactory('todopyramid')


class ViewTests(unittest.TestCase):

    def setUp(self):
        self.request = testing.DummyRequest()
        self.db = MongoClient().todopyramid
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
