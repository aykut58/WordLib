from flask import Blueprint,request,jsonify
from app.security import is_token_valid

token_check_blueprint=Blueprint("token_check",__name__)

@token_check_blueprint.route("/token-check",methods=["POST"])
def token_check():
    if "token" in request.headers:
        return jsonify({"Result":is_token_valid(request.headers.get("token"))})
    else:
        return jsonify({"Error":"Token was not given"}),400