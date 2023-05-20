""" Product Model Definition"""

from . import db
from .abc import BaseModel, MetaBaseModel
from datetime import datetime


class Product(db.Model, BaseModel, metaclass=MetaBaseModel):
    """ The Product model """

    __tablename__ = "products"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(300), nullable=False)
    price = db.Column(db.Float(10, 2), nullable=False)
    quantity = db.Column(db.Integer)
    description = db.Column(db.String(500), nullable=False)
    image = db.Column(db.String(500))
    created_at = db.Column(db.DateTime(), default=datetime.utcnow)
    updated_at = db.Column(db.DateTime(), default=datetime.utcnow)

    # Foreign Key
    category_id = db.Column(db.Integer, db.ForeignKey(
        'product_categories.id'), nullable=False)
