import jwt
import datetime
from jwt.exceptions import DecodeError,ExpiredSignatureError
from werkzeug.exceptions import Unauthorized

token_key="7Kc8QdRBrFuRVnBS"
token_algorithm="HS256"

def is_token_valid(token_string):
    try:
        jwt.decode(token_string,token_key,token_algorithm)
        return True
    except:
        return False

def create_token(user):
    expire=round((datetime.datetime.now()+datetime.timedelta(days=30)).timestamp())
    return jwt.encode({"username":user.username,"exp":expire,"role":user.role},token_key,token_algorithm)

def get_token(token_string):
    try:
        token=jwt.decode(token_string,token_key,token_algorithm)
    except DecodeError:
        raise Unauthorized("Invalid Token")
    except ExpiredSignatureError:
        raise Unauthorized("Expired Token")
    return token