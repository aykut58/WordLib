from app.database import db
from sqlalchemy import Column,Integer,String,Boolean

class Admin(db.Model):
    id=Column(Integer,primary_key=True)
    username=Column(String(30),unique=True)
    password=Column(String(128))
    role="Admin"
    
    def to_dict(self):
        return {"id":self.id,"username":self.username}

class Category(db.Model):
    id=Column(Integer,primary_key=True)
    name=Column(String(25),unique=True)

    def to_dict(self):
        return {"id":self.id,"name":self.name}

class User(db.Model):
    id=Column(Integer,primary_key=True)
    email=Column(String(50),unique=True)
    username=Column(String(30),unique=True)
    password=Column(String(128))
    is_active=Column(Boolean)
    role="User"

    def to_dict(self):
        return {"id":self.id,"email":self.email,"username":self.username,"is_active":self.is_active}