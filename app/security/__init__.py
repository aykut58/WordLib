import hashlib
from flask import request
from app.repository import UserRepository,AdminRepository
from werkzeug.exceptions import BadRequest,Unauthorized,Forbidden
from .token_functions import is_token_valid,create_token,get_token

user_repository=UserRepository()
admin_repository=AdminRepository()

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