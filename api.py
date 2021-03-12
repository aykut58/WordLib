from flask import Blueprint,request,jsonify
from repository import UserRepository
from model import User
from security import create_token,hash_password
from send_email import send_email

register_blueprint=Blueprint("register",__name__)
user_repository=UserRepository()

@register_blueprint.route("/login",methods=["POST"])
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
            return jsonify({"Token":create_token(user.username)})
        else:
            return jsonify({"Error Message":"Inactivated Account"}),400
    return jsonify({"Error Message":"Email or Username or Password is incorrect"}),400

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
                user=User(username=username,password=password,email=email,is_active=False)
                user_repository.add(user)
                content="""
                    <h1>Wordlib</h1>
                    <a href='http://34.201.148.42:5000/activate/"""+username+"""'>Click Here To Activate</a>
                """
                send_email(email,content,"Email Confirmation")
                return jsonify({"Message":"Successful"})
            return jsonify({"Error Message":"Another User uses this email"}),400
        return jsonify({"Error Message":"Another User uses this username"}),400
    return jsonify({"Error Message":"Password are not same"}),400

@register_blueprint.route("/activate/<username>",methods=["GET"])
def activate_user(username):
    if user_repository.exists_by_username(username):
        user=user_repository.get_by_username(username)
        user.is_active=True
        user_repository.update(user)
        return jsonify({"Message":"Succesful"})
    else:
        return jsonify({"Message":"Username not Found"}),400