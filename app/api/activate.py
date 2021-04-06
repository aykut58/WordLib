from flask import jsonify
from app.repository import UserRepository
from app import app

user_repository=UserRepository()

@app.route("/activate/<id>",methods=["GET"])
def activate_user(id):
    if user_repository.exists_by_id(id):
        user=user_repository.get_by_id(id)
        user.is_active=True
        user_repository.update(user)
        return jsonify({"Message":"Succesful"})
    else:
        return jsonify({"Message":"User not Found"}),404