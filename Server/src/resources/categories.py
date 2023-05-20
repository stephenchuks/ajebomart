"""Category Resource"""
from flask import jsonify, abort
from flask_restful import Resource
from flask_restful.reqparse import Argument
from repositories import CategoryRepository
from utils import parse_params
from utils.errors import DataNotFound


class CategoriesResource(Resource):
    """ Category Resource """

    @staticmethod
    def get_category(category_id):
        """ get product category """
        try:
            category = CategoryRepository.get(category_id=category_id)
            return jsonify({
                "id": category.id,
                "name": category.name,
            })
        except DataNotFound as e:
            abort(404, e.message)
        except Exception:
            abort(500)

    @staticmethod
    def get_all():
        """ get all categories """
        categories = CategoryRepository.getAll()
        return jsonify({"data": categories})

    @staticmethod
    @parse_params(
        Argument("name", location="json", required=True,
                 help="The name of the product_category."),
    )
    def update(category_id, name):
        """ Update a category """
        category = CategoryRepository().update(
            category_id=category_id, name=name
        )
        return jsonify({"message": category.json})

    def delete(category_id):
        """ delete a category"""
        CategoryRepository.delete(category_id=category_id)
        return jsonify({"message": "category successfully deleted"})

    @staticmethod
    @parse_params(
        Argument("name", location="json", required=True,
                 help="The name of the category."),
    )
    def post(name):
        """ Create a category """
        category = CategoryRepository.create(
            name=name
        )
        return jsonify({"data": category.json})
