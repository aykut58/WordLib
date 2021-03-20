import hashlib
import jwt
import datetime
from flask import request,jsonify
from repository import UserRepository
from jwt.exceptions import DecodeError,ExpiredSignatureError

token_key="key"
token_algorithm="HS256"
user_repository=UserRepository()

def is_token_valid(token):
    try:
        jwt.decode(request.headers.get("token"),token_key,token_algorithm)
        return True
    except:
        return False

def hash_password(password):
    return hashlib.sha512(password.encode()).hexdigest()

def create_token(username):
    expire=round((datetime.datetime.now()+datetime.timedelta(days=30)).timestamp())
    return jwt.encode({"username":username,"exp":expire},token_key,token_algorithm)

def token_filter():
    if request.path!="/login" and request.path!="/register" and not request.path.startswith("/activate") and request.path!="/token-check":
        if "token" in request.headers:
            try:
                token=jwt.decode(request.headers.get("token"),token_key,token_algorithm)
            except DecodeError:
                return jsonify({"Error Message":"Invalid Token"}),400
            except ExpiredSignatureError:
                return jsonify({"Error Message":"Expired Token"}),401
            username=token.get("username")
            if not user_repository.exists_by_username(username):
                return jsonify({"Error Message":"User not Found"}),401
        else:
            return jsonify({"Error Message":"Token not Found"}),401