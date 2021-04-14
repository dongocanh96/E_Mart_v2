from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
from flask_login import LoginManager
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)
login = LoginManager(app)
login.login_view = "login"
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app.models import models
from app.routes import account, auth, item

app.register_blueprint(account.bp)
app.register_blueprint(auth.bp)
app.register_blueprint(item.bp)
