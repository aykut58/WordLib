import hashlib
import jwt
import datetime
from flask import request,jsonify
from app.repository import UserRepository,AdminRepository
from jwt.exceptions import DecodeError,ExpiredSignatureError

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
    return jwt.encode({"username":user.username,"exp":expire,"usertype":type(user).__name__},token_key,token_algorithm)

def token_filter():
    if request.path!="/" and request.path!="/login" and request.path!="/register" and not request.path.startswith("/activate") and request.path!="/token-check" and request.path!="/login/admin":
        if "token" in request.headers:
            try:
                token=jwt.decode(request.headers.get("token"),token_key,token_algorithm)
            except DecodeError:
                return jsonify({"Error Message":"Invalid Token"}),400
            except ExpiredSignatureError:
                return jsonify({"Error Message":"Expired Token"}),401
            username=token.get("username")
            usertype=token.get("usertype")
            if usertype=="Admin":
                if not admin_repository.exists_by_username(username):
                    return jsonify({"Error Message":"User not Found"}),401
            elif usertype=="User":
                if not user_repository.exists_by_username(username):
                    return jsonify({"Error Message":"User not Found"}),401
                if request.method=="DELETE" or request.method=="POST" or request.method=="PUT":
                    return jsonify({"Error Message":"Authorization Error"}),403
        else:
            return jsonify({"Error Message":"Token not Found"}),401