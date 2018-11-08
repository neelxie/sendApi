import unittest
from flask import Flask
from ..sendit.models.user_model import Users

class Test_Datasets(unittest.TestCase):
    """ Test class to test data structures used in app."""

    def test_users_model(self):
        """ Test method to test users model."""
        my_obj = Users()
        self.assertIsInstance(my_obj.users_list, list)