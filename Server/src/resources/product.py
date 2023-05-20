"""Product Resource"""
from flask import jsonify, abort
from flask_restful import Resource
from flask_restful.reqparse import Argument
from repositories import ProductRepository
from utils import parse_params
from utils.errors import DataNotFound


class ProductResource(Resource):
    """ Product Resource"""

    @staticmethod
    def get_one(product_id):
        try:
            product = ProductRepository.get(product_id=product_id)
            if not product:
                return jsonify({"message": f" Product with the id {product_id} not found"})

            return jsonify({
                "id": product.id,
                "title": product.title,
                "quantity": product.quantity,
                "description": product.description,
                "price": product.price,
                "category_id": product.category_id,
                "image": product.image,
                "created_at": product.created_at,
                "updated_at": product.updated_at,
            })
        except DataNotFound as e:
            abort(404, e.message)
        except Exception:
            abort(500)

    @staticmethod
    def get_all():
        """ get all product """
        products = ProductRepository.getAll()
        return jsonify({"data": products})

    @staticmethod
    @parse_params(
        Argument("title", location="json", required=True,
                 help="The title of the product."),
        Argument("price", location="json", required=True,
                 help="The price of the product."),
        Argument("quantity", location="json", required=True,
                 help="The quantity of the product."),
        Argument("description", location="json", required=True,
                 help="The description of the product."),
        Argument("image", location="json", required=True,
                 help="The image of the product."),
        Argument("category_id", location="json", required=True,
                 help="The category_id of the product."),
    )
    def post(title, price, quantity, description,  image, category_id):
        """ create product """
        product = ProductRepository.create(
            title=title, price=price, quantity=quantity, description=description, image=image, category_id=category_id
        )
        return jsonify({
            "title": product.title,
            "price": product.price,
            "quantity": product.quantity,
            "description": product.description,
            "image": product.image,
            "category_id": product.category_id,
            "created_at": product.created_at,
            "updated_at": product.updated_at,
        })

    def delete(product_id):
        """ delete product """
        product = ProductRepository.delete(product_id=product_id)

        return jsonify({"message": "product successfully deleted"})

    @staticmethod
    @parse_params(
        Argument("title", location="json", required=True,
                 help="The title of the product."),
        Argument("price", location="json", required=True,
                 help="The price of the product."),
        Argument("quantity", location="json", required=True,
                 help="The quantity of the product."),
        Argument("description", location="json", required=True,
                 help="The description of the product."),
        Argument("image", location="json", required=True,
                 help="The image of the product."),
    )
    def update_product(product_id, title, price, quantity, description, image):
        """ Update a product """
        repository = ProductRepository()
        product = repository.update(
            product_id=product_id, title=title, price=price,
            quantity=quantity, description=description,
            image=image
        )
        return jsonify({"message": "updated successfully"})
