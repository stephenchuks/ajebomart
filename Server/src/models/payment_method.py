"""
This module defines the paymentMethod model
"""

from locale import currency
from . import db
from datetime import datetime


class PaymentMethod(db.Model):
    """
    The payment method class 
    """

    __tablename__ = 'payment_methods'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    currency = db.Column(db.String(30), nullable=False)
    # currency = db.Column(CurrencyType)
    created_at = db.Column(db.DateTime(), default = datetime.utcnow)
    updated_at = db.Column(db.DateTime(), default = datetime.utcnow)


    #relationship
    payment_details = db.relationship('PaymentDetail', backref="payment_methods", lazy=True)

