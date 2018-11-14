""" File for users view."""
from sendit.views.user_view import UserView
from sendit import app

obj_user_views = UserView()

@app.route('/api/v1/users', methods=["GET"])
def get_users():
    """ Method route to get all users """
    return obj_user_views.fetch_users()

@app.route('/api/v1/users/<int:user_id>', methods=["GET"])
def get_single_user(user_id):
    """ Method route to get user by ID """
    return obj_user_views.fetch_single_user_id(user_id)

@app.route('/api/v1/users', methods=["POST"])
def create_user():
    """ Method route to create a user."""
    return obj_user_views.add_app_user()

@app.route('/api/v1/users/<int:user_id>/parcels', methods=["GET"])
def user_parcels(user_id):
    """ Method route to cancel a user."""
    return obj_user_views.specific_user_pancels(user_id)