""" File for index view."""
from sendit.views.index_view import IndexView
from sendit import app

obj_parcel_views = IndexView()

@app.route('/api/v1/')
def home():
    """ Index route for app."""
    return obj_parcel_views.index()