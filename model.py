from db import db
from sqlalchemy import Column,Integer,String,Boolean

class User(db.Model):
    id=Column(Integer,primary_key=True)
    email=Column(String(50),unique=True)
    username=Column(String(30),unique=True)
    password=Column(String(128))
    is_active=Column(Boolean)

    def to_json(self):
        return {"id":self.id,"email":self.email,"username":self.username,"is_active":self.is_active}

class Category(db.Model):
    id=Column(Integer,primary_key=True)
    name=Column(String(25),unique=True)

    def to_json(self):
        return {"id":self.id,"name":self.name}