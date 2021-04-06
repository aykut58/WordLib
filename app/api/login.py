from flask import request,jsonify
from app.repository import UserRepository
from app.security import hash_password,create_token
from app import app

user_repository=UserRepository()

@app.route("/login",methods=["POST"])
def login():
    data=request.get_json()
    password=data["password"]
    if "email" in data:
        email=data["email"]
        if user_repository.exists_by_email(email):
            user=user_repository.get_by_email(email)
        else:
            return jsonify({"Error Message":"Email or Username or Password is incorrect"}),400
    elif "username" in data:
        username=data["username"]
        if user_repository.exists_by_username(username):
            user=user_repository.get_by_username(username)
        else:
            return jsonify({"Error Message":"Email or Username or Password is incorrect"}),400
    else:
        return jsonify({"Error Message":"Neither username nor email was given"}),400
    if user.password==hash_password(password):
        if user.is_active:
            return jsonify({"Token":create_token(user)})
        else:
            return jsonify({"Error Message":"Inactivated Account"}),400
    return jsonify({"Error Message":"Email or Username or Password is incorrect"}),400