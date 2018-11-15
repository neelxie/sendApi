""" File herein resides my app instance."""
from flask import Flask

app = Flask(__name__)

from .views.parcel_view import *
from .views.user_view import *