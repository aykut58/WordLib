from .repository import WordRepository
from werkzeug.exceptions import BadRequest, Forbidden, NotFound,Unauthorized
from . import security

class WordService:

    def __init__(self):
        self.word_repository=WordRepository()

    def get_all(self):
        if security.logged_in():
            return self.word_repository.get_all()
        else:
            raise Unauthorized("You must log in")
    
    def get_by_id(self,id):
        if self.word_repository.exists_by_id(id):
            return self.word_repository.get_by_id(id)
        raise NotFound("No word found by this id")
    
    def get_by_turkish(self,turkish):
        if security.logged_in():
            if self.word_repository.exists_by_turkish(turkish):
                return self.word_repository.get_by_turkish(turkish)
            else:
                raise BadRequest("No word found")
        else:
            raise Unauthorized("You must log in")
    
    def get_by_english(self,english):
        return self.word_repository.get_by_english(english)

    def add(self,word):
        if security.logged_in():
            if security.is_logged_in_user_admin():
                return self.word_repository.add(word)
            else:
                raise Forbidden("You have no permission for this operation")
        else:
            raise Unauthorized("You must log in")
    
    def update(self,word):
        if security.logged_in():
            if security.is_logged_in_user_admin():
                return self.word_repository.update(word)
            else:
                raise Forbidden("You have no permission for this operation")
        else:
            raise Unauthorized("You must log in")
    
    def delete_by_id(self,id):
        if self.word_repository.exists_by_id(id):
            self.word_repository.delete_by_id(id)
            return True
        raise NotFound("No word found by this id")