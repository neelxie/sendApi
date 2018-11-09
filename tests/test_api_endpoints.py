import unittest
from sendit import app

class Test_endpoints(unittest.TestCase):
    """ Test class for end points."""

    def setUp(self):
        """ Set up test client."""
        self.app = app.test_client()

    def test_get_one_user(self):
        """ Correct Test method to get one user."""
        with self.app as derek:
            resp = derek.get('/api/v1/users/1')
            self.assertEqual(resp.status_code, 200)

    def test_get_wrong_user(self):
        """ Test method to get non-existant user."""
        with self.app as derek:
            resp = derek.get('/api/v1/users/9')
            self.assertEqual(resp.data, b'{"error": "User not found"}\n')
            self.assertEqual(resp.status_code, 400)

    # def test_get_user_empty_list(self):
        """ Correct Test method to get one user."""
        # with self.app as derek:
            # resp = derek.get('/api/v1/users/1')
            # resp.data["users_record.users_list"]
            # self.assertEqual(resp.data, b'{"error": "Users record empty."}\n')
            # self.assertEqual(resp.status_code, 400)

    # def test_get_all_users_empty_list(self):
        """ Correct Test method to get one user."""
        # with self.app as derek:
            # resp = derek.get('/api/v1/users')
            # self.assertEqual(resp.data, b'{"error": "Users record empty."}\n')
            # self.assertEqual(resp.status_code, 400)

    def test_get_all_users(self):
        """ Correct Test method to get all users."""
        with self.app as derek:
            resp = derek.get('/api/v1/users')
            self.assertEqual(resp.status_code, 200)