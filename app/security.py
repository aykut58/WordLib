import hashlib
import jwt
import datetime
from flask import request
from app.repository import UserRepository,AdminRepository
from jwt.exceptions import DecodeError,ExpiredSignatureError
from werkzeug.exceptions import BadRequest,Unauthorized,Forbidden

token_key="7Kc8QdRBrFuRVnBS"
token_algorithm="HS256"
user_repository=UserRepository()
admin_repository=AdminRepository()

def is_token_valid(token):
    try:
        jwt.decode(token,token_key,token_algorithm)
        return True
    except:
        return False

def hash_password(password):
    return hashlib.sha512(password.encode()).hexdigest()

def create_token(user):
    expire=round((datetime.datetime.now()+datetime.timedelta(days=30)).timestamp())
    return jwt.encode({"username":user.username,"exp":expire,"role":user.role},token_key,token_algorithm)

def user_exists(username,role):
    if role=="Admin":
        if not admin_repository.exists_by_username(username):
            raise Unauthorized("Admin not Found")
        return admin_repository.get_by_username(username)
    elif role=="User":
        if not user_repository.exists_by_username(username):
            raise Unauthorized("User not Found")
        return user_repository.get_by_username(username)

def authentication(role):
    if "token" in request.headers:
        try:
            token=jwt.decode(request.headers.get("token"),token_key,token_algorithm)
        except DecodeError:
            raise Unauthorized("Invalid Token")
        except ExpiredSignatureError:
            raise Unauthorized("Expired Token")
        username=token.get("username")
        userrole=token.get("role")
        user_exists(username,userrole)
        if role!="*" and userrole!=role:
            raise Forbidden("Authorization Error")
    else:
        raise BadRequest("Token not Found")