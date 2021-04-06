from flask import request,jsonify
from app.repository import AdminRepository
from app.security import hash_password,create_token
from app import app
from werkzeug.exceptions import BadRequest,Unauthorized

admin_repository=AdminRepository()

@app.route("/login/admin",methods=["POST"])
def admin_login():
    data=request.get_json()
    if "password" not in data:
        raise BadRequest("Password was not Given")
    if "username" not in data:
        raise BadRequest("Username was not Given")
    username=data["username"]
    password=data["password"]
    if admin_repository.exists_by_username(username):
        admin=admin_repository.get_by_username(username)
    else:
        raise Unauthorized("Username or Password is incorrect")
    if admin.password==hash_password(password):
        return jsonify({"Token":create_token(admin)})
    raise Unauthorized("Username or Password is incorrect")