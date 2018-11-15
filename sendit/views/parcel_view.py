""" File for Parcel view."""
from sendit import app
from ..models.parcel_model import Parcels

my_parcels = Parcels()

@app.route('/api/v1/')
def home():
    """ Index route for app."""
    return "Welcome to the SendIT Courier App."

@app.route('/api/v1/parcels', methods=["GET"])
def get_parcels():
    """ Method route to fetch all Parcels """
    return my_parcels.get_all_app_parcels()

@app.route('/api/v1/parcels/<int:parcel_id>', methods=["GET"])
def get_single_parcel(parcel_id):
    """ App route to get Parcel by ID """
    return my_parcels.fetch_parcel_by_id(parcel_id)

@app.route('/api/v1/parcels', methods=["POST"])
def create_parcel():
    """ Route to create a Parcel."""
    return my_parcels.add_parcels()

@app.route('/api/v1/parcels/<int:parcel_id>/cancel', methods=["PUT"])
def cancel_parcel(parcel_id):
    """ This is a method route to cancel a Parcel delivery order."""
    return my_parcels.cancel_specific_parcel(parcel_id)
