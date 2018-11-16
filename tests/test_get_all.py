""" File to handles tests for get all parcels endpoint """
import unittest
from sendit import app
from sendit.models.parcel_model import authenticate
from sendit.models.parcel_model import valid_string
from sendit.models.parcel_model import my_str_len

class TestAllParcels(unittest.TestCase):
    """ Test Class for get all Parcels endpoint"""

    def setUp(self):
        """ set up method for test cases."""
        self.app = app.test_client()

    def test_authenticate_function(self):
        """ test helper function authenticate in parcel view."""
        self.assertEqual(authenticate("ssd", 1, "ssss"), True)

    def test_valid_string_function(self):
        """ test authenticate function."""
        self.assertEqual(valid_string("s", " ", "2"), True)

    def test_helper_funtion_two(self):
        """ test helper function my_str_len in parcel view."""
        self.assertEqual(my_str_len("s", "", "2"), True)

    def test_my_str_second(self):
        """ test helper function my_str_len in parcel view."""
        self.assertEqual(my_str_len("s", "lk", "2"), True)

    def test_index_endpoint(self):
        """ Test method to test index endpoint of the app."""
        response = self.app.get('/api/v1/')
        self.assertEqual(response.status_code, 200)

    def test_get_all_parcels(self):
        """ Test method to test index endpoint of the app."""
        response = self.app.get('/api/v1/parcels')
        self.assertEqual(response.status_code, 200)