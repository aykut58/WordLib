from flask import Blueprint,jsonify
from sqlalchemy.orm.exc import NoResultFound

error_blueprint=Blueprint("error",__name__)

@error_blueprint.app_errorhandler(Exception)
def error(error):
    if isinstance(error,NoResultFound):
        return jsonify({"Message":"No Entity Found by This id"}),400
    return jsonify({"Message":"Error"}),500