from .repository import WordRepository
from werkzeug.exceptions import NotFound,Unauthorized
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
        return self.word_repository.get_by_turkish(turkish)
    
    def get_by_english(self,english):
        return self.word_repository.get_by_english(english)

    def add(self,word):
        return self.word_repository.add(word)
    
    def update(self,word):
        return self.word_repository.update(word)
    
    def delete_by_id(self,id):
        if self.word_repository.exists_by_id(id):
            self.word_repository.delete_by_id(id)
            return True
        raise NotFound("No word found by this id")