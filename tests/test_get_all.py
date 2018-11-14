""" File to handles tests for get all parcels endpoint """
import unittest
from sendit import app

class TestAllParcels(unittest.TestCase):
    """ Test Class for get all Parcels endpoint"""

    def setUp(self):
        """ set up method for test cases."""
        self.app = app.test_client()

    def test_get_all_parcels(self):
        """ Test method to test index endpoint of the app."""
        response = self.app.get('/api/v1/parcels')
        self.assertEqual(response.status_code, 200)