""" Model class for parcels that returns a list that holds all parcels."""
from flask import jsonify
from flask import request

all_parcels = []

class Parcels:
    """ Model class for parcels. """
    def __init__(self):
        """ Initialisation method for parcels class."""

    def fetch_all_parcels(self):
        """ Method to return all parcels."""
        if not all_parcels:
            return jsonify({"Message": "Parcels list is empty."}), 200
        return jsonify({"All Parcels": all_parcels}), 200

    def fetch_parcel_by_id(self, parcel_id):
        """ Method to return parcel by ID."""
        if all_parcels:
            specific_parcel = [parcel for parcel in all_parcels if parcel.get(
                "parcel_id") == int(parcel_id)]
            if specific_parcel:
                return jsonify({"Parcel": specific_parcel}), 200
            return jsonify({"error": "No parcel by that ID in Parcels list."})

    def add_parcels(self):
        """ Method to add a parcel."""
        data = request.get_json()
        if data:
            data['parcel_id'] = len(all_parcels) + 1
            data['status'] = 'Transit'
            parcel_keys = ("user_id", "user_email", "parcel_weight",
                           "pick_up_location", "destination", "price_quote")

            if all(key in data.keys() for key in parcel_keys):
                user_id = data.get("user_id")
                user_email = data.get("user_email")
                parcel_weight = data.get("parcel_weight")
                pick_up_location = data.get("pick_up_location")
                destination = data.get("destination")
                price_quote = data.get("price_quote")

                if not isinstance(user_id, int) or not isinstance(
                        parcel_weight, int) or not isinstance(price_quote, int):
                    return jsonify(
                        {"error": "User ID, Parcel weight and Price quote must be an int."})

                if not isinstance(user_email, str) or not isinstance(
                        pick_up_location, str) or not isinstance(destination, str):
                    return jsonify(
                        {"Error": "User Email, Pickup location and Destination must be of variable type string."})

                if pick_up_location.isspace() or not pick_up_location.isalpha() or destination.isspace() or not destination.isalpha():
                    return jsonify(
                        {"Error": "The Pickup location and Destination must be string with letters."})

                all_parcels.append(data)
                return jsonify({"msg":"Parcel has been added"}), 201
            return jsonify({"error": "field missing."})

    def cancel_specific_parcel(self, parcel_id):
        """ Method to cancel a parcel."""
        data = 0
        for my_parcel in all_parcels:
            if my_parcel.get("parcel_id") == int(parcel_id):
                data = my_parcel
        if data:
            if data['status'] == 'Canceled' or data['status'] == 'Delivered':
                return jsonify(
                    {"error": "Can not cancel an already canceled or delivered parcel order."})
            data['status'] = "Canceled"
            return jsonify(
                {"msg": "Parcel delivery order canceled."}), 200
        return jsonify({"error": "Can not cancel non existant parcel order."})

