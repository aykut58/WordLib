from app.db import db
from app.model import Admin

class AdminRepository:

    def count(self):
        return db.session.query(Admin).count()

    def exists_by_username(self,username):
        return db.session.query(Admin).filter_by(username=username).scalar() is not None

    def get_all(self):
        return db.session.query(Admin).all()
    
    def get_by_id(self,id):
        return db.session.query(Admin).filter_by(id=id).one()
    
    def get_by_username(self,username):
        return db.session.query(Admin).filter_by(username=username).one()
    
    def add(self,admin):
        admin=db.session.merge(admin)
        db.session.commit()
        return admin
    
    def update(self,admin):
        admin=db.session.merge(admin)
        db.session.commit()
        return admin