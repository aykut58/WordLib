from flask import jsonify,request,Blueprint
from werkzeug.exceptions import BadRequest,Unauthorized,Conflict
from app.repository import UserRepository,AdminRepository,CategoryRepository
from app.security import authentication,hash_password,create_token,is_token_valid
from app.model import Category,User
from .serializer import WordSerializer
from .service import WordService

blueprint=Blueprint("blueprint",__name__)
user_repository=UserRepository()
admin_repository=AdminRepository()
category_repository=CategoryRepository()
word_serializer=WordSerializer()
words_serializer=WordSerializer(many=True)
word_service=WordService()

@blueprint.route("/word")
def get_all_words():
    return words_serializer.jsonify(word_service.get_all())

@blueprint.route("/word/<id>")
def get_word_by_id(id):
    return word_serializer.jsonify(word_service.get_by_id(id))

def model_to_json(model):
    if type(model) is list:
        return jsonify([each.to_dict() for each in model])
    else:
        return jsonify(model.to_dict())

@blueprint.route("/activate/<id>",methods=["GET"])
def activate_user(id):
    if user_repository.exists_by_id(id):
        user=user_repository.get_by_id(id)
        user.is_active=True
        user_repository.update(user)
        return jsonify({"Message":"Succesful"})
    else:
        raise BadRequest("User not Found by this id")

@blueprint.route("/login/admin",methods=["POST"])
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

@blueprint.route("/register",methods=["POST"])
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

@blueprint.route("/login",methods=["POST"])
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

@blueprint.route("/tokencheck",methods=["POST"])
def token_check():
    if "token" in request.headers:
        return jsonify({"Result":is_token_valid(request.headers.get("token"))})
    else:
        raise BadRequest("Token was not given")

@blueprint.route("/category",methods=["GET"])
def get_all_categories():
    authentication("*")
    return model_to_json(category_repository.get_all())

@blueprint.route("/category/<id>",methods=["GET"])
def get_category_by_id(id):
    authentication("*")
    return model_to_json(category_repository.get_by_id(id))

@blueprint.route("/category",methods=["POST"])
def add_category():
    authentication("Admin")
    data=request.get_json()
    category=Category(name=data["name"])
    return model_to_json(category_repository.add(category))

@blueprint.route("/category",methods=["PUT"])
def update_category():
    authentication("Admin")
    data=request.get_json()
    category=Category(name=data["name"],id=data["id"])
    return model_to_json(category_repository.update(category))

@blueprint.route("/category/<id>",methods=["DELETE"])
def delete_category_by_id(id):
    authentication("Admin")
    category_repository.delete_by_id(id)
    return jsonify({"Message":"Succesful"})

@blueprint.route("/user",methods=["GET"])
def get_all_users():
    authentication("*")
    return model_to_json(user_repository.get_all())

@blueprint.route("/user/<id>",methods=["GET"])
def get_user_by_id(id):
    authentication("*")
    return model_to_json(user_repository.get_by_id(id))