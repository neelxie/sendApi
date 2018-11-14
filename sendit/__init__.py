""" File herein resides my app instance."""
from flask import Flask

app = Flask(__name__)

from sendit import controller