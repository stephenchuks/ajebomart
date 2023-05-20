""" A repository for Product Category """
import sys
from sqlalchemy import or_
from models import ProductCategory, db
from utils.errors import DataNotFound, DuplicateData, InternalServerError
from sqlalchemy.exc import IntegrityError
from flask import jsonify


class CategoryRepository:
    """ Cartegory CRUD functionalities """

    @staticmethod
    def get(category_id=None):
        """ Query a product based on category """

        # ensure that a parameter was passed
        if not category_id:
            raise DataNotFound(
                f"category id required")

        try:
            query = ProductCategory.query
            if category_id:
                query = query.filter(ProductCategory.id == category_id)

            product_category = query.first()
            return product_category
        except DataNotFound as e:
            print(sys.exc_info())
            raise DataNotFound(
                f"Product Category with {category_id} not found")

    @staticmethod
    def getAll():
        """ get all categories"""
        query = db.session.query(ProductCategory).all()

        data = []

        for category in query:
            data.append({
                "id": category.id,
                "name": category.name,
                "created_at": category.created_at,
            })

        return data

    def update(self, category_id, **args):
        """ Update a category via an Id """
        category = self.get(category_id)
        if 'name' in args and args['name'] is not None:
            category.name = args['name']

        return category.save()

    @staticmethod
    def create(name):
        """ Create a new category """
        try:
            print("Testing the router ", name)
            category = ProductCategory(name=name)
            return category.save()

        except IntegrityError as e:
            message = e.orig.diag.message_detail
            raise DuplicateData(message)
        except Exception as e:
            print(e)
            raise InternalServerError

    @staticmethod
    def delete(category_id):
        """ Delete Category by Id"""

        # ensure category_id is pass
        if not category_id:
            raise DataNotFound(f"please provide Category Id")

        try:
            query = ProductCategory.query.filter(
                ProductCategory.id == category_id).first()
            if not query:
                raise DataNotFound(
                    f"Category with {category_id} not found")
            return query.delete()
        except DataNotFound as e:
            print(sys.exc_info())
            raise DataNotFound(f"Category with {category_id} not found")
