from db import db
from model import User

class UserRepository:

    def exists_by_username(self,username):
        return db.session.query(User).filter_by(username=username).scalar() is not None

    def exists_by_email(self,email):
        return db.session.query(User).filter_by(email=email).scalar() is not None

    def get_all(self):
        return db.session.query(User).all()
    
    def get_by_id(self,id):
        return db.session.query(User).filter_by(id=id).one()
    
    def get_by_username(self,username):
        return db.session.query(User).filter_by(username=username).one()
    
    def get_by_email(self,email):
        return db.session.query(User).filter_by(email=email).one()
    
    def add(self,user):
        user=db.session.merge(user)
        db.session.commit()
        return user
    
    def update(self,user):
        user=db.session.merge(user)
        db.session.commit()
        return user
    
    def delete_by_id(self,id):
        db.session.query(User).filter_by(id=id).delete()