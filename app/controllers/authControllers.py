from flask import request, jsonify, make_response, session
import jwt
from functools import wraps
from datetime import datetime, timedelta
from app import app, db
from app.models.models import Account


def token_required(f):
    @wraps(f)
    def decorated(*arg, **kwargs):
        token = None

        if "x-access-token" in request.headers:
            token = request.headers["x-access-token"]
        if not token:
            return jsonify({"message": "Token is missing"}), 401

        try:
            data = jwt.decode(token, app.config["SECRET_KEY"])
            current_user = Account.query.filter_by(id=data["id"]).first()
        except:
            return jsonify({"message": "Token is invalid!"}), 401
        
        return f(current_user, *arg, **kwargs)

    return decorated


def create_user():
    data = request.get_json()
    user1 = Account.query.filter_by(name=data["name"]).first()
    user2 = Account.query.filter_by(name=data["email"]).first()
    user3 = Account.query.filter_by(name=data["phone_number"]).first()

    if user1 is None and user2 is None and user3 is None:

        if "key" in data.keys() and data["key"] == "599s1Z]76G4MVMX":
            user = Account(name=data["name"], admin=True, email=data["email"],
                        phone_number=data["phone_number"], address=data["address"],
                        create_at=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                        update_at=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    )
            user.set_password(data["password"])
            db.session.add(user)
            db.session.commit()
        else:
            user = Account(name=data["name"], admin=False, email=data["email"],
                        phone_number=data["phone_number"], address=data["address"],
                        create_at=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                        update_at=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    )
            user.set_password(data["password"])
            db.session.add(user)
            db.session.commit()

        return jsonify({"message": "New user is created!"})
    else:
        return jsonify({"message": "Information in some fields has been used"})


def login():
    auth = request.authorization

    if not auth or not auth.username or not auth.password:
        return make_response("Could not verify", 401, {"WWW-Authenticate" : "Basic realm='Login required!'"})

    user = Account.query.filter_by(name=auth.username).first()

    if not user:
        return make_response("Could not verify", 401, {"WWW-Authenticate" : "Basic realm='Login required!'"})

    if user.check_password(auth.password):
        token = jwt.encode({"id" : user.id, "exp" : datetime.utcnow() + timedelta(minutes=30)}, app.config["SECRET_KEY"])

        return jsonify({"token" : token.decode("UTF-8")})

    return make_response("Could not verify", 401, {"WWW-Authenticate" : "Basic realm='Login required!'"})


def logout():
    pass
