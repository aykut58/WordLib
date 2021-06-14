from flask import jsonify,request,Blueprint
from werkzeug.exceptions import BadRequest,Unauthorized,Conflict
from app.repository import UserRepository,AdminRepository,CategoryRepository
from app.security import authentication,hash_password,create_token,is_token_valid
from app.model import Category, EnglishWord,TurkishWord,User
from .serializer import TurkishWordSerializer,EnglishWordSerializer
from .service import EnglishWordService,TurkishWordService

blueprint=Blueprint("blueprint",__name__)
user_repository=UserRepository()
admin_repository=AdminRepository()
category_repository=CategoryRepository()
turkish_word_serializer=TurkishWordSerializer()
turkish_words_serializer=TurkishWordSerializer(many=True)
turkish_word_service=TurkishWordService()
english_word_serializer=EnglishWordSerializer()
english_words_serializer=EnglishWordSerializer(many=True)
english_word_service=EnglishWordService()

def check_request_data(*keys):
    if request.get_json()==None:
        raise BadRequest(keys[0]+" not given")
    for key in keys:
        if not key in request.get_json():
            raise BadRequest(key+" not given")
    return True

@blueprint.route("/word/english")
def get_all_english_words():
    return english_words_serializer.jsonify(english_word_service.get_all())

@blueprint.route("/word/english/random/<count>")
def get_random_english_words(count):
    return english_words_serializer.jsonify(english_word_service.get_random(count))

@blueprint.route("/word/english/random/<category_id>/<count>")
def get_random_english_words_by_category_id(category_id,count):
    return english_words_serializer.jsonify(english_word_service.get_random_by_category_id(category_id,count))

@blueprint.route("/word/english/<id>")
def get_english_word_by_id(id):
    return english_word_serializer.jsonify(english_word_service.get_by_id(id))

@blueprint.route("/word/english/<id>",methods=["DELETE"])
def delete_english_word_by_id(id):
    return jsonify({"Result":english_word_service.delete_by_id(id)})

@blueprint.route("/word/english",methods=["POST"])
def add_english_word():
    if check_request_data("category_id","word"):
        category_id=request.get_json()["category_id"]
        word=request.get_json()["word"]
        english_word=EnglishWord(category_id=category_id,word=word)
        return english_word_serializer.jsonify(english_word_service.add(english_word)),201

@blueprint.route("/word/english",methods=["PUT"])
def update_english_word():
    if check_request_data("turkish_words","category_id","id","word"):
        id=request.get_json()["id"]
        category_id=request.get_json()["category_id"]
        word=request.get_json()["word"]
        turkish_words=[turkish_word_service.get_by_id(turkish_word["id"]) for turkish_word in request.get_json()["turkish_words"]]
        english_word=EnglishWord(category_id=category_id,word=word,turkish_words=turkish_words,id=id)
        return english_word_serializer.jsonify(english_word_service.update(english_word))

@blueprint.route("/word/turkish")
def get_all_turkish_words():
    return turkish_words_serializer.jsonify(turkish_word_service.get_all())

@blueprint.route("/word/turkish/random/<count>")
def get_random_turkish_words(count):
    return turkish_words_serializer.jsonify(turkish_word_service.get_random(count))

@blueprint.route("/word/turkish/random/<category_id>/<count>")
def get_random_turkish_words_by_category_id(category_id,count):
    return turkish_words_serializer.jsonify(turkish_word_service.get_random_by_category_id(category_id,count))

@blueprint.route("/word/turkish/<id>")
def get_turkish_word_by_id(id):
    return turkish_word_serializer.jsonify(turkish_word_service.get_by_id(id))

@blueprint.route("/word/turkish/<id>",methods=["DELETE"])
def delete_turkish_word_by_id(id):
    return jsonify({"Result":turkish_word_service.delete_by_id(id)})

@blueprint.route("/word/turkish",methods=["POST"])
def add_turkish_word():
    if check_request_data("category_id","word"):
        category_id=request.get_json()["category_id"]
        word=request.get_json()["word"]
        turkish_word=TurkishWord(category_id=category_id,word=word)
        return turkish_word_serializer.jsonify(turkish_word_service.add(turkish_word)),201

@blueprint.route("/word/turkish",methods=["PUT"])
def update_turkish_word():
    if check_request_data("english_words","category_id","id","word"):
        category_id=request.get_json()["category_id"]
        word=request.get_json()["word"]
        id=request.get_json()["id"]
        english_words=[english_word_service.get_by_id(english_word["id"]) for english_word in request.get_json()["english_words"]]
        turkish_word=TurkishWord(category_id=category_id,word=word,english_words=english_words,id=id)
        return turkish_word_serializer.jsonify(turkish_word_service.update(turkish_word))

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
    if check_request_data("username","password"):
        username=request.get_json()["username"]
        password=request.get_json()["password"]
        if admin_repository.exists_by_username(username):
            admin=admin_repository.get_by_username(username)
        else:
            raise Unauthorized("Username or Password is incorrect")
        if admin.password==hash_password(password):
            return jsonify({"Token":create_token(admin)})
        raise Unauthorized("Username or Password is incorrect")

@blueprint.route("/register",methods=["POST"])
def register():
    if check_request_data("username","password","email"):
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
                return jsonify({"Message":"Successful"}),201
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
    if check_request_data("turkish_name","english_name"):
        category=Category(turkish_name=request.get_json()["turkish_name"],english_name=request.get_json()["english_name"])
        return model_to_json(category_repository.add(category)),201

@blueprint.route("/category",methods=["PUT"])
def update_category():
    authentication("Admin")
    if check_request_data("id","turkish_name","english_name"):
        category=Category(turkish_name=request.get_json()["turkish_name"],english_name=request.get_json()["english_name"],id=request.get_json()["id"])
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