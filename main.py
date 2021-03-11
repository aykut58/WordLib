from flask import Flask,request,jsonify
from db import db,db_url
from model import User
from api import register_blueprint

app=Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]=db_url
db.init_app(app)
app.register_blueprint(register_blueprint)
with app.app_context():
    db.create_all()
app.run(host="0.0.0.0")