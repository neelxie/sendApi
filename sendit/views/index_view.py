""" File for index view."""
from sendit import app

@app.route('/api/v1/')
def home():
    """ Index route for app."""
    return "Welcome to the SendIT Courier App."