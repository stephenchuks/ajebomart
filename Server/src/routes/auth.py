"""Authentication Blueprint"""
from flask import Blueprint

from resources import AuthResource

AUTH_BLUEPRINT = Blueprint("auth", __name__)

AUTH_BLUEPRINT.route(
    "/login_customer", methods=['POST'])(AuthResource.login)
AUTH_BLUEPRINT.route(
    "/login_admin", methods=['POST'])(AuthResource.login)