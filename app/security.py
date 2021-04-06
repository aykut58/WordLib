import hashlib
import jwt
import datetime
from flask import request,jsonify
from app.repository import UserRepository,AdminRepository
from jwt.exceptions import DecodeError,ExpiredSignatureError
from app.exception import AuthenticationException

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
            raise AuthenticationException("Admin not Found",code=404)
        return admin_repository.get_by_username(username)
    elif role=="User":
        if not user_repository.exists_by_username(username):
            raise AuthenticationException("User not Found",code=404)
        return user_repository.get_by_username(username)

def authentication(role):
    if "token" in request.headers:
        try:
            token=jwt.decode(request.headers.get("token"),token_key,token_algorithm)
        except DecodeError:
            raise AuthenticationException("Invalid Token",code=401)
        except ExpiredSignatureError:
            raise AuthenticationException("Expired Token",code=401)
        username=token.get("username")
        userrole=token.get("role")
        user_exists(username,userrole)
        if userrole!=role:
            raise AuthenticationException("Authorization Error",code=403)
    else:
        raise AuthenticationException("Token not Found",code=401)