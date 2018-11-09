""" stuff """
from flask import Flask
from flask import Blueprint
from flask_restful import Api
from flask_restful import Resource
from sendit.views.index_view import Index
from sendit.views.user_view import OneUser
from sendit.views.user_view import AllUsers
from sendit.views.parcel_view import OneParcel
from sendit.views.parcel_view import AllParcels
from sendit.views.parcel_view import UserParcels
from sendit.views.parcel_view import CancelParcel


api_bp = Blueprint('api', __name__)
api = Api(api_bp)

api.add_resource(Index, '/')
api.add_resource(AllUsers, '/users')
api.add_resource(OneUser, '/users/<int:user_id>')
api.add_resource(UserParcels, '/users/<int:user_id>/parcels')
api.add_resource(AllParcels, '/parcels')
api.add_resource(OneParcel, '/parcels/<int:parcel_id>')
api.add_resource(CancelParcel, '/parcels/<int:parcel_id>/cancel')
