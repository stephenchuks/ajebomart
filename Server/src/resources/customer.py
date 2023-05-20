"""Customer Resource"""
from flask import jsonify, abort
from flask_restful import Resource
from flask_restful.reqparse import Argument
from repositories import CustomerRepository
from utils import parse_params
from utils.errors import DataNotFound


class CustomerResource(Resource):
    """ Customer Resource Definition """

    @staticmethod
    def get_one(customer_id):
        """ get Customer Information """

        try:
            customer = CustomerRepository.get(customer_id=customer_id)
            if not customer:
                return jsonify({"message": f" customer with the id {customer_id} not found"})
            data = {
                "id": customer.id,
                "username": customer.username,
                "first_name": customer.first_name,
                "last_name": customer.last_name,
                "email": customer.email,
                "phone": customer.phone,
                "country": customer.country,
                "state": customer.state,
                "city": customer.city,
                "street_name": customer.street_name,
                "zipcode": customer.zipcode,
            }
            return jsonify({"data": data})
        except DataNotFound as e:
            abort(404, e.message)
        except Exception:
            abort(500)

    @staticmethod
    def get_all():
        """ get all customers"""
        customers = CustomerRepository.getAll()
        return jsonify({"data": customers})

    @staticmethod
    @parse_params(
        Argument("first_name", location="json",
                 help="The first_name of the customer."),
        Argument("last_name", location="json",
                 help="The last_name of the customer."),
        Argument("phone", location="json",
                 help="The phone of the customer.")
    )
    def update_customer(customer_id, last_name, first_name, phone):
        """ Update a customer records"""
        customer = CustomerRepository().update(
            customer_id=customer_id, last_name=last_name, first_name=first_name, phone=phone
        )
        return jsonify({"data": customer.json})

    @staticmethod
    @parse_params(
        Argument("first_name", location="json", required=True,
                 help="The first_name of the customer."),
        Argument("last_name", location="json", required=True,
                 help="The last_name of the customer."),
        Argument("username", location="json", required=True,
                 help="The username of the customer."),
        Argument("email", location="json", required=True,
                 help="The email of the customer."),
        Argument("phone", location="json", required=True,
                 help="The phone of the customer."),
        Argument("password", location="json", required=True,
                 help="The password of the customer."),
        Argument("country", location="json", required=True,
                 help="The country of the customer."),
        Argument("state", location="json", required=True,
                 help="The state of the customer."),
        Argument("city", location="json", required=True,
                 help="The city of the customer."),
        Argument("street_name", location="json", required=True,
                 help="The street_name of the customer."),
        Argument("zipcode", location="json", required=True,
                 help="The zipcode of the customer."),
    )
    def post(username, last_name, first_name, phone, email, city,
             zipcode, street_name, password, state, country):
        """ Create a customer """
        # TODO: Check duplicates

        cus_check = CustomerRepository.get(username=username)
        if cus_check:
            return jsonify({"message": f" customer exits"})

        new_customer = CustomerRepository.create(
            username=username, last_name=last_name, first_name=first_name,
            phone=phone, email=email, city=city, state=state,
            zipcode=zipcode, street_name=street_name,
            password=password, country=country)

        new_customer.set_password(password)

        if len(password) < 6:
            return jsonify({"error": "Password must be at least 6 characters"}), 400
        customer = new_customer.save()
        return jsonify({"data": customer.json})
