from flask import jsonify,request,Blueprint
from werkzeug.exceptions import HTTPException

error_handler_blueprint=Blueprint("error_handler",__name__)

@error_handler_blueprint.app_errorhandler(Exception)
def default_error_handler(exception):
    #TODO log
    print("Exception:",exception)
    return jsonify({"Error":"Something Went Wrong on the Server"}),500

@error_handler_blueprint.app_errorhandler(HTTPException)
def http_error_handler(exception):
    return jsonify({"Error":str(exception)}),exception.code