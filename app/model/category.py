from app.db import db
from sqlalchemy import Column,Integer,String

class Category(db.Model):
    id=Column(Integer,primary_key=True)
    name=Column(String(25),unique=True)

    def to_dict(self):
        return {"id":self.id,"name":self.name}