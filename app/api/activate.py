from flask import Blueprint,jsonify
from app.repository import UserRepository

user_repository=UserRepository()
activate_blueprint=Blueprint("activate",__name__)

@activate_blueprint.route("/activate/<id>",methods=["GET"])
def activate_user(id):
    if user_repository.exists_by_id(id):
        user=user_repository.get_by_id(id)
        user.is_active=True
        user_repository.update(user)
        return jsonify({"Message":"Succesful"})
    else:
        return jsonify({"Message":"User not Found"}),400