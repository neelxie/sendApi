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

    def test_authenticate_parcel_user_id_missing(self):
        """ Test method to test delivery order without a user id."""
        resp = self.app.post('/api/v1/parcels', data=json.dumps(
            {"parcel_id": 1, "user_email": "derek@fbi.gov","parcel_weight": 15, "pick_up_location": "kisasi",
            "destination": "Andela", "price_quote": 200, "status": "Transit"}), content_type='application/json')
        self.assertEqual(
            resp.data, b'{"error":"field missing."}\n')


    def test_authenticate_parcel_user_id(self):
        """ Test method to test delivery order with user id as empty string."""
        resp = self.app.post('/api/v1/parcels', data=json.dumps(
            {"parcel_id": 1, "user_id": "", "user_email": "derek@fbi.gov", "parcel_weight": 15, "pick_up_location": "kisasi",
            "destination": "Andela", "price_quote": 200, "status": "Transit"}), content_type='application/json')
        self.assertEqual(
            resp.data, b'{"error":"User ID, Parcel weight and Price quote must be an int."}\n')


    def test_authenticate_parcel_weight(self):
        """ Test method to test delivery order with parcel weight as string."""
        resp = self.app.post('/api/v1/parcels', data=json.dumps(
            {"parcel_id": 1, "user_id": 2, "user_email": "derek@fbi.gov", "parcel_weight": "gf", "pick_up_location": "kisasi",
            "destination": "Andela", "price_quote": 200, "status": "Transit"}), content_type='application/json')
        self.assertEqual(
            resp.data, b'{"error":"User ID, Parcel weight and Price quote must be an int."}\n')


    def test_authenticate_parcel_price_quote(self):
        """ Test method to test delivery order without a price quote."""
        resp = self.app.post('/api/v1/parcels', data=json.dumps(
            {"parcel_id": 1, "user_id": 2, "user_email": "derek@fbi.gov", "parcel_weight": 15, "pick_up_location": "kisasi",
            "destination": "Andela", "price_quote": "ffg", "status": "Transit"}), content_type='application/json')
        self.assertEqual(
            resp.data, b'{"error":"User ID, Parcel weight and Price quote must be an int."}\n')


    def test_authenticate_parcel_status_missing(self):
        """ Test method to test delivery order without a status"""
        resp = self.app.post('/api/v1/parcels', data=json.dumps(
            {"parcel_id": 1, "user_id": 2, "user_email": "derek@fbi.gov", "parcel_weight": 15, "pick_up_location": "kisasi",
            "destination": "Andela", "price_quote": 200,}), content_type='application/json')
        self.assertEqual(
            resp.data, b'{"msg":"Parcel has been added"}\n')


    def test_get_all_nonexistant_user_parcels(self):
        """ Test method to retrieve parcels of non existant user."""
        resp = self.app.get('/api/v1/users/9/parcels')
        self.assertEqual(resp.data, b'{"error":"User not found"}\n')
        self.assertEqual(resp.status_code, 200)

    def test_cancel_delivery_transit(self):
        """ Test method to cancel a delivery in transit."""
        resp = self.app.put('/api/v1/parcels/1/cancel', data=json.dumps(
                {"parcel_id": 1, "user_id": 2, "user_email": "derek@fbi.gov", "parcel_weight": 15, "pick_up_location": "kisasi",
        "destination": "Andela", "price_quote": 200, "status": "Transit"}), content_type='application/json')
        self.assertEqual(resp.status_code, 200)

    def test_cancel_nonexistant_parcel_delivery(self):
        """ Test method to cancel an nonexistant delivery."""
        resp = self.app.put('/api/v1/parcels/9/cancel', data=json.dumps(
            {"parcel_id": 1, "user_id": 2, "user_email": "derek@fbi.gov", "parcel_weight": 15, "pick_up_location": "kisasi",
            "destination": "Andela", "price_quote": 200, "status": "Canceled"}), content_type='application/json')
        self.assertEqual(
            resp.data, b'{"error":"Can not cancel non existant parcel order."}\n')

    def test_get_parcel_by_wrong_id(self):
        """ Test method to check wrong id."""
        resp = self.app.get('/api/v1/parcels/9')
        self.assertEqual(resp.data, b'{"error":"No parcel by that ID in Parcels list."}\n')

    def test_parcels_record_creation(self):
        """ Test method  to test status code of created parcel order."""
        resp = self.app.post('/api/v1/parcels', data=json.dumps(
            {"parcel_id": 1, "user_id": 2, "user_email": "derek@fbi.gov", "parcel_weight": 15, "pick_up_location": "kisasi",
            "destination": "Andela", "price_quote": 200, "status": "Transit"}), content_type='application/json')
        # self.assertEqual(resp.status_code, 201)
        self.assertEqual(resp.data, b'{"msg":"Parcel has been added"}\n')

    def test_retrieve_all_parcel_records(self):
        """ Test method  fetch all parcels in list."""
        resp = self.app.get('/api/v1/parcels')
        self.assertEqual(resp.status_code, 200)

    def test_get_parcel_record_given_an_id(self):
        """ Test method to check whether parcel is in list given its id."""
        resp = self.app.get('/api/v1/parcels/2')
        self.assertEqual(resp.status_code, 200)

    def test_nonexistant_parcel(self):
        """ Test method to test non existant parcel by id."""
        resp = self.app.get('/api/v1/parcels/<parcel_id>')
        self.assertEqual(resp.status_code, 404)

    def tearDown(self):
        pass