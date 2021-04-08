from flask import Flask
from app.security import hash_password
from app.repository import AdminRepository
from app import database
from app.model import Admin,User,Category
from app.exception import default_error_handler,http_error_handler
from werkzeug.exceptions import HTTPException

def load_config(app):
    app.config.from_object("app.config.Config")
    if app.config["ENV"]=="development":
        app.debug=True
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=True

def create_database(app):
    database.db.init_app(app)
    with app.app_context():
        database.create_database(app.config["SQLALCHEMY_DATABASE_URI"])
        database.db.create_all()

def create_admin(app):
    with app.app_context():
        admin_repository=AdminRepository()
        if admin_repository.count()==0:
            admin=Admin(username="admin",password=hash_password("1234"))
            admin_repository.add(admin)

def add_error_handlers(app):
    error_handlers=((Exception,default_error_handler),(HTTPException,http_error_handler))
    for exception,error_handler in error_handlers:
        app.register_error_handler(exception,error_handler)

app=Flask(__name__)
load_config(app)
create_database(app)
create_admin(app)
add_error_handlers(app)
from app import api