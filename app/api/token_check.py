from flask import request,jsonify
from app.security import is_token_valid
from app import app
from werkzeug.exceptions import BadRequest

@app.route("/tokencheck",methods=["POST"])
def token_check():
    if "token" in request.headers:
        return jsonify({"Result":is_token_valid(request.headers.get("token"))})
    else:
        raise BadRequest("Token was not given")