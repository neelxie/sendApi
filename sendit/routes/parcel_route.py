""" File for Parcel view."""
from sendit.views.parcel_view import ParcelView
from sendit import app

obj_parcel_views = ParcelView()

@app.route('/api/v1/parcels', methods=["GET"])
def get_parcels():
    """ Method route to get all Parcels """
    return obj_parcel_views.fetch_all_parcels()

@app.route('/api/v1/parcels/<int:parcel_id>', methods=["GET"])
def get_single_parcel(parcel_id):
    """ Method route to get Parcel by ID """
    return obj_parcel_views.fetch_parcel_by_id(parcel_id)

@app.route('/api/v1/parcels', methods=["POST"])
def create_parcel():
    """ Method route to create a Parcel."""
    return obj_parcel_views.add_parcels()

@app.route('/api/v1/parcels/<int:parcel_id>/cancel', methods=["PUT"])
def cancel_parcel(parcel_id):
    """ Method route to cancel a Parcel."""
    return obj_parcel_views.cancel_specific_parcel(parcel_id)