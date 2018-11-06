from flask import Flask
from flask_restful import Api
from flask_restful import Resource

app = Flask(__name__)
api = Api(app)

class Index(Resource):
    """ Index resource."""
    def get(self):
        """ Get method for my index page."""
        return {"message":"This is my Index Page."}

api.add_resource(Index, '/')

if __name__ == '__main__':
    app.run(debug=True)
