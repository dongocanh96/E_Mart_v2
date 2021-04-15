from flask import request, jsonify
from datetime import datetime, timedelta
from app import app, db
from app.models.models import Item


def get_all_item():
    output = []
    items = Item.query.all()

    for item in items:
        item_data = {}
        item_data["id"] = item.id
        item_data["name"] = item.name
        item_data["price"] = item.price
        item_data["stock"] = item.stock
        item_data["collection"] = item.collection
        output.append(item_data)
    
    return jsonify({"item": output})


def get_one_item(id):

    item = Item.query.filter_by(id=id).first()

    if not item:
        return jsonify({"message": "Item is not found!"})
    
    item_data = {}
    item_data["id"] = item.id
    item_data["name"] = item.name
    item_data["price"] = item.price
    item_data["stock"] = item.stock
    item_data["collection"] = item.collection

    return jsonify({"item": item_data})


def create_item(current_user):
    if not current_user.admin:
        return jsonify({"message": "You're not allowed!"})

    data = request.get_json()
    item1 = Item.query.filter_by(name=data["name"]).first()

    if item1:
        return jsonify({"message": "Item's name already exist!"})
    
    item = Item(name=data["name"], price=data["price"], stock=data["stock"],
                collection=data["collection"],
                create_at=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                update_at=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            )
    db.session.add(item)
    db.session.commit()

    return jsonify({"message": "New item is created!"})


def update_item(id):
    item = Item.query.filter_by(id=id).first()
    data = request.get_json()
    
    if "name" in data:
        item1 = Item.query.filter_by(name=data["name"]).first()
        if item1 is not None and item1 != item:
            return jsonify({"message": "Some fields are duplicated!"})
    
    item.from_dict(data)
    item.update_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    db.session.commit()

    return jsonify({"message": "Update success!"})


def delete_item():
    item = Item.query.filter_by(id=id).first()

    if not item:
        return jsonify({"message" : "No item found!"})
    
    db.session.delete(item)
    db.session.commit()

    return jsonify({"message" : "The item has been deleted!"})
