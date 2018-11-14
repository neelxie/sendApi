""" File for Parcel view."""
from sendit.views.parcel_view import ParcelView
from sendit import app

obj_parcel_views = ParcelView()

@app.route('/api/v1/parcels', methods=["GET"])
def get_parcels():
    """ Method route to get all Parcels """
    return obj_parcel_views.fetch_all_parcels()