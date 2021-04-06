from app import app
from app.repository import UserRepository
from .model_to_json import model_to_json
from app.security import authentication

user_repository=UserRepository()

class UserAPI:
    
    @app.route("/user",methods=["GET"])
    def get_all_users():
        authentication("*")
        return model_to_json(user_repository.get_all())

    @app.route("/user/<id>",methods=["GET"])
    def get_user_by_id(id):
        authentication("*")
        return model_to_json(user_repository.get_by_id(id))