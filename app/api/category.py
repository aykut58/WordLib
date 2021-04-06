from flask import Blueprint,request,jsonify
from app.repository import CategoryRepository
from app.model import Category

category_blueprint=Blueprint("category",__name__)
category_repository=CategoryRepository()

def model_to_dict(model):
    if type(model) is list:
        return [each.to_dict() for each in model]
    else:
        return model.to_dict()

@category_blueprint.route("/category",methods=["GET"])
def get_all():
    return jsonify(model_to_dict(category_repository.get_all()))
    
@category_blueprint.route("/category/<id>",methods=["GET"])
def get_by_id(id):
    return jsonify(model_to_dict(category_repository.get_by_id(id)))

@category_blueprint.route("/category",methods=["POST"])
def add():
    data=request.get_json()
    category=Category(name=data["name"])
    return jsonify(model_to_dict(category_repository.add(category)))

@category_blueprint.route("/category",methods=["PUT"])
def update():
    data=request.get_json()
    category=Category(name=data["name"],id=data["id"])
    return jsonify(model_to_dict(category_repository.update(category)))

@category_blueprint.route("/category/<id>",methods=["DELETE"])
def delete_by_id(id):
    category_repository.delete_by_id(id)
    return jsonify({"Message":"Succesful"})