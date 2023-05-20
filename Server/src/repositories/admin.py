""" A repository for Customer """
import sys
from sqlalchemy import or_, and_
from models import Admin
from utils.errors import DataNotFound


class AdminRepository:
    """ admin CRUD functionalities """

    @staticmethod
    def get(username=None, email=None):
        """ Query a customer by customer_id """

        # make sure one of the parameters was passed
        if not username and not email:
            raise DataNotFound(f"Customer not found, no detail provided")

        try:
            query = Admin.query
            if username:
                query = query.filter(
                    or_(Admin.username == username, Admin.email == username))
            if email:
                query = query.filter(
                    or_(Admin.email == email, Admin.username == email))

            admin = query.first()
            return admin
        except:
            print(sys.exc_info())
            raise DataNotFound(f"Admin with {username} not found")
