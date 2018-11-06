import unittest
from flask import Flask
from ..run import app, api, Api

class TestApi(unittest.TestCase):
    """ Class to test api."""
    def setUp(self):
        """ Set up test client."""
        self.app = app.test_client()

    def test_index(self):
        """ Test index resource."""
        with self.app as derek:
            resp = derek.get('/')
            self.assertEqual(resp.data, b'{"message": "This is my Index Page."}\n')

    def test_api(self):
        """ Test api instance."""
        self.assertIsInstance(api, Api)

    def test_app(self):
        """ Test app instance."""
        self.assertTrue(app is not None)
