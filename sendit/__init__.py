""" File contains my app factory. """
from flask import Flask

def create_app():
    """ Method to create a flask app."""
    app = Flask(__name__)

    from sendit.routes import api_bp
    app.register_blueprint(api_bp, url_prefix='/api/v1')

    return app

app = create_app()
