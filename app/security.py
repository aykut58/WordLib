import hashlib
from app.repository import UserRepository,AdminRepository
from werkzeug.exceptions import BadRequest,Unauthorized,Forbidden
import jwt
import datetime
from jwt.exceptions import DecodeError,ExpiredSignatureError
from flask import current_app,request

user_repository=UserRepository()
admin_repository=AdminRepository()

def is_logged_in_user_admin():
    return get_token(request.headers["token"])["role"]=="Admin"

def logged_in():
    if "token" in request.headers:
        return is_token_valid(request.headers["token"])
    else:
        return False

def hash_password(password):
    return hashlib.sha512(password.encode()).hexdigest()

def user_exists(username,role):
    if role=="Admin":
        if not admin_repository.exists_by_username(username):
            raise Unauthorized("Admin not Found")
    elif role=="User":
        if not user_repository.exists_by_username(username):
            raise Unauthorized("User not Found")

def authentication(role):
    if "token" in request.headers:
        token=get_token(request.headers.get("token"))
        username=token.get("username")
        userrole=token.get("role")
        user_exists(username,userrole)
        if role!="*" and userrole!=role:
            raise Forbidden("Authorization Error")
    else:
        raise BadRequest("Token not Found")

token_algorithm="HS256"

def is_token_valid(token_string):
    try:
        jwt.decode(token_string,current_app.config["JWT_KEY"],token_algorithm)
        return True
    except:
        return False

def create_token(user):
    expire=round((datetime.datetime.now()+datetime.timedelta(days=30)).timestamp())
    return jwt.encode({"username":user.username,"exp":expire,"role":user.role},current_app.config["JWT_KEY"],token_algorithm)

def get_token(token_string):
    try:
        token=jwt.decode(token_string,current_app.config["JWT_KEY"],token_algorithm)
    except DecodeError:
        raise Unauthorized("Invalid Token")
    except ExpiredSignatureError:
        raise Unauthorized("Expired Token")
    return token