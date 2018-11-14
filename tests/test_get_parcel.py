""" File to handles tests for get single parcel endpoint """
import unittest
from sendit import app

class TestSingleParcel(unittest.TestCase):
    """ Test Class for single parcel endpoint"""

    def setUp(self):
        """ set up method for test cases."""
        self.app = app.test_client()

    def test_get_single_parcel(self):
        """ Test method to test index endpoint of the app."""
        response = self.app.get('/api/v1/parcels')
        self.assertEqual(response.status_code, 200)