from flask import Blueprint,request,jsonify
from repository import UserRepository,CategoryRepository,AdminRepository
from model import User,Category
from security import create_token,hash_password
from send_email import send_activation_mail

user_blueprint=Blueprint("user",__name__)
category_blueprint=Blueprint("category",__name__)
register_blueprint=Blueprint("register",__name__)
admin_blueprint=Blueprint("admin",__name__)
user_repository=UserRepository()
category_repository=CategoryRepository()
admin_repository=AdminRepository()

def model_to_json(model):
    if type(model) is list:
        return [each.to_json() for each in model]
    else:
        return model.to_json()

class Register:
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
                    user=user_repository.add(user)
                    send_activation_mail(email,user)
                    return jsonify({"Message":"Successful"})
                return jsonify({"Error Message":"Another User uses this email"}),400
            return jsonify({"Error Message":"Another User uses this username"}),400
        return jsonify({"Error Message":"Password are not same"}),400

    @register_blueprint.route("/activate/<id>",methods=["GET"])
    def activate_user(id):
        if user_repository.exists_by_id(id):
            user=user_repository.get_by_id(id)
            user.is_active=True
            user_repository.update(user)
            return jsonify({"Message":"Succesful"})
        else:
            return jsonify({"Message":"User not Found"}),400

class AdminLogin:

    @admin_blueprint.route("/admin-login",methods=["POST"])
    def admin_login():
        data=request.get_json()
        username=data["username"]
        password=data["password"]
        if "username" in data:
            username=data["username"]
            if admin_repository.exists_by_username(username):
                admin=admin_repository.get_by_username(username)
            else:
                return jsonify({"Error Message":"Email or Username or Password is incorrect"}),400
        else:
            return jsonify({"Error Message":"Neither username nor email was given"}),400
        if admin.password==hash_password(password):
            if admin.is_active:
                return jsonify({"Token":create_token(admin.username)})
            else:
                return jsonify({"Error Message":"Inactivated Account"}),400
        return jsonify({"Error Message":"Email or Username or Password is incorrect"}),400

class CategoryAPI:
    
    @category_blueprint.route("/category",methods=["GET"])
    def get_all():
        return jsonify(model_to_json(category_repository.get_all()))
    
    @category_blueprint.route("/category/<id>",methods=["GET"])
    def get_by_id(id):
        return jsonify(model_to_json(category_repository.get_by_id(id)))
    
    @category_blueprint.route("/category",methods=["POST"])
    def add():
        data=request.get_json()
        category=Category(name=data["name"])
        return jsonify(model_to_json(category_repository.add(category)))
    
    @category_blueprint.route("/category",methods=["PUT"])
    def update():
        data=request.get_json()
        category=Category(name=data["name"],id=data["id"])
        return jsonify(model_to_json(category_repository.update(category)))
    
    @category_blueprint.route("/category/<id>",methods=["DELETE"])
    def delete_by_id(id):
        category_repository.delete_by_id(id)
        return jsonify({"Message":"Succesful"})

class UserAPI:
    
    @user_blueprint.route("/user",methods=["GET"])
    def get_all():
        return jsonify(model_to_json(user_repository.get_all()))
    
    @user_blueprint.route("/user/<id>",methods=["GET"])
    def get_by_id(id):
        return jsonify(model_to_json(user_repository.get_by_id(id)))