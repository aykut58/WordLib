from flask import Blueprint,request,jsonify
from app.repository import AdminRepository
from app.security import hash_password,create_token

admin_login_blueprint=Blueprint("admin_login",__name__)
admin_repository=AdminRepository()

@admin_login_blueprint.route("/login/admin",methods=["POST"])
def admin_login():
    data=request.get_json()
    username=data["username"]
    password=data["password"]
    if "username" in data:
        username=data["username"]
        if admin_repository.exists_by_username(username):
            admin=admin_repository.get_by_username(username)
        else:
            return jsonify({"Error Message":"Username or Password is incorrect"}),400
    else:
        return jsonify({"Error Message":"username not found"}),400
    if admin.password==hash_password(password):
        return jsonify({"Token":create_token(admin)})
    return jsonify({"Error Message":"Username or Password is incorrect"}),400