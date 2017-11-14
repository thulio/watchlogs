import unittest
from server.app import app


class TestApp(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def test_index(self):
        rv = self.app.get('/')

        self.assertEqual(200, rv.status_code)

    def test_health(self):
        rv = self.app.get('/_health')

        self.assertEqual(200, rv.status_code)
