"""
This module defines the payment detail model
"""

from . import db
from .abc import BaseModel, MetaBaseModel
from datetime import datetime

class Paymentdetail(db.Model, BaseModel, metaclass=MetaBaseModel):
    """
    The Payment Details model class
    """

    __table__ = "payment_details"

    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Integer)
    status = db.Column(db.String(20))
    created_at = db.Column(db.DateTime(), Default=datetime.utcnow)
    updated_at = db.Column(db.DateTime(), Default=datetime.utcnow)

    #Foreign Key
    orders_id = db.Column(db.Integer, db.ForeignKey('orders.id'), nullable=False)
    payment_methods_id = db.Column(db.Integer, db.ForeignKey('payment_methods.id'), nullable=False)

    #Relationship
    # orders = db.relationship('Order', backref='payment_details', lazy=True)
