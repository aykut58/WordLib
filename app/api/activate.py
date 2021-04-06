from flask import jsonify
from app.repository import UserRepository
from app import app
from werkzeug.exceptions import BadRequest

user_repository=UserRepository()

@app.route("/activate/<id>",methods=["GET"])
def activate_user(id):
    if user_repository.exists_by_id(id):
        user=user_repository.get_by_id(id)
        user.is_active=True
        user_repository.update(user)
        return jsonify({"Message":"Succesful"})
    else:
        raise BadRequest("User not Found by this id")