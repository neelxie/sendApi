""" Model class for parcels that returns a list that holds all parcels."""
from flask import jsonify
from flask import request

all_parcels = []

def get_parcel_by_id(parcel_id):
    """ Check parcel list for a parcel with this ID."""
    for parcel in all_parcels:
        if parcel.get("parcel_id") == int(parcel_id):
            return parcel

def all_int(first, second, third):
    """
    method to check if all arguments are ints else return false. """
    if not isinstance(first, int) or not isinstance(
            second, int) or not isinstance(third, int):
        return True
    return False

def valid_string(one, two, three):
    """ method to check whether all inputs are strings.
    """
    if not isinstance(one, str) or not isinstance(two, str) or not isinstance(three, str):
        return True
    if one.isspace() or two.isspace() or three.isspace():
        return True
    return False

def my_str_len(un, deux, trois):
    """ method to check string length. """
    if len(un) < 1 or len(deux) < 1 or len(trois) < 1:
        return True
    if not deux.isalpha() or not trois.isalpha():
        return True
    return False

def authenticate(ling, yi, san):
    if valid_string(ling, yi, san) or my_str_len(ling, yi, san):
        return True
    return False

class Parcels:
    """ Model class for parcels. """
    def __init__(self, *args):
        """ Initialisation method for parcels class."""
        pass

    def get_all_app_parcels(self):
        """ This is a class method to return all parcels."""
        if not all_parcels:
            return jsonify({"Message": "Parcels list is empty."}), 200
        return jsonify({"All Parcels": all_parcels}), 200

    def fetch_parcel_by_id(self, parcel_id):
        """ Method to return parcel by ID."""
        if all_parcels:
            specific_parcel = get_parcel_by_id(parcel_id)
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

                if all_int(user_id, parcel_weight, price_quote):
                    return jsonify(
                        {"error": "User ID, Parcel weight and Price quote must be an int."})

                if authenticate(user_email, pick_up_location, destination):
                    return jsonify(
                        {"Error": "User Email, Pickup location and Destination must be of variable type string."})

                all_parcels.append(data)
                return jsonify({"msg":"Parcel has been added"}), 201
            return jsonify({"error": "field missing."})

    def cancel_specific_parcel(self, parcel_id):
        """ Method to cancel a parcel."""
        data = get_parcel_by_id(parcel_id)
        if data:
            if data['status'] == 'Canceled' or data['status'] == 'Delivered':
                return jsonify(
                    {"error": "Can not cancel an already canceled or delivered parcel order."})
            data['status'] = "Canceled"
            return jsonify(
                {"msg": "Parcel delivery order canceled."}), 200
        return jsonify({"error": "Can not cancel non existant parcel order."})

