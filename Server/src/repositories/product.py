""" A repository for Product """
import sys
from sqlalchemy import or_
from models import db, Product, ProductCategory
from utils.errors import DataNotFound, DuplicateData, InternalServerError
from sqlalchemy.exc import IntegrityError
from flask import jsonify


class ProductRepository:
    """ Product CRUD functionalities """

    @staticmethod
    def get(product_id=None):
        """ get product by product_id """

        # ensure product_id was passed
        if not product_id:
            raise DataNotFound(f"Please provide a product Id")

        try:
            query = Product.query
            if product_id:
                query = query.filter(Product.id == product_id)

            product = query.first()
            return product
        except DataNotFound as e:
            print(sys.exc_info())
            raise DataNotFound(f"Product with {product_id} not found")

    @staticmethod
    def getAll():
        """ Query all products"""
        query = db.session.query(Product).join(ProductCategory).all()
        products = []

        for product in query:
            products.append({
                "id": product.id,
                "title": product.title,
                "price": product.price,
                "quantity": product.quantity,
                "description": product.description,
                "image": product.image,
                "category_id": product.category_id,
                "created_at": product.created_at,
                "updated_at": product.updated_at
            })

        return products

    def update(self, product_id, **args):
        """ Update a product details """
        product = self.get(product_id)
        if 'title' in args and args['title'] is not None:
            product.title = args['title']

        if 'price' in args and args['price'] is not None:
            product.price = args['price']

        if 'quantity' in args and args['quantity'] is not None:
            product.quantity = args['quantity']

        if 'description' in args and args['description'] is not None:
            product.description = args['description']

        if 'image' in args and args['image'] is not None:
            product.image = args['image']

        return product.save()

    @staticmethod
    def create(title, price, quantity, description, image, category_id):
        """ Create a new product """
        try:
            product = Product(title=title, price=price, quantity=quantity,
                              description=description, image=image, category_id=category_id)

            return product.save()

        except IntegrityError as e:
            message = e.orig.diag.message_detail
            raise DuplicateData(message)
        except Exception as er:
            print("printing error", er)
            raise InternalServerError

    @staticmethod
    def delete(product_id):
        """ Delete a product by product_id """

        # ensure product id is passed
        if not product_id:
            raise DataNotFound(f"Please provide product_id")

        try:
            query = Product.query.filter(Product.id == product_id)

            product = query.first()
            return product.delete()
        except DataNotFound as e:
            print(sys.exc_info())
            raise DataNotFound(f"Product with {product_id} not found")
