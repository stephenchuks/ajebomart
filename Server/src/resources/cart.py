"""Cart Resource"""
from flask_restful import Resource
from flask_restful.reqparse import Argument
from repositories import CartRepository
from utils import parse_params
from utils.errors import DataNotFound


class CartResource(Resource):
    """ cart functionalities """

    @staticmethod
    def get_one(card_id):
        """ Return a cart based on id provided"""
        try:
            cart = CartRepository.get_one(card_id=card_id)
            if not cart:
                return jsonify({"message": f" Cart with the id {card_id} not found"})
            data = {
                "quantity": cart.quantity,
                "id": cart.id,
                "product_id": cart.product_id,
                "customer_id": cart.customer_id,
                "unit_price": cart.unit_price,
                "total_cost": cart.total_cost
            }
            return jsonify({"data": data})
        except DataNotFound as e:
            abort(404, e.message)
        except Exception as err:
            print(err)
            abort(500)

    @staticmethod
    def get_all(customer_id):
        """ get all cart items"""
        carts = CartRepository.getAll(customer_id=customer_id)
        return jsonify({"data": carts})

    @staticmethod
    @parse_params(
        Argument("unit_price", location="json",
                 help="The unit price of cart product."),
        Argument("quantity", location="json",
                 help="The quantity of the cart product."),
        Argument("total_cost", location="json",
                 help="The total_cost of the cart product."),
    )
    def update(cart_id, unit_price, quantity, total_cost):
        """ Update a cart """
        cart = CartRepository().update(
            cart_id=cart_id,
            unit_price=unit_price,
            quantity=quantity,
            total_cost=total_cost
        )
        data = {
            "id": cart.id,
            "quantity": cart.quantity,
            "unit_price": cart.unit_price,
            "total_cost": cart.total_cost,
            "product_id": cart.product_id,
            "customer_id": cart.customer_id,
        }

        return jsonify({"data": data})

    @staticmethod
    @parse_params(
        Argument("unit_price", location="json",
                 help="The unit price of cart product."),
        Argument("quantity", location="json",
                 help="The quantity of the cart product."),
        Argument("total_cost", location="json",
                 help="The total_cost of the cart product."),
        Argument("customer_id", location="json",
                 help="The customer_id of the cart product."),
        Argument("product_id", location="json",
                 help="The product_id of the cart product."),
    )
    def post(unit_price, quantity, total_cost, customer_id, product_id):
        """ Create a cart """
        cart = CartRepository.create(
            unit_price=unit_price,
            quantity=quantity,
            total_cost=total_cost,
            customer_id=customer_id,
            product_id=product_id
        )
        data = {
            "quantity": cart.quantity,
            "id": cart.id,
            "product_id": cart.product_id,
            "customer_id": cart.customer_id,
            "unit_price": cart.unit_price,
            "total_cost": cart.total_cost
        }
        return jsonify({"data": data})

    def delete(cart_id, customer_id):
        """ delete cart """
        CartRepository.delete(cart_id=cart_id, customer_id=customer_id)
        return jsonify({"message": "cart item successfully deleted"})
