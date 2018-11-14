""" File to handles tests for cancel parcels endpoint """
import unittest
from sendit import app
import json

class TestCancelParcel(unittest.TestCase):
    """ Test Class for cancel Parcels endpoint"""

    def setUp(self):
        """ set up method for test cases."""
        self.app = app.test_client()

    def test_cancel_parcel(self):
        """ Test method to cancel a delivery in transit."""
        resp = self.app.post('http://127.0.0.1:5000/api/v1/parcels', data=json.dumps(
                {"parcel_id": 1, "user_id": 2, "user_email": "derek@fbi.gov", "parcel_weight": 15, "pick_up_location": "kisasi",
        "destination": "Andela", "price_quote": 200, "status": "Transit"}), content_type='application/json')
        resp = self.app.put('http://127.0.0.1:5000/api/v1/parcels/1/cancel', data=json.dumps(
                {"parcel_id": 1, "user_id": 2, "user_email": "derek@fbi.gov", "parcel_weight": 15, "pick_up_location": "kisasi",
        "destination": "Andela", "price_quote": 200, "status": "Transit"}), content_type='application/json')
        self.assertEqual(resp.status_code, 200)