from flask import Flask, jsonify
from flask.blueprints import Blueprint
from flask_migrate import Migrate
from sqlalchemy.exc import IntegrityError
from flask_cors import CORS
import os

import config
import routes
from models import db, Admin


server = Flask(__name__)
# server = Flask(__name__, static_folder='../../client/build', static_url_path='/')
CORS(server)
# cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

server.debug = config.DEBUG
server.config["SQLALCHEMY_DATABASE_URI"] = config.DB_URI
server.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = config.SQLALCHEMY_TRACK_MODIFICATIONS  # noqa
db.init_app(server)
db.app = server
db.create_all()
migrate = Migrate(server, db)

username = os.getenv("ADMIN_USERNAME", '')
email = os.getenv("ADMIN_EMAIL", '')
first_name = os.getenv("ADMIN_FIRSTNAME", '')
last_name = os.getenv("ADMIN_LASTNAME", '')
password = os.getenv("ADMIN_PASSWORD", '')
phone = os.getenv("ADMIN_PHONE", '')

try:
    adminx = Admin(username=username, first_name=first_name, last_name=last_name,
                   email=email, phone=phone)
    adminx.set_password(password)
    adminx.save()
except IntegrityError as e:
    pass
except Exception:
    pass

for blueprint in vars(routes).values():
    if isinstance(blueprint, Blueprint):
        server.register_blueprint(
            blueprint, url_prefix=config.APPLICATION_ROOT)

""" Error handling """


# error handler for 422
@server.errorhandler(422)
def unprocessable(error):
    return jsonify({
        "success": False,
        "error": 422,
        "message": "unprocessable"
    }), 422


# error handler for 400
@server.errorhandler(400)
def bad_request(error):
    print(error)
    return jsonify({
        "success": False,
        "error": 400,
        "message": error.description
    }), 400


# error handler for 401
@server.errorhandler(401)
def unauthorized(error):
    return jsonify({
        "success": False,
        "error": 401,
        "message": error.description
    }), 401


# error handler for 403
@server.errorhandler(403)
def forbidden(error):
    return jsonify({
        "success": False,
        "error": 403,
        "message": error.description
    }), 403


# error handler for 404
@server.errorhandler(404)
def not_found(error):
    return jsonify({
        "success": False,
        "error": 404,
        "message": error.description
    }), 404


# error handler for 500
@server.errorhandler(500)
def internal_server_error(error):
    print({"error": error})
    return jsonify({
        "success": False,
        "error": 500,
        "message": "Internal server error"
    }), 500


if __name__ == "__main__":
    server.debug = True
    server.run(host=config.HOST, port=config.PORT)
