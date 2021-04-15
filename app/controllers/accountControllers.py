from flask import request, jsonify
from datetime import datetime, timedelta
from app import db
from app.models.models import Account


def get_all_users(current_user):
    if not current_user.admin:
        return jsonify({"message": "You're not allowed"})
    users = Account.query.all()
    output = []

    for user in users:
        user_data = {}
        user_data["id"] = user.id
        user_data["name"] = user.name
        user_data["role"] = "Admin" if user.admin else "Customer"
        user_data["phone_number"] = user.phone_number
        output.append(user_data)
    
    return jsonify({"user": output})


def get_one_user(current_user, id):
    if not current_user.admin and current_user.id != id:
        return jsonify({"message": "You're not allowed"})
    user = Account.query.filter_by(id=id).first()

    if not user:
        return jsonify({"message": "User is not found!"})

    user_data = {}
    user_data["id"] = user.id
    user_data["name"] = user.name
    user_data["role"] = "Admin" if user.admin else "Customer"
    user_data["phone_number"] = user.phone_number

    return jsonify({"user": user_data})


def delete_user(current_user, id):
    if not current_user.admin:
        return jsonify({"message": "You're not allowed"})
    user = Account.query.filter_by(id=id).first()

    if not user:
        return jsonify({"message" : "No user found!"})

    db.session.delete(user)
    db.session.commit()

    return jsonify({"message" : "The user has been deleted!"})

def update_info(current_user, id):

    if not current_user.admin or current_user.id != id:
        return jsonify({"message": "You're not allowed!"})
    
    user = Account.query.filter_by(id=id).first()
    data = request.get_json()
    if "name" in data:
        user1 = Account.query.filter_by(name=data["name"]).first()
        if user1 is not None and user1 != user:
            return jsonify({"message": "Some fields are duplicated!"})
    
    if "email" in data:
        user2 = Account.query.filter_by(name=data["email"]).first()
        if user2 is not None and user2 != user:
            return jsonify({"message": "Some fields are duplicated!"})
    
    if "phone_number" in data:
        user3 = Account.query.filter_by(name=data["phone_number"]).first()
        if user3 is not None and user3 != user:
            return jsonify({"message": "Some fields are duplicated!"})

    user.from_dict(data)
    user.update_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    db.session.commit()

    return jsonify({"message": "Update success!"})