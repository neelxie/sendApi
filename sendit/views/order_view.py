""" This file contains the orders resources view."""
from flask_restful import Resource
from flask_restful.reqparse import RequestParser
from ..models.order_model import Orders

orders_record = Orders()

# orders_record.orders_list = []
orders_record.orders_list = [ 
    {
        "order_id": 1,
        "user_id": 2,
        "user_email": "derek@fbi.gov",
        "parcel_weight": 15,
        "pick_up_location": "kisasi",
        "destination": "Andela",
        "price_quote": 200,
        "status": "Transit"
    },
    {
        "order_id": 2,
        "user_id": 1,
        "user_email": "dero@mit.edu",
        "parcel_weight": 55,
        "pick_up_location": "work",
        "destination": "home",
        "price_quote": 300,
        "status": "Canceled"
    },
    {
        "order_id": 3,
        "user_id": 2,
        "user_email": "derek@fbi.gov",
        "parcel_weight": 35,
        "pick_up_location": "Posta",
        "destination": "DHL",
        "price_quote": 500,
        "status": "Delivered"
    } 
]

def get_order_by_id(order_id):
    """ Check order list for a order with this ID."""
    for order in orders_record.orders_list:
        if order.get("order_id") == int(order_id):
            return order

class OneOrder(Resource):
    """ class for a single order."""

    def get(self, order_id):
        """ Method to get a order by ID."""
        if not orders_record.orders_list:
            return {"error": "Orders record empty."}, 400
        specific_order = get_order_by_id(order_id)
        if not specific_order:
            return {"error": "Order not found"}, 400
        return specific_order

requester = RequestParser(bundle_errors=True)
requester.add_argument("order_id", type=int, default=1, required=True, help="id has to be an int.")
requester.add_argument("user_id", type=int, default=1, required=True, help="id has to be an int.")
requester.add_argument("user_email", type=str, required=True, help="Name has to be valid string.")
requester.add_argument("parcel_weight", type=int, default=1, required=True, help="id has to be an int.")
requester.add_argument("pick_up_location", type=str, required=True, help="Role has to be a valid string")
requester.add_argument("destination", type=str, required=True, help="Role has to be a valid string")
requester.add_argument("price_quote", type=int, default=1, required=True, help="id has to be an int.")
requester.add_argument("status", type=str, required=True, help="Role has to be a valid string")


class AllOrders(Resource):
    """ class for all Orders."""
    def get(self):
        """ Method to return all orders in the record."""
        if orders_record.orders_list:
            return orders_record.orders_list
        return {"error": "Orders record empty."}, 400

    def post(self):
        """ Method to add an order in the record."""
        args = requester.parse_args()
        args["order_id"] = len(orders_record.orders_list) + 1
        args["status"] = "Transit"
        orders_record.orders_list.append(args)
        return {"msg": "User added", "User_info": args}