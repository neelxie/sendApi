""" File to handles tests for post parcels endpoint """
import unittest
from sendit import app
import json

class TestPostParcel(unittest.TestCase):
    """ Test Class for post Parcels endpoint"""

    def setUp(self):
        """ set up method for test cases."""
        self.app = app.test_client()

    def test_post_parcels(self):
        """ Test method to test post endpoint of the app."""
        response = self.app.post('/api/v1/parcels', data=json.dumps(
            {"parcel_id": 1, "user_id": 2, "user_email": "derek@fbi.gov", "parcel_weight": 15, "pick_up_location": "kisasi",
            "destination": "Andela", "price_quote": 200, "status": "Transit"}),
             content_type='application/json')
        self.assertEqual(response.status_code, 201)