from app import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class Account(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), index=True, unique=True)
    admin = db.Column(db.Boolean)
    email = db.Column(db.String(255), index=True, unique=True)
    phone_number = db.Column(db.String(20), index=True, unique=True)
    address = db.Column(db.String(255))
    password_hash = db.Column(db.String(255))
    orders = db.relationship("Order", backref="owner", lazy="dynamic")
    create_at = db.Column(db.DateTime)
    update_at = db.Column(db.DateTime)

    def __repr__(self):
        return "<User {}>".format(self.name)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password) 

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def from_dict(self, data):
        for field in ["name", "email", "phone_number", "address"]:
            if field in data:
                setattr(self, field, data[field])
        if "password" in data:
            self.set_password(data["password"])


class Item(db.Model):
    id = db.Column(db.Integer, index=True, primary_key=True)
    name = db.Column(db.String(255))
    price = db.Column(db.Float)
    stock = db.Column(db.Integer)
    collection = db.Column(db.String(255))
    create_at = db.Column(db.DateTime)
    update_at = db.Column(db.DateTime)
    carts = db.relationship("ItemCart", backref="item", lazy="dynamic")

    def __repr__(self):
        return "<Item {}>".format(self.name)
    
    def from_dict(self, data):
        for field in ["name", "price", "stock", "collection"]:
            if field in data:
                setattr(self, field, data[field])


class Order(db.Model):
    id = db.Column(db.Integer, index=True, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey("account.id"))
    total_price = db.Column(db.Float)
    create_at = db.Column(db.DateTime)
    update_at = db.Column(db.DateTime)
    items = db.relationship("ItemCart", backref="order", lazy="dynamic")

    def __repr__(self):
        return "<Total price {}>".format(self.total_price)


class ItemCart(db.Model):
    id = db.Column(db.Integer, index=True, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey("order.id"))
    item_id = db.Column(db.Integer, db.ForeignKey("item.id"))
    amount = db.Column(db.Integer)

    def __repr__(self):
        return "<Item {}, amount {}>".format(self.item_id, self.amount)