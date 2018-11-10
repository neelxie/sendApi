""" File for initial unit tests."""
import unittest
from flask_restful import Api
from sendit import create_app
from sendit.routes import api

app = create_app()

class TestApi(unittest.TestCase):
    """ Class to test api."""

    def setUp(self):
        """ Set up test client."""
        self.app = app.test_client()

    def test_index(self):
        """ Test index resource."""
        with self.app as derek:
            resp = derek.get('http://127.0.0.1:5000/api/v1/')
            self.assertEqual(
                resp.data, b'{"message": "This is my Index Page."}\n')

    def test_api(self):
        """ Test api instance."""
        self.assertIsInstance(api, Api)

    def test_app(self):
        """ Test app instance."""
        self.assertTrue(app is not None)
