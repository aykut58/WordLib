from .repository import TurkishWordRepository,EnglishWordRepository
from werkzeug.exceptions import Forbidden,NotFound,Unauthorized
from . import security

class TurkishWordService:
    def get_by_category_id(self,category_id):
        return self.turkish_word_repository.get_by_category_id(category_id)

    def __init__(self):
        self.turkish_word_repository=TurkishWordRepository()

    def get_all(self):
        if security.logged_in():
            return self.turkish_word_repository.get_all()
        else:
            raise Unauthorized("You must log in")

    def get_random_by_category_id(self,category_id,count):
        if security.logged_in():
            return self.turkish_word_repository.get_random_by_category_id(category_id,count)
        else:
            raise Unauthorized("You must log in")

    def get_random(self,count):
        if security.logged_in():
            return self.turkish_word_repository.get_random(count)
        else:
            raise Unauthorized("You must log in")
    
    def get_by_id(self,id):
        if security.logged_in():
            if self.turkish_word_repository.exists_by_id(id):
                return self.turkish_word_repository.get_by_id(id)
            raise NotFound("No word found by this id")
        else:
            raise Unauthorized("You must log in")

    def add(self,word):
        if security.logged_in():
            if security.is_logged_in_user_admin():
                return self.turkish_word_repository.add(word)
            else:
                raise Forbidden("You have no permission for this operation")
        else:
            raise Unauthorized("You must log in")
    
    def update(self,word):
        if security.logged_in():
            if security.is_logged_in_user_admin():
                return self.turkish_word_repository.update(word)
            else:
                raise Forbidden("You have no permission for this operation")
        else:
            raise Unauthorized("You must log in")
    
    def delete_by_id(self,id):
        if security.logged_in():
            if security.is_logged_in_user_admin():
                if self.turkish_word_repository.exists_by_id(id):
                    self.turkish_word_repository.delete_by_id(id)
                    return True
                raise NotFound("No word found by this id")
            else:
                raise Forbidden("You have no permission for this operation")
        else:
            raise Unauthorized("You must log in")

class EnglishWordService:
    def get_by_category_id(self,category_id):
        return self.english_word_repository.get_by_category_id(category_id)

    def __init__(self):
        self.english_word_repository=EnglishWordRepository()

    def get_all(self):
        if security.logged_in():
            return self.english_word_repository.get_all()
        else:
            raise Unauthorized("You must log in")

    def get_random_by_category_id(self,category_id,count):
        if security.logged_in():
            return self.english_word_repository.get_random_by_category_id(category_id,count)
        else:
            raise Unauthorized("You must log in")

    def get_random(self,count):
        if security.logged_in():
            return self.english_word_repository.get_random(count)
        else:
            raise Unauthorized("You must log in")
    
    def get_by_id(self,id):
        if security.logged_in():
            if self.english_word_repository.exists_by_id(id):
                return self.english_word_repository.get_by_id(id)
            raise NotFound("No word found by this id")
        else:
            raise Unauthorized("You must log in")

    def add(self,word):
        if security.logged_in():
            if security.is_logged_in_user_admin():
                return self.english_word_repository.add(word)
            else:
                raise Forbidden("You have no permission for this operation")
        else:
            raise Unauthorized("You must log in")
    
    def update(self,word):
        if security.logged_in():
            if security.is_logged_in_user_admin():
                return self.english_word_repository.update(word)
            else:
                raise Forbidden("You have no permission for this operation")
        else:
            raise Unauthorized("You must log in")
    
    def delete_by_id(self,id):
        if security.logged_in():
            if security.is_logged_in_user_admin():
                if self.english_word_repository.exists_by_id(id):
                    self.english_word_repository.delete_by_id(id)
                    return True
                raise NotFound("No word found by this id")
            else:
                raise Forbidden("You have no permission for this operation")
        else:
            raise Unauthorized("You must log in")