from flask import request,jsonify
from app.repository import CategoryRepository
from app.model import Category
from .model_to_json import model_to_json
from app import app
from app.security import authentication

category_repository=CategoryRepository()

class CategoryAPI:

    @app.route("/category",methods=["GET"])
    def get_all_categories():
        authentication("*")
        return model_to_json(category_repository.get_all())

    @app.route("/category/<id>",methods=["GET"])
    def get_category_by_id(id):
        authentication("*")
        return model_to_json(category_repository.get_by_id(id))

    @app.route("/category",methods=["POST"])
    def add_category():
        authentication("Admin")
        data=request.get_json()
        category=Category(name=data["name"])
        return model_to_json(category_repository.add(category))

    @app.route("/category",methods=["PUT"])
    def update_category():
        authentication("Admin")
        data=request.get_json()
        category=Category(name=data["name"],id=data["id"])
        return model_to_json(category_repository.update(category))

    @app.route("/category/<id>",methods=["DELETE"])
    def delete_category_by_id(id):
        authentication("Admin")
        category_repository.delete_by_id(id)
        return jsonify({"Message":"Succesful"})