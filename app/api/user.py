from flask import Blueprint,request,jsonify
from app.repository import UserRepository

user_blueprint=Blueprint("user",__name__)
user_repository=UserRepository()

def model_to_dict(model):
    if type(model) is list:
        return [each.to_dict() for each in model]
    else:
        return model.to_dict()

@user_blueprint.route("/user",methods=["GET"])
def get_all():
    return jsonify(model_to_dict(user_repository.get_all()))

@user_blueprint.route("/user/<id>",methods=["GET"])
def get_by_id(id):
    return jsonify(model_to_dict(user_repository.get_by_id(id)))