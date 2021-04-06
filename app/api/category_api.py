from flask import Blueprint,request,jsonify
from app.repository import CategoryRepository
from app.model import Category
from .model_to_json import model_to_json
from sqlalchemy.orm.exc import NoResultFound

category_blueprint=Blueprint("category",__name__)
category_repository=CategoryRepository()

@category_blueprint.route("/category",methods=["GET"])
def get_all():
    return model_to_json(category_repository.get_all())

@category_blueprint.route("/category/<id>",methods=["GET"])
def get_by_id(id):
    return model_to_json(category_repository.get_by_id(id))

@category_blueprint.route("/category",methods=["POST"])
def add():
    data=request.get_json()
    category=Category(name=data["name"])
    return model_to_json(category_repository.add(category))

@category_blueprint.route("/category",methods=["PUT"])
def update():
    data=request.get_json()
    category=Category(name=data["name"],id=data["id"])
    return model_to_json(category_repository.update(category))

@category_blueprint.route("/category/<id>",methods=["DELETE"])
def delete_by_id(id):
    category_repository.delete_by_id(id)
    return jsonify({"Message":"Succesful"})