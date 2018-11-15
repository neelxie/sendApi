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
    """ Method route to get all Parcels """
    return my_parcels.fetch_all_parcels()

@app.route('/api/v1/parcels/<int:parcel_id>', methods=["GET"])
def get_single_parcel(parcel_id):
    """ Method route to get Parcel by ID """
    return my_parcels.fetch_parcel_by_id(parcel_id)

@app.route('/api/v1/parcels', methods=["POST"])
def create_parcel():
    """ Method route to create a Parcel."""
    return my_parcels.add_parcels()

@app.route('/api/v1/parcels/<int:parcel_id>/cancel', methods=["PUT"])
def cancel_parcel(parcel_id):
    """ Method route to cancel a Parcel."""
    return my_parcels.cancel_specific_parcel(parcel_id)
