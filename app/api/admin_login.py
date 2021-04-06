from flask import request,jsonify
from app.repository import AdminRepository
from app.security import hash_password,create_token
from app import app
from app.exception import AuthenticationException

admin_repository=AdminRepository()

@app.route("/login/admin",methods=["POST"])
def admin_login():
    data=request.get_json()
    username=data["username"]
    password=data["password"]
    if "username" in data:
        username=data["username"]
        if admin_repository.exists_by_username(username):
            admin=admin_repository.get_by_username(username)
        else:
            raise AuthenticationException("Username or Password is incorrect",code=401)
    else:
        raise AuthenticationException("Username not Found",code=400)
    if admin.password==hash_password(password):
        return jsonify({"Token":create_token(admin)})
    raise AuthenticationException("Username or Password is incorrect",code=401)