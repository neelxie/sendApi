""" This file contains the users resources view."""
from flask_restful import Resource
from models.user_model import Users

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
    }
]

def get_user_by_id(user_id):
    """ Check user list for a user with this ID."""
    for user in users_record.users_list:
        if user.get("user_id") == int(user_id):
            return user

class OneUser(Resource):
    """ class for a single user."""

    def get(self, user_id):
        """ Method to get a user by ID."""
        specific_user = get_user_by_id(user_id)
        if not specific_user:
            return {"error": "User not found"}
        return specific_user

class AllUsers(Resource):
    """ class for all users."""
    pass
