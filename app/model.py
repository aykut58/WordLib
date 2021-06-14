from sqlalchemy.orm import relation,relationship
from app.database import db
from sqlalchemy import Column,Integer,String,Boolean,ForeignKey

english_turkish=db.Table("english_turkish",
    Column("english_word_id",Integer,ForeignKey("english_word.id"),primary_key=True),
    Column("turkish_word_id",Integer,ForeignKey("turkish_word.id"),primary_key=True)
)

class TurkishWord(db.Model):
    id=Column(Integer,primary_key=True)
    word=Column(String(100),unique=True)
    category=relation("Category")
    category_id=Column(ForeignKey("category.id"))
    english_words=relationship("EnglishWord",secondary=english_turkish)

class EnglishWord(db.Model):
    id=Column(Integer,primary_key=True)
    word=Column(String(100),unique=True)
    category=relation("Category")
    category_id=Column(ForeignKey("category.id"))
    turkish_words=relationship("TurkishWord",secondary=english_turkish)

class Admin(db.Model):
    id=Column(Integer,primary_key=True)
    username=Column(String(30),unique=True)
    password=Column(String(128))
    role="Admin"
    
    def to_dict(self):
        return {"id":self.id,"username":self.username}

class Category(db.Model):
    id=Column(Integer,primary_key=True)
    turkish_name=Column(String(25),unique=True)
    english_name=Column(String(25),unique=True)

    def to_dict(self):
        return {"id":self.id,"turkish_name":self.turkish_name,"english_name":self.english_name}

class User(db.Model):
    id=Column(Integer,primary_key=True)
    email=Column(String(50),unique=True)
    username=Column(String(30),unique=True)
    password=Column(String(128))
    is_active=Column(Boolean)
    role="User"

    def to_dict(self):
        return {"id":self.id,"email":self.email,"username":self.username,"is_active":self.is_active}