from flask import Blueprint,request,jsonify
from app.repository import UserRepository
from app.security import create_token,hash_password
from app.model import User

register_blueprint=Blueprint("register",__name__)
user_repository=UserRepository()

@register_blueprint.route("/register",methods=["POST"])
def register():
    data=request.get_json()
    username=data["username"]
    password=data["password"]
    password2=data["password2"]
    email=data["email"]
    if password==password2:
        if not user_repository.exists_by_username(username):
            if not user_repository.exists_by_email(email):
                password=hash_password(password)
                user=User(username=username,password=password,email=email,is_active=True)
                user=user_repository.add(user)
                #send_activation_mail(email,user)
                return jsonify({"Message":"Successful"})
            return jsonify({"Error Message":"Another User uses this email"}),400
        return jsonify({"Error Message":"Another User uses this username"}),400
    return jsonify({"Error Message":"Password are not same"}),400