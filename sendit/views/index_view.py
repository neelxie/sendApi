""" This file contains the index resource. --http://sendit.com/api/v1/-- """

from flask_restful import Resource

class Index(Resource):
    """ Index resource."""
    def get(self):
        """ Get method for my index page."""
        return {"message":"This is my Index Page."}
