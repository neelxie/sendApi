""" File herein resides my app instance."""
from flask import Flask

app = Flask(__name__)

from .routes.index_route import home
from .routes.parcel_route import get_parcels
from .routes.parcel_route import get_single_parcel
from .routes.parcel_route import create_parcel
from .routes.parcel_route import cancel_parcel
from .routes.user_route import get_single_user
from .routes.user_route import user_parcels
from .routes.user_route import create_user
from .routes.user_route import get_users