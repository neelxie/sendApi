"""Class model for user that returns a list that holds all user."""
from flask import jsonify
from flask import request
from .parcel_model import all_parcels

list_of_users = []

def check_user(user_id):
    """ Check for a user with this as ID."""
    for user in list_of_users:
        if user.get("user_id") == int(user_id):
            return user

def personal_orders(user_id):
    """ Method to return list of orders for a single user."""
    individual_parcels = []
    for parcel in all_parcels:
        if parcel.get("user_id") == int(user_id):
            individual_parcels.append(parcel)
            return individual_parcels

class Users:
    """ Model class for users. """
    def __init__(self, *args):
        """ Initialisation method for users class."""
        pass

    def fetch_users(self):
        """ Method to return all users."""
        if not list_of_users:
            return jsonify({"Message": "users list is empty."}), 200
        return jsonify({"All users": list_of_users}), 200

    def fetch_single_user_id(self, user_id):
        """ Method to return user by ID."""
        if list_of_users:
            specific_user = check_user(user_id)
            if specific_user:
                return jsonify({"user": specific_user})
            return jsonify({"error": "No user by that ID in users list."})

    def add_app_user(self):
        """ Method to add a user."""
        user_info = request.get_json()

        if user_info:
            user_info['user_id'] = len(list_of_users) + 1
            user_strs = ("user_email", "user_name")

            if all(key in user_info.keys() for key in user_strs):
                user_email = user_info.get("user_email")
                user_name = user_info.get("user_name")
                if len(user_email) < 2 or not user_name.isalpha():
                    return jsonify({"Error": "User Email and User name must be of valid string."})
                list_of_users.append(user_info)
                return jsonify({"msg": "User added"}), 201
            return jsonify({"error": "field missing."})

    def specific_user_pancels(self, user_id):
        """ Method to cancel a user parcel delivery order."""
        user = check_user(user_id)
        parcel_order = personal_orders(user_id)
        if user:
            if parcel_order:
                return jsonify(parcel_order[0])
            return jsonify({"message": "User has no parcels yet."})
        return jsonify({"error": "User not found"})
