from flask import request,jsonify
from app.repository import UserRepository
from app.security import hash_password,create_token
from app import app
from werkzeug.exceptions import BadRequest,Unauthorized

user_repository=UserRepository()

@app.route("/login",methods=["POST"])
def login():
    data=request.get_json()
    if "password" not in data:
        raise BadRequest("Password was not Given")
    password=data["password"]
    if "email" in data:
        email=data["email"]
        if user_repository.exists_by_email(email):
            user=user_repository.get_by_email(email)
        else:
            raise Unauthorized("Email or Password is incorrect")
    elif "username" in data:
        username=data["username"]
        if user_repository.exists_by_username(username):
            user=user_repository.get_by_username(username)
        else:
            raise Unauthorized("Username or Password is incorrect")
    else:
        raise BadRequest("Neither username nor email was given")
    if user.password==hash_password(password):
        if user.is_active:
            return jsonify({"Token":create_token(user)})
        else:
            raise Unauthorized("Inactivated Account")
    raise Unauthorized("Email or Username or Password is incorrect")