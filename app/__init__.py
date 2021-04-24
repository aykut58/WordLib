from flask import Flask
from app.security import hash_password
from app.repository import AdminRepository
from app import database
from app.model import Admin,User,Category,Word
from app.api import blueprint
from app.exception import error_handler_blueprint
from .serializer import marshmallow

def init_app():
    create_database()
    create_admin()
    marshmallow.init_app(app)

def create_database():
    database.db.init_app(app)
    with app.app_context():
        database.create_database(app.config["SQLALCHEMY_DATABASE_URI"])
        database.db.create_all()

def create_admin():
    with app.app_context():
        admin_repository=AdminRepository()
        if admin_repository.count()==0:
            admin=Admin(username="admin",password=hash_password("1234"))
            admin_repository.add(admin)

app=Flask(__name__)
app.register_blueprint(blueprint)
app.register_blueprint(error_handler_blueprint)