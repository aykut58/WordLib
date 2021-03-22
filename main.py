from flask import Flask
from db import db,db_url
from model import User,Category,Admin
from api import register_blueprint,category_blueprint,user_blueprint,admin_blueprint
from security import token_filter,hash_password
from repository import AdminRepository
import sys

app=Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]=db_url
db.init_app(app)
app.register_blueprint(register_blueprint)
app.register_blueprint(category_blueprint)
app.register_blueprint(user_blueprint)
app.register_blueprint(admin_blueprint)
app.before_request(token_filter)
with app.app_context():
    db.create_all()
    admin_repository=AdminRepository()
    if admin_repository.count()==0:
        admin=Admin(username="admin",password=hash_password("1234"))
        admin_repository.add(admin)
if len(sys.argv)>1:
    app.run(host="0.0.0.0")
else:
    app.run(debug=True)