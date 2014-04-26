import unittest
from pyramid import testing
from pyramid.i18n import TranslationStringFactory
from pymongo import MongoClient

_ = TranslationStringFactory('todopyramid')


class BaseCaseTest(unittest.TestCase):
    def setUp(self):
        self.request = testing.DummyRequest()
        self.db = MongoClient().test_todopyramid
        self.request.db = self.db
        testing.setUp(request=self.request)

    def tearDown(self):
        testing.tearDown()

class ViewTests(BaseCaseTest):

    def setUp(self):
        BaseCaseTest.setUp(self)

    def make_one(self):
        todo = {'todo_name': 'Test', 'description': 'teste'}
        return self.db.todolist.insert(todo)

    def tearDown(self):
        BaseCaseTest.tearDown(self)
        self.db.todolist.remove()

    def test_my_index(self):
        from todopyramid.views import index
        response = index(self.request)
        self.assertEqual(response['todolist'], list(self.db.todolist.find()))

    def test_my_new_todo(self):
        from todopyramid.views import new
        resp = new(self.request)
        self.assertEqual(resp['todo'], {})


class FunctionalTest(BaseCaseTest):
    def setUp(self):
        from pyramid.paster import bootstrap
        app = bootstrap('development.ini')
        from webtest import TestApp
        self.client = TestApp(app)
        BaseCaseTest.setUp(self)

    def tearDown(self):
        self.db.todolist.remove()
        testing.tearDown()


    def test_index_status(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_int, 200)

    def test_new_status(self):
        resp = self.client.get('/new')
        self.assertEqual(resp.status_int, 200)
