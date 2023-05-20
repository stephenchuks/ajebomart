"""
Category Blueprint
"""

from flask import Blueprint

from resources import CategoriesResource

CATEGORY_BLUEPRINT = Blueprint("category", __name__)

CATEGORY_BLUEPRINT.route(
    "/categories", methods=['GET'])(CategoriesResource.get_all)

CATEGORY_BLUEPRINT.route("/categories/<int:product_category_id>",
                         methods=['GET'])(CategoriesResource.get_category)

CATEGORY_BLUEPRINT.route(
    "/categories", methods=['POST'])(CategoriesResource.post)

CATEGORY_BLUEPRINT.route("categories/<int:category_id>",
                         methods=["DELETE"])(CategoriesResource.delete)

CATEGORY_BLUEPRINT.route("categories/<int:category_id>",
                         methods=["PUT"])(CategoriesResource.update)
