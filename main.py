from flask import Flask
from db import db,db_url
from model import User,Category
from api import register_blueprint,category_blueprint,user_blueprint
from security import token_filter
import sys

app=Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]=db_url
db.init_app(app)
app.register_blueprint(register_blueprint)
app.register_blueprint(category_blueprint)
app.register_blueprint(user_blueprint)
app.before_request(token_filter)
with app.app_context():
    db.create_all()
if len(sys.argv)>1:
    app.run(host="0.0.0.0")
else:
    app.run(debug=True)