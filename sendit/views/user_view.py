""" File for users view."""
from sendit.models.user_model import Users
from sendit import app

app_users = Users()

@app.route('/api/v1/users', methods=["GET"])
def get_users():
    """ Method route to get all users """
    return app_users.fetch_users()

@app.route('/api/v1/users/<int:user_id>', methods=["GET"])
def get_single_user(user_id):
    """ Method route to get user by ID """
    return app_users.fetch_single_user_id(user_id)

@app.route('/api/v1/users', methods=["POST"])
def create_user():
    """ Method route to create a user."""
    return app_users.add_app_user()

@app.route('/api/v1/users/<int:user_id>/parcels', methods=["GET"])
def user_parcels(user_id):
    """ Method route to cancel a user."""
    return app_users.specific_user_pancels(user_id)