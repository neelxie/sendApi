""" Test File with all app endpoints. """
import unittest
import json
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

    def test_get_all_users(self):
        """ Correct Test method to get all users."""
        with self.app as derek:
            resp = derek.get('/api/v1/users')
            self.assertEqual(resp.status_code, 200)

    """ Test parcel creation endpoint """

    def test_api_parcel_creation(self):
        """ Test method to test delivery order."""
        resp = self.app.post('http://127.0.0.1:5000/api/v1/parcels', data=json.dumps(
            {"parcel_id": 1, "user_id": 2, "user_email": "derek@fbi.gov", "parcel_weight": 15, "pick_up_location": "kisasi",
            "destination": "Andela", "price_quote": 200, "status": "Transit"}),
             content_type='application/json')
        self.assertEqual(resp.status_code, 201)

    def test_authenticate_parcel_user_id_missing(self):
        """ Test method to test delivery order without a user id."""
        resp = self.app.post('http://127.0.0.1:5000/api/v1/parcels', data=json.dumps(
            {"parcel_id": 1, "user_email": "derek@fbi.gov","parcel_weight": 15, "pick_up_location": "kisasi",
            "destination": "Andela", "price_quote": 200, "status": "Transit"}), content_type='application/json')
        self.assertEqual(
            resp.data, b'{"message": {"user_id": "user_id has to be an int."}}\n')

    def test_authenticate_parcel_id(self):
        """ Test method to test delivery order without a parcel id."""
        resp = self.app.post('http://127.0.0.1:5000/api/v1/parcels', data=json.dumps(
            {"parcel_id": "sff", "user_id": 2,"user_email": "derek@fbi.gov", "parcel_weight": 15, "pick_up_location": "kisasi",
            "destination": "Andela", "price_quote": 200, "status": "Transit"}), content_type='application/json')
        self.assertEqual(
            resp.data, b'{"message": {"parcel_id": "parcel_id has to be an int."}}\n')

    def test_authenticate_parcel_id_missing(self):
        """ Test method to test delivery order with parcel id missing."""
        resp = self.app.post('http://127.0.0.1:5000/api/v1/parcels', data=json.dumps(
            {"user_id": 2, "user_email": "derek@fbi.gov", "parcel_weight": 15, "pick_up_location": "kisasi",
            "destination": "Andela", "price_quote": 200, "status": "Transit"}), content_type='application/json')
        self.assertEqual(
            resp.data, b'{"message": {"parcel_id": "parcel_id has to be an int."}}\n')

    def test_authenticate_parcel_id_space(self):
        """ Test method to test delivery order with parcel id as string."""
        resp = self.app.post('http://127.0.0.1:5000/api/v1/parcels', data=json.dumps(
            {"parcel_id": " ", "user_id": 2, "user_email": "derek@fbi.gov", "parcel_weight": 15, "pick_up_location": "kisasi",
            "destination": "Andela", "price_quote": 200, "status": "Transit"}), content_type='application/json')
        self.assertEqual(
            resp.data, b'{"message": {"parcel_id": "parcel_id has to be an int."}}\n')

    def test_authenticate_parcel_user_id(self):
        """ Test method to test delivery order with user id as empty string."""
        resp = self.app.post('http://127.0.0.1:5000/api/v1/parcels', data=json.dumps(
            {"parcel_id": 1, "user_id": "", "user_email": "derek@fbi.gov", "parcel_weight": 15, "pick_up_location": "kisasi",
            "destination": "Andela", "price_quote": 200, "status": "Transit"}), content_type='application/json')
        self.assertEqual(
            resp.data, b'{"message": {"user_id": "user_id has to be an int."}}\n')


    def test_authenticate_parcel_weight(self):
        """ Test method to test delivery order with parcel weight as string."""
        resp = self.app.post('http://127.0.0.1:5000/api/v1/parcels', data=json.dumps(
            {"parcel_id": 1, "user_id": 2, "user_email": "derek@fbi.gov", "parcel_weight": "gf", "pick_up_location": "kisasi",
            "destination": "Andela", "price_quote": 200, "status": "Transit"}), content_type='application/json')
        self.assertEqual(
            resp.data, b'{"message": {"parcel_weight": "parcel_weight has to be an int."}}\n')


    def test_authenticate_parcel_price_quote(self):
        """ Test method to test delivery order without a price quote."""
        resp = self.app.post('http://127.0.0.1:5000/api/v1/parcels', data=json.dumps(
            {"parcel_id": 1, "user_id": 2, "user_email": "derek@fbi.gov", "parcel_weight": 15, "pick_up_location": "kisasi",
            "destination": "Andela", "price_quote": "ffg", "status": "Transit"}), content_type='application/json')
        self.assertEqual(
            resp.data, b'{"message": {"price_quote": "price_quote has to be an int."}}\n')


    def test_authenticate_parcel_location(self):
        """ Test method to test delivery order with location as numbers."""
        resp = self.app.post('http://127.0.0.1:5000/api/v1/parcels', data=json.dumps(
            {"parcel_id": 1, "user_id": 2, "user_email": "derek@fbi.gov", "parcel_weight": 15, "pick_up_location": "kisasi",
            "destination": "24563", "price_quote": 200, "status": "Transit"}), content_type='application/json')
        self.assertEqual(
            resp.data, b'{"msg": "Location should only be a string."}\n')

    def test_authenticate_parcel_status_missing(self):
        """ Test method to test delivery order without a status"""
        resp = self.app.post('http://127.0.0.1:5000/api/v1/parcels', data=json.dumps(
            {"parcel_id": 1, "user_id": 2, "user_email": "derek@fbi.gov", "parcel_weight": 15, "pick_up_location": "kisasi",
            "destination": "Andela", "price_quote": 200,}), content_type='application/json')
        self.assertEqual(
            resp.data, b'{"message": {"status": "Status has to be a valid string"}}\n')


    """ Test get all parcels endpoint """

    def test_get_all_user_by_id(self):
        """ Test method to retrieve a user with id 1."""
        resp = self.app.get('http://127.0.0.1:5000/api/v1/users/1')
        self.assertEqual(resp.status_code, 200)

    def test_get_all_nonexistant_user_parcels(self):
        """ Test method to retrieve parcels of non existant user."""
        resp = self.app.get('http://127.0.0.1:5000/api/v1/users/9/parcels')
        self.assertEqual(resp.data, b'{"error": "User not found"}\n')
        self.assertEqual(resp.status_code, 200)

    def test_get_user_with_zero_parcels(self):
        """ Test method to retrieve a user with no parcel delivery orders yet."""
        resp = self.app.get('http://127.0.0.1:5000/api/v1/users/3/parcels')
        self.assertEqual(resp.data, b'{"message": "User has no parcels yet."}\n')

    def test_cancel_delivery_transit(self):
        """ Test method to cancel a delivery in transit."""
        resp = self.app.post('http://127.0.0.1:5000/api/v1/parcels', data=json.dumps(
                {"parcel_id": 1, "user_id": 2, "user_email": "derek@fbi.gov", "parcel_weight": 15, "pick_up_location": "kisasi",
        "destination": "Andela", "price_quote": 200, "status": "Transit"}), content_type='application/json')
        resp = self.app.put('http://127.0.0.1:5000/api/v1/parcels/1/cancel', data=json.dumps(
                {"parcel_id": 1, "user_id": 2, "user_email": "derek@fbi.gov", "parcel_weight": 15, "pick_up_location": "kisasi",
        "destination": "Andela", "price_quote": 200, "status": "Transit"}), content_type='application/json')
        self.assertEqual(resp.status_code, 200)

    def test_cancel_delivery_canceled(self):
        """ Cancel Test method to test an already canceled order."""
        resp = self.app.post('http://127.0.0.1:5000/api/v1/parcels', data=json.dumps(
            {"parcel_id": 1, "user_id": 2, "user_email": "derek@fbi.gov", "parcel_weight": 15, "pick_up_location": "kisasi",
            "destination": "Andela", "price_quote": 200, "status": "Transit"}), content_type='application/json')
        resp = self.app.put('http://127.0.0.1:5000/api/v1/parcels/1/cancel', data=json.dumps(
            {"parcel_id": 1, "user_id": 2, "user_email": "derek@fbi.gov", "parcel_weight": 15, "pick_up_location": "kisasi",
            "destination": "Andela", "price_quote": 200, "status": "Canceled"}), content_type='application/json')
        self.assertEqual(
            resp.data, b'{"error": "Can not cancel an already canceled parcel order."}\n')

    def test_cancel_nonexistant_parcel_delivery(self):
        """ Test method to cancel an nonexistant delivery."""
        resp = self.app.post('http://127.0.0.1:5000/api/v1/parcels', data=json.dumps(
            {"parcel_id": 1, "user_id": 2, "user_email": "derek@fbi.gov", "parcel_weight": 15, "pick_up_location": "kisasi",
            "destination": "Andela", "price_quote": 200, "status": "Transit"}), content_type='application/json')
        resp = self.app.put('http://127.0.0.1:5000/api/v1/parcels/9/cancel', data=json.dumps(
            {"parcel_id": 1, "user_id": 2, "user_email": "derek@fbi.gov", "parcel_weight": 15, "pick_up_location": "kisasi",
            "destination": "Andela", "price_quote": 200, "status": "Canceled"}), content_type='application/json')
        self.assertEqual(
            resp.data, b'{"error": "Can not cancel non existant parcel order."}\n')

    def test_get_parcel_by_wrong_id(self):
        """ Test method to check wrong id."""
        resp = self.app.get('http://127.0.0.1:5000/api/v1/parcels/9')
        self.assertEqual(resp.data, b'{"error": "parcel not found"}\n')

    def test_parcels_record_creation(self):
        """ Test method  to test status code of created parcel order."""
        resp = self.app.post('http://127.0.0.1:5000/api/v1/parcels', data=json.dumps(
            {"parcel_id": 1, "user_id": 2, "user_email": "derek@fbi.gov", "parcel_weight": 15, "pick_up_location": "kisasi",
            "destination": "Andela", "price_quote": 200, "status": "Transit"}), content_type='application/json')
        self.assertEqual(resp.status_code, 201)

    def test_retrieve_all_parcel_records(self):
        """ Test method  fetch all parcels in list."""
        resp = self.app.get('http://127.0.0.1:5000/api/v1/parcels')
        self.assertEqual(resp.status_code, 200)

    def test_get_parcel_record_given_an_id(self):
        """ Test method to check whether parcel is in list given its id."""
        resp = self.app.get('http://127.0.0.1:5000/api/v1/parcels/2')
        self.assertEqual(resp.status_code, 200)

    def test_nonexistant_parcel(self):
        """ Test method to test non existant parcel by id."""
        resp = self.app.get(
            'http://127.0.0.1:5000/api/v1/parcels/<parcel_id>')
        self.assertEqual(resp.status_code, 404)

    def tearDown(self):
        pass
