import os


class Config(object):
    SECRET_KEY = os.environ.get("SECRET_KEY") or ("dev")
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://dongocanh96:Ngocanh8#@localhost/emartdb"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
