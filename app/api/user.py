from flask import Blueprint
from app.repository import UserRepository
from .model_to_json import model_to_json

user_blueprint=Blueprint("user",__name__)
user_repository=UserRepository()

@user_blueprint.route("/user",methods=["GET"])
def get_all():
    return model_to_json(user_repository.get_all())

@user_blueprint.route("/user/<id>",methods=["GET"])
def get_by_id(id):
    return model_to_json(user_repository.get_by_id(id))