"""Authentication Resource"""
import sys
import os
from flask import jsonify, abort
from flask_restful import Resource
from flask_restful.reqparse import Argument
from repositories import CustomerRepository, AdminRepository
from utils import parse_params
from utils.errors import DataNotFound, DuplicateData


class AuthResource(Resource):
    """ methods relative to the authorization """

    @staticmethod
    @parse_params(
        Argument("username", location="json",
                 help="The username/email of the customer."),
        Argument("password", location="json",
                 help="The password of the customer.")
    )
    def login(username, password):
        """ Login a customer"""

        ady = os.getenv("ADMIN_USERNAME", '')
        print(ady)
        try:
            if not ady in username:
                customer = CustomerRepository.get(username=username)
                if not customer.check_password(password):
                    abort(401, "Username or Password is incorrect")
                return jsonify({"data": customer.json})
            else:
                admin = AdminRepository.get(username=username)
                if not admin.check_password(password):
                    abort(401, "Username or Password is incorrect")
                return jsonify({"data": admin.json})
        except DataNotFound:
            abort(401, "Username or Password is incorrect")
        except:
            abort(500)
