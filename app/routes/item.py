from app import app
from app.controllers import itemControllers
from app.controllers.authControllers import token_required
from flask import Blueprint

bp = Blueprint("item", __name__, url_prefix="/item")


@bp.route("/all", methods=["GET"])
def get_all_item():
    return itemControllers.get_all_item()


@bp.route("/<int:id>", methods=["GET"])
def get_one_item(id):
    return itemControllers.get_one_item(id)


@bp.route("/create", methods=["POST"])
@token_required
def create_item(current_user):
    return itemControllers.create_item(current_user)


@bp.route("/<int:id>/update", methods=["POST"])
@token_required
def update_item(id):
    return itemControllers.update_item(id)


@bp.route("/<int:id>", methods=["DELETE"])
@token_required
def delete_item(id):
    return itemControllers.delete_item(id)
