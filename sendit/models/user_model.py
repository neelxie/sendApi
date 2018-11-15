"""Class model for user that returns a list that holds all user."""
from flask import jsonify
from flask import request
from .parcel_model import all_parcels

list_of_users = []

class Users:
    """ Model class for users. """
    def __init__(self):
        """ Initialisation method for users class."""
        self.user_list = []

    def fetch_users(self):
        """ Method to return all users."""
        if not list_of_users:
            return jsonify({"Message": "users list is empty."}), 200
        return jsonify({"All users": list_of_users}), 200

    def fetch_single_user_id(self, user_id):
        """ Method to return user by ID."""
        if list_of_users:
            specific_user = [user for user in list_of_users if user.get("user_id") == int(user_id)]
            if specific_user:
                return jsonify({"user": specific_user})
            return jsonify({"error": "No user by that ID in users list."})

    def add_app_user(self):
        """ Method to add a user."""
        data = request.get_json()
        if data:
            data['user_id'] = len(list_of_users) + 1
            list_of_users.append(data)
            return jsonify({"msg": "User added"}), 201

    def specific_user_pancels(self, user_id):
        """ Method to cancel a user parcel delivery order."""
        user = 0
        individual_parcels = []
        for my_user in list_of_users:
            if my_user.get("user_id") == int(user_id):
                user = my_user
        if user:
            for parcel in all_parcels:
                if parcel.get("user_id") == int(user_id):
                    individual_parcels.append(parcel)
            if individual_parcels:
                return jsonify(individual_parcels)
            return jsonify({"message": "User has no parcels yet."})
        return jsonify({"error": "User not found"})
