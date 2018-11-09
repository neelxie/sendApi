""" This file contains the parcels resources view."""
from flask_restful import Resource
from flask_restful.reqparse import RequestParser
from ..models.parcel_model import Parcels
from .user_view import get_user_by_id

parcels_record = Parcels()

# parcels_record.parcels_list = []
parcels_record.parcels_list = [ 
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

def get_parcel_by_id(parcel_id):
    """ Check parcel list for a parcel with this ID."""
    for parcel in parcels_record.parcels_list:
        if parcel.get("parcel_id") == int(parcel_id):
            return parcel

class OneParcel(Resource):
    """ class for a single parcel."""

    def get(self, parcel_id):
        """ Method to get a parcel by ID."""
        if not parcels_record.parcels_list:
            return {"error": "parcels record empty."}, 400
        specific_parcel = get_parcel_by_id(parcel_id)
        if not specific_parcel:
            return {"error": "parcel not found"}, 400
        return specific_parcel

class UserParcels(Resource):
    """ class for all parcels from single user."""

    def get(self, user_id):
        """ Method to get a parcel by ID."""
        user = get_user_by_id(user_id)
        if user:
            individual_parcels = []
            for parcel in parcels_record.parcels_list:
                if parcel.get("user_id") == int(user_id):
                    individual_parcels.append(parcel)
            if individual_parcels:
                return individual_parcels
            else:
                return {"message": "User has no parcels yet."}
        return {"error": "User not found"}


requester = RequestParser(bundle_errors=True)
requester.add_argument("parcel_id", type=int, default=1, required=True, help="id has to be an int.")
requester.add_argument("user_id", type=int, default=1, required=True, help="id has to be an int.")
requester.add_argument("user_email", type=str, required=True, help="Name has to be valid string.")
requester.add_argument("parcel_weight", type=int, default=1, required=True, help="id has to be an int.")
requester.add_argument("pick_up_location", type=str, required=True, help="Role has to be a valid string")
requester.add_argument("destination", type=str, required=True, help="Role has to be a valid string")
requester.add_argument("price_quote", type=int, default=1, required=True, help="id has to be an int.")
requester.add_argument("status", type=str, required=True, help="Role has to be a valid string")


class AllParcels(Resource):
    """ class for all parcels."""
    def get(self):
        """ Method to return all parcels in the record."""
        if parcels_record.parcels_list:
            return parcels_record.parcels_list
        return {"error": "parcels record empty."}, 400

    def post(self):
        """ Method to add an parcel in the record."""
        args = requester.parse_args()
        args["parcel_id"] = len(parcels_record.parcels_list) + 1
        args["status"] = "Transit"
        parcels_record.parcels_list.append(args)
        return {"msg": "User added", "User_info": args}