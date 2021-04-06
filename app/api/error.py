from flask import jsonify
from sqlalchemy.orm.exc import NoResultFound
from app import app

@app.errorhandler(Exception)
def errorhandler(error):
    if isinstance(error,NoResultFound):
        return jsonify({"Message":"No Entity Found by This id"}),400
    if error.code==404:
        return jsonify({"Message":"URL Not Found"}),404
    if error.code==500:
        return jsonify({"Message":"Something went wrong on server"}),500
    if error.code==405:
        return jsonify({"Message":"Method not Allowed"}),405
    return jsonify({"Message":"Error"}),error.code