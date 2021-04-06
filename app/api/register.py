from flask import request,jsonify
from app.repository import UserRepository
from app.security import hash_password
from app.model import User
from app import app
from werkzeug.exceptions import Conflict

user_repository=UserRepository()

@app.route("/register",methods=["POST"])
def register():
    data=request.get_json()
    username=data["username"]
    password=data["password"]
    email=data["email"]
    if not user_repository.exists_by_username(username):
        if not user_repository.exists_by_email(email):
            password=hash_password(password)
            user=User(username=username,password=password,email=email,is_active=True)
            user=user_repository.add(user)
            #send_activation_mail(email,user)
            return jsonify({"Message":"Successful"})
        raise Conflict("Another User uses this email")
    raise Conflict("Another User uses this username")