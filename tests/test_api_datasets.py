import unittest
from flask import Flask
from sendit.models.user_model import Users
from sendit.models.parcel_model import Parcels
from sendit.views.parcel_view import *

class Test_Datasets(unittest.TestCase):
    """ Test class to test data structures used in app."""

    def test_users_model(self):
        """ Test method to test users model."""
        my_obj = Users()
        self.assertIsInstance(my_obj.users_list, list)

    def test_parcels_model(self):
        """ Test method to test parcels model."""
        my_parcel = Parcels()
        self.assertIsInstance(my_parcel.parcels_list, list)

        #Testing the get_order_by_id function with an integer
    def test_get_parcel_by_id(self):
        self.assertIsInstance(get_parcel_by_id(1), dict)


    #Testing the get_user_by_id function with an integer
    def test_get_user_by_id(self):
        self.assertIsInstance(get_user_by_id(1), dict)
