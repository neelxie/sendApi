""" Users view file of the SendIT app."""
from sendit.models.user_model import Users
from sendit.views.parcel_view import obj_parcel
from flask import jsonify
from flask import request

users_record = Users()

users_record.users_list = [
    {
        "user_id": 1,
        "user_email": "dero@mit.edu",
        "user_name": "Deliki"
    },
    {
        "user_id": 2,
        "user_email": "derek@fbi.gov",
        "user_name": "Derek"
    },
    {
        "user_id": 3,
        "user_email": "hack@cia.gov",
        "user_name": "Haqa"
    }
]

class UserView:
    """ Users class for views."""
    def fetch_users(self):
        """ Method to return all users."""
        if not users_record.users_list:
            return jsonify({"Message": "users list is empty."}), 200
        return jsonify({"All users": users_record.users_list}), 200

    def fetch_single_user_id(self, user_id):
        """ Method to return user by ID."""
        if users_record.users_list:
            specific_user = [user for user in users_record.users_list if user.get("user_id") == int(user_id)]
            if specific_user:
                return jsonify({"user": specific_user})
            return jsonify({"error": "No user by that ID in users list."})

    def add_app_user(self):
        """ Method to add a user."""
        data = request.get_json()
        if data:
            data['user_id'] = len(users_record.users_list) + 1
            users_record.users_list.append(data)
            return jsonify({"msg": "User added"}), 201

    def specific_user_pancels(self, user_id):
        """ Method to cancel a user parcel delivery order."""
        user = 0
        individual_parcels = []
        for my_user in users_record.users_list:
            if my_user.get("user_id") == int(user_id):
                user = my_user
        if user:
            for parcel in obj_parcel.parcels_list:
                if parcel.get("user_id") == int(user_id):
                    individual_parcels.append(parcel)
            if individual_parcels:
                return jsonify(individual_parcels)
            return jsonify({"message": "User has no parcels yet."})
        return jsonify({"error": "User not found"})