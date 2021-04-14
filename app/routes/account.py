from app.controllers import accountControllers
from app.controllers.authControllers import token_required
from flask import Blueprint

bp = Blueprint("account", __name__, url_prefix="/account")

@bp.route("/all", methods=["GET"])
@token_required
def get_all_users(current_user):
    return accountControllers.get_all_users(current_user)


@bp.route("/<int:id>", methods=["GET"])
@token_required
def get_one_user(current_user, id):
    return accountControllers.get_one_user(current_user, id)


@bp.route("<int:id>/update", methods=["POST"])
@token_required
def update_info(current_user, id):
    return accountControllers.update_info(current_user, id)


@bp.route("/<int:id>", methods=["DELETE"])
@token_required
def delete_user(current_user, id):
    return accountControllers.delete_user()