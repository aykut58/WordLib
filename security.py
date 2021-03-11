import hashlib
import jwt
import datetime

token_key="key"
token_algorithm="HS256"

def hash_password(password):
    return hashlib.sha512(password.encode()).hexdigest()

def create_token(username):
    expire=round((datetime.datetime.now()+datetime.timedelta(days=30)).timestamp())
    return jwt.encode({"username":username,"exp":expire},token_key,token_algorithm)