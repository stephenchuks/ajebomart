""" A repository for Customer """
import sys
from sqlalchemy import or_, and_
from models import Customer
from utils.errors import DataNotFound, DuplicateData, InternalServerError
from sqlalchemy.exc import IntegrityError, DataError


class CustomerRepository:
    """ Customer CRUD functionalities """

    @staticmethod
    def get(customer_id=None, username=None, email=None):
        """ Query a customer by customer_id """

        # make sure one of the parameters was passed
        if not customer_id and not username and not email:
            raise DataNotFound(f"Customer not found, no detail provided")

        try:
            query = Customer.query
            if customer_id:
                query = query.filter(Customer.id == customer_id)
            if username:
                query = query.filter(
                    or_(Customer.username == username, Customer.email == username))
            if email:
                query = query.filter(
                    or_(Customer.email == email, Customer.username == email))

            customer = query.first()
            return customer
        except:
            print(sys.exc_info())
            raise DataNotFound(f"Customer with {customer_id} not found")

    @staticmethod
    def getAll():
        """ Query all customers"""
        customers = Customer.query.all()
        if not customers:
            return []
        data = []
        for cus in customers:
            data.append({
                "id": cus.id,
                "username": cus.username,
                "first_name": cus.first_name,
                "last_name": cus.last_name,
                "email": cus.email,
                "phone": cus.phone,
                "country": cus.country,
                "state": cus.state,
                "city": cus.city,
                "street_name": cus.street_name,
                "created_at": cus.created_at,
                "zipcode": cus.zipcode,
            })

        return data

    def update(self, customer_id, **args):
        """ Update customers records """
        customer = self.get(customer_id)
        if 'phone' in args and args['phone'] is not None:
            customer.phone = args['phone']

        if 'last_name' in args and args['last_name'] is not None:
            customer.last_name = args['last_name']

        if 'first_name' in args and args['first_name'] is not None:
            customer.first_name = args['first_name']

        return customer.save()

    @staticmethod
    def create(username, last_name, first_name, password,
               phone, email, city=None, state=None,
               zipcode=None, street_name=None,
               country=None):
        """ Create a new customer """
        try:
            customer = Customer(username=username, first_name=first_name, last_name=last_name,
                                email=email, phone=phone, country=country, state=state, city=city,
                                street_name=street_name, zipcode=zipcode)
            customer.set_password(password)

            return customer.save()
        except IntegrityError as e:
            message = e.orig.diag.message_detail
            raise DuplicateData(message)
        except Exception:
            raise InternalServerError
