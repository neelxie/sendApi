""" This file contains the parcels resources view."""
from flask_restful import Resource
from flask_restful.reqparse import RequestParser
from ..models.parcel_model import Parcels
from .user_view import get_user_by_id
from ..authenticate import AuthenticateView

parcels_record = Parcels()
authenticate = AuthenticateView()

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
        if parcels_record.parcels_list:
            specific_parcel = get_parcel_by_id(parcel_id)
            if not specific_parcel:
                return {"error": "parcel not found"}, 400
            return specific_parcel

class UserParcels(Resource):
    """ class for all parcels from single user."""

    def get(self, user_id):
        """ Method to get a parcel by ID."""
        user = get_user_by_id(user_id)
        individual_parcels = []
        if user:
            for parcel in parcels_record.parcels_list:
                if parcel.get("user_id") == int(user_id):
                    individual_parcels.append(parcel)
            if individual_parcels:
                return individual_parcels
            else:
                return {"message": "User has no parcels yet."}
        return {"error": "User not found"}

class CancelParcel(Resource):
    """ Resource fro canceling an order."""

    def put(self, parcel_id):
        """ Method to cancel a parcel by ID."""
        args = parser.parse_args()
        parcel = get_parcel_by_id(parcel_id)
        if parcel:
            if args["status"] == "Canceled":
                return {"error": "Can not cancel an already canceled parcel order."}
            parcels_record.parcels_list.remove(parcel)
            args["status"] = "Canceled"
            parcels_record.parcels_list.append(args)
            return {"msg": "Parcel delivery order canceled.", "User_info": args}, 200
        return {"error": "Can not cancel non existant parcel order."}


parser = RequestParser(bundle_errors=True)
parser.add_argument("parcel_id", type=int, default=1,
                    required=True, help="parcel_id has to be an int.")
parser.add_argument("user_id", type=int, default=1,
                    required=True, help="user_id has to be an int.")
parser.add_argument("user_email", type=str, required=True,
                    help="user_email has to be valid string.")
parser.add_argument("parcel_weight", type=int, default=1,
                    required=True, help="parcel_weight has to be an int.")
parser.add_argument("pick_up_location", type=str, required=True,
                    help="pick_up_location has to be a valid string")
parser.add_argument("destination", type=str, required=True,
                    help="destination has to be a valid string")
parser.add_argument("price_quote", type=int, default=1,
                    required=True, help="price_quote has to be an int.")
parser.add_argument("status", type=str, required=True,
                    help="Status has to be a valid string")

class AllParcels(Resource):
    """ class for all parcels."""

    def get(self):
        """ Method to return all parcels in the record."""
        if parcels_record.parcels_list:
            return parcels_record.parcels_list

    def post(self):
        """ Method to add an parcel in the record."""
        args = parser.parse_args()
        args["parcel_id"] = len(parcels_record.parcels_list) + 1
        args["status"] = "Transit"
        parcel_keys = ("pick_up_location", "destination")
        if all(key in args.keys() for key in parcel_keys):
            pick_up_location = args.get("pick_up_location")
            destination = args.get("destination")

            invalid = authenticate.authenticate_parcel_order(pick_up_location, destination)
            if invalid:
                return {"msg": invalid}, 400
            parcels_record.parcels_list.append(args)
            return {"msg": "Parcel order delivery added", "User_info": args}, 201
