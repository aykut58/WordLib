from .repository import TurkishWordRepository,EnglishWordRepository
from werkzeug.exceptions import Forbidden,NotFound,Unauthorized
from . import security
import random

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

    def get_random_except(self,word_id,count):
        return self.turkish_word_repository.get_random_except(word_id,count)

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

    def get_random_except(self,word_id,count):
        return self.english_word_repository.get_random_except(word_id,count)

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

class EnglishExamService:

    def __init__(self):
        self.english_word_service=EnglishWordService()
        self.turkish_word_service=TurkishWordService()

    def create_by_category_id(self,category_id):
        if security.logged_in():
            output=[]
            words=self.english_word_service.get_random_by_category_id(category_id,20)
            for word in words:
                exam_word={"word":word.word}
                random_correct_answer_index=random.randint(0,3)
                random_index=random.randint(0,len(word.turkish_words)-1)
                print(word.word,random_correct_answer_index)
                options=[]
                random_incorrect_options=self.turkish_word_service.get_random_except(word.turkish_words[random_index].id,3)
                for i,incorrect_word in enumerate(random_incorrect_options):
                    if i==random_correct_answer_index:
                        options.append({"word":word.turkish_words[random_index].word,"is_correct":True})
                    options.append({"word":incorrect_word.word,"is_correct":False})
                if random_correct_answer_index==3:
                    options.append({"word":word.turkish_words[random_index].word,"is_correct":True})
                exam_word["options"]=options
                output.append(exam_word)
            return output
        else:
            raise Unauthorized("You must log in")

    def create(self):
        if security.logged_in():
            output=[]
            words=self.english_word_service.get_random(20)
            for word in words:
                exam_word={"word":word.word}
                random_correct_answer_index=random.randint(0,3)
                random_index=random.randint(0,len(word.turkish_words)-1)
                options=[]
                random_incorrect_options=self.turkish_word_service.get_random_except(word.turkish_words[random_index].id,3)
                for i,incorrect_word in enumerate(random_incorrect_options):
                    if i==random_correct_answer_index:
                        options.append({"word":word.turkish_words[random_index].word,"is_correct":True})
                    options.append({"word":incorrect_word.word,"is_correct":False})
                if random_correct_answer_index==3:
                    options.append({"word":word.turkish_words[random_index].word,"is_correct":True})
                exam_word["options"]=options
                output.append(exam_word)
            return output
        else:
            raise Unauthorized("You must log in")

class TurkishExamService:

    def __init__(self):
        self.english_word_service=EnglishWordService()
        self.turkish_word_service=TurkishWordService()

    def create_by_category_id(self,category_id):
        if security.logged_in():
            output=[]
            words=self.turkish_word_service.get_random_by_category_id(category_id,20)
            for word in words:
                exam_word={"word":word.word}
                random_correct_answer_index=random.randint(0,3)
                random_index=random.randint(0,len(word.english_words)-1)
                options=[]
                random_incorrect_options=self.english_word_service.get_random_except(word.english_words[random_index].id,3)
                for i,incorrect_word in enumerate(random_incorrect_options):
                    if i==random_correct_answer_index:
                        options.append({"word":word.english_words[random_index].word,"is_correct":True})
                    options.append({"word":incorrect_word.word,"is_correct":False})
                if random_correct_answer_index==3:
                    options.append({"word":word.english_words[random_index].word,"is_correct":True})
                exam_word["options"]=options
                output.append(exam_word)
            return output
        else:
            raise Unauthorized("You must log in")

    def create(self):
        if security.logged_in():
            output=[]
            words=self.turkish_word_service.get_random(20)
            for word in words:
                exam_word={"word":word.word}
                random_correct_answer_index=random.randint(0,3)
                random_index=random.randint(0,len(word.english_words)-1)
                options=[]
                random_incorrect_options=self.english_word_service.get_random_except(word.english_words[random_index].id,3)
                for i,incorrect_word in enumerate(random_incorrect_options):
                    if i==random_correct_answer_index:
                        options.append({"word":word.english_words[random_index].word,"is_correct":True})
                    options.append({"word":incorrect_word.word,"is_correct":False})
                if random_correct_answer_index==3:
                    options.append({"word":word.english_words[random_index].word,"is_correct":True})
                exam_word["options"]=options
                output.append(exam_word)
            return output
        else:
            raise Unauthorized("You must log in")
