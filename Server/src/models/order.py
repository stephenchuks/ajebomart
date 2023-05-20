"""
This class defines the order database model
"""
import uuid
from . import db
from .abc import BaseModel, MetaBaseModel
from datetime import datetime


class Order(db.Model, BaseModel, metaclass=MetaBaseModel):
    """
    The Order model class
    """

    __tablename__ = "orders"

    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)
    # tax = db.Column(db.Float, nullable=False)
    total_cost = db.Column(db.Float, nullable=False)
    delivery_status = db.Column(
        db.String(20), nullable=False, default="pending")
    delivered_at = db.Column(db.DateTime)
    delivery_address = db.Column(db.String(100), nullable=False)
    phone_number = db.Column(db.String(20), nullable=False)

    # Foreign key
    customer_id = db.Column(db.Integer, db.ForeignKey(
        "customers.id"), nullable=False)
    products_id = db.Column(db.Integer, db.ForeignKey(
        'products.id'), nullable=False)
