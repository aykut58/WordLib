from app.db import db
from sqlalchemy import Column,Integer,String

class Admin(db.Model):
    id=Column(Integer,primary_key=True)
    username=Column(String(30),unique=True)
    password=Column(String(128))

    def to_dict(self):
        return {"id":self.id,"username":self.username}