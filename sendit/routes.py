""" stuff """
from flask import Flask
from flask import Blueprint
from flask_restful import Api
from flask_restful import Resource
from sendit.views.index_view import Index
from sendit.views.user_view import OneUser
from sendit.views.user_view import AllUsers


api_bp = Blueprint('api', __name__)
api = Api(api_bp)

api.add_resource(Index, '/')
api.add_resource(AllUsers, '/users')
api.add_resource(OneUser, '/users/<int:user_id>')