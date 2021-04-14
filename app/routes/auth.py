from app.controllers import authControllers
from flask import Blueprint

bp = Blueprint("auth", __name__, url_prefix="/auth")

@bp.route("/create-user", methods=["POST"])
def create_user():
    return authControllers.create_user()


@bp.route("/login")
def login():
    return authControllers.login()


@bp.route("/logout")
def logout():
    pass
