"""
Define the resources for the order
"""
from flask import jsonify, abort
from flasgger import swag_from
from flask_restful import Resource
from flask_restful.reqparse import Argument
from repositories import OrderRepository
from utils import parse_params
from utils.errors import DataNotFound


class OrderResource(Resource):
    """ methods relative to the order """

    @staticmethod
    def get_one(order_id):
        """ Return an order key information based on order_id """

        try:
            order = OrderRepository.get(order_id=order_id)
            if not order:
                return jsonify({"message": f" Order with the id {order_id} not found"})
            data = {
                "id": order.id,
                "phone_number": order.phone_number,
                "total_cost": order.total_cost,
                "delivery_status": order.delivery_status,
                "delivery_address": order.delivery_address,
                "delivery_": order.delivery_status,
                "delivered_at": order.delivered_at,
                "customer_id": order.customer_id,
                "products_id": order.products_id,
            }
            return jsonify({"data": data})
        except DataNotFound as e:
            abort(404, e.message)
        except Exception as err:
            print(err)
            abort(500)

    @staticmethod
    def get_all():
        """ Return all order key information based on the query parameter """
        orders = OrderRepository.getAll()
        return jsonify({"data": orders})

    @staticmethod
    @parse_params(
        Argument("total_cost", location="json",
                 help="The total_cost of the order."),
        Argument("phone_number", location="json",
                 help="The phone_number of the order."),
        Argument("delivery_status", location="json",
                 help="The delivery_status of the order."),
        Argument("delivered_at", location="json",
                 help="The order of the order."),
        Argument("delivery_address", location="json",
                 help="The order address of an order."),
    )
    def update_order(order_id, total_cost, phone_number, delivery_status, delivery_address, delivered_at):
        """ Update an order """
        repo = OrderRepository()
        order = repo.update(
            order_id=order_id,
            total_cost=total_cost,
            phone_number=phone_number,
            delivery_status=delivery_status,
            delivery_address=delivery_address,
            delivered_at=delivered_at,
        )

        return jsonify({"message": f"order with the id {order_id} updated successfully"})

    @staticmethod
    @parse_params(
        Argument("total_cost", location="json",
                 help="The total_cost of the order."),
        Argument("delivery_address", location="json",
                 help="The delivery_address of the order."),
        Argument("phone_number", location="json",
                 help="The phone number for an order."),
        Argument("delivery_status", location="json",
                 help="The delivery_status of the order."),
        Argument("delivered_at", location="json",
                 help="The order of the order."),
        Argument("customer_id", location="json",
                 help="The customer_id of the order."),
        Argument("products_id", location="json",
                 help="The products id of the order."),
    )
    def post(total_cost, delivery_address, phone_number, delivery_status, delivered_at, products_id, customer_id):
        """ Create an order detail """
        order = OrderRepository.create(
            total_cost=total_cost,
            delivery_status=delivery_status,
            delivery_address=delivery_address,
            phone_number=phone_number,
            delivered_at=delivered_at,
            products_id=products_id,
            customer_id=customer_id,
        )
        data = {
            "phone_number": order.phone_number,
            "total_cost": order.total_cost,
            "delivery_status": order.delivery_status,
            "delivery_address": order.delivery_address,
            "customer_id": order.customer_id,
            "product_id": order.products_id,
        }
        return jsonify({"data": data})

    def delete(order_id):
        """ delete a order via the provided id """
        OrderRepository.delete(order_id=order_id)
        return jsonify({"message": "order successfully deleted"})
