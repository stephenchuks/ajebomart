from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()


from .admin import Admin
from .customer import Customer
from .category import ProductCategory
from .product import Product
from .cart import Cart
from .order import Order