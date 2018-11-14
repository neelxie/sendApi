""" File to handles tests for get all users endpoint """
import unittest
from sendit import app

class TestUser(unittest.TestCase):
    """ Test Class for get all Parcels endpoint"""

    def setUp(self):
        """ set up method for test cases."""
        self.app = app.test_client()

    def test_get_all_user_by_id(self):
        """ Test method to retrieve a user with id 1."""
        resp = self.app.get('/api/v1/users/1')
        self.assertEqual(resp.status_code, 200)

    def test_get_all_nonexistant_user_parcels(self):
        """ Test method to retrieve parcels of non existant user."""
        resp = self.app.get('/api/v1/users/9/parcels')
        # self.assertEqual(resp.data, b'{"error": "User not found"}\n')
        self.assertEqual(resp.status_code, 200)

    def test_get_user_with_zero_parcels(self):
        """ Test method to retrieve a user with no parcel delivery orders yet."""
        resp = self.app.get('http://127.0.0.1:5000/api/v1/users/3/parcels')
        # self.assertEqual(resp.data, b'{"message": "User has no parcels yet."}\n')
        self.assertEqual(resp.status_code, 200)