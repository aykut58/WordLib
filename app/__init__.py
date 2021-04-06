from flask import Flask
from app.db import db,create_database
from app.model import *
from app.security import token_filter,hash_password
from app.repository import AdminRepository

app=Flask(__name__)
app.config.from_object("app.config.Config")
if app.config["ENV"]=="development":
    app.debug=True
db.init_app(app)
app.before_request(token_filter)
with app.app_context():
    create_database(app.config["SQLALCHEMY_DATABASE_URI"])
    db.create_all()
    admin_repository=AdminRepository()
    if admin_repository.count()==0:
        admin=Admin(username="admin",password=hash_password("1234"))
        admin_repository.add(admin)
from app import api