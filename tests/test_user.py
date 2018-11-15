""" File to handles tests for get all users endpoint """
import unittest
import json
from sendit import app

class TestUser(unittest.TestCase):
    """ Test Class for get all Parcels endpoint"""

    def setUp(self):
        """ set up method for test cases."""
        self.app = app.test_client()

    def test_get_all_nonexistant_user_parcels(self):
        """ Test method to retrieve parcels of non existant user."""
        resp = self.app.get('/api/v1/users/9/parcels')
        self.assertEqual(resp.data, b'{"error":"User not found"}\n')
        self.assertEqual(resp.status_code, 200)

    def test_get_user_with_zero_parcels(self):
        """ Test method to retrieve a user with no parcel delivery orders yet."""
        resp = self.app.get('/api/v1/users/3/parcels')
        # self.assertEqual(resp.data, b'{"message": "User has no parcels yet."}\n')
        self.assertEqual(resp.status_code, 200)

    def test_correct_create_user(self):
        """ Test method to test post user endpoint of the app."""
        response = self.app.post('/api/v1/users', data=json.dumps(
            {"user_id": 1, "user_email": "derek@fbi.gov", "user_name": "Derek"}), content_type='application/json')
        self.assertEqual(response.status_code, 201)

    def test_fetch_app_users(self):
        """ Test method get every app user in list."""
        resp = self.app.get('/api/v1/users')
        self.assertEqual(resp.status_code, 200)

    def test_user_not_yet(self):
        """ Test user not yet added by id."""
        resp = self.app.get('/api/v1/users/9')
        self.assertEqual(resp.data, b'{"error":"No user by that ID in users list."}\n')

    def test_get_parcel_by_wrong_id(self):
        """ Test method to check wrong id."""
        resp = self.app.get('/api/v1/parcels/9')
        self.assertEqual(resp.data, b'{"error":"No parcel by that ID in Parcels list."}\n')

    def test_authenticate_user_user_id_missing(self):
        """ Test method to test delivery order without a user id."""
        resp = self.app.post('/api/v1/users', data=json.dumps(
            { "user_name": "Derek"}), content_type='application/json')
        self.assertEqual(resp.data, b'{"error":"field missing."}\n')

    def test_get_user_record_given_an_id(self):
        """ Test method to check whether user is in list given its id."""
        resp = self.app.get('/api/v1/users/2')
        self.assertEqual(resp.status_code, 200)

    def test_nonexistant_user(self):
        """ Test method to test non existant user by id."""
        resp = self.app.get(
            '/api/v1/users/<user_id>')
        self.assertEqual(resp.status_code, 404)

    def test_wrong_credentials_create_user(self):
        """ Test post user endpoint of the app."""
        response = self.app.post('/api/v1/users', data=json.dumps(
            {"user_id": 1, "user_email": "derek@fbi.gov", "user_name": ""}), content_type='application/json')
        self.assertEqual(response.data, b'{"Error":"User Email and User name must be of valid string."}\n')
