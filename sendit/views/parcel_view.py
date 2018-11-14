""" Parcels view file of the SendIT app."""
from sendit.models.parcel_model import Parcels
from flask import jsonify
from flask import request

obj_parcel = Parcels()
obj_parcel.parcels_list = [
    {
        "parcel_id": 1,
        "user_id": 2,
        "user_email": "derek@fbi.gov",
        "parcel_weight": 15,
        "pick_up_location": "kisasi",
        "destination": "Andela",
        "price_quote": 200,
        "status": "Transit"
    },
    {
        "parcel_id": 2,
        "user_id": 1,
        "user_email": "dero@mit.edu",
        "parcel_weight": 55,
        "pick_up_location": "work",
        "destination": "home",
        "price_quote": 300,
        "status": "Canceled"
    },
    {
        "parcel_id": 3,
        "user_id": 2,
        "user_email": "derek@fbi.gov",
        "parcel_weight": 35,
        "pick_up_location": "Posta",
        "destination": "DHL",
        "price_quote": 500,
        "status": "Delivered"
    }
]

class ParcelView:
    """ Parcel view class."""

    def fetch_all_parcels(self):
        """ Method to return all parcels."""
        if not obj_parcel.parcels_list:
            return jsonify({"Message": "Parcels list is empty."}), 200
        return jsonify({"All Parcels": obj_parcel.parcels_list}), 200

    def fetch_parcel_by_id(self, parcel_id):
        """ Method to return parcel by ID."""
        if obj_parcel.parcels_list:
            specific_parcel = [parcel for parcel in obj_parcel.parcels_list if parcel.get("parcel_id") == int(parcel_id)]
            if specific_parcel:
                return jsonify({"Parcel": specific_parcel})
            return jsonify({"error": "No parcel by that ID in Parcels list."})
        return jsonify({"All Parcels": obj_parcel.parcels_list}), 200

    def add_parcels(self):
        """ Method to add a parcel."""
        data = request.get_json()
        if data:
            data['parcel_id'] = len(obj_parcel.parcels_list) + 1
            data['status'] = 'Transit'
            obj_parcel.parcels_list.append(data)
            return jsonify({"msg": "User added", "User_info": data}), 201
