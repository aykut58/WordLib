from app.database import db
from app.model import Admin,User,Category,Word

class UserRepository:

    def exists_by_username(self,username):
        return db.session.query(User).filter_by(username=username).scalar() is not None

    def exists_by_email(self,email):
        return db.session.query(User).filter_by(email=email).scalar() is not None

    def exists_by_id(self,id):
        return db.session.query(User).filter_by(id=id).scalar() is not None

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
        db.session.commit()

class CategoryRepository:

    def get_all(self):
        return db.session.query(Category).all()
    
    def get_by_id(self,id):
        return db.session.query(Category).filter_by(id=id).one()
    
    def add(self,category):
        category=db.session.merge(category)
        db.session.commit()
        return category
    
    def update(self,category):
        category=db.session.merge(category)
        db.session.commit()
        return category
    
    def delete_by_id(self,id):
        db.session.query(Category).filter_by(id=id).delete()
        db.session.commit()

class WordRepository:

    def get_all(self):
        return db.session.query(Word).all()
    
    def get_by_id(self,id):
        return db.session.query(Word).filter_by(id=id).one()
    
    def exists_by_id(self,id):
        return db.session.query(Word).filter_by(id=id).scalar() is not None
    
    def get_by_turkish(self,turkish):
        return db.session.query(Word).filter_by(turkish=turkish.lower()).one()
    
    def get_by_english(self,english):
        return db.session.query(Word).filter_by(english=english.lower()).one()

    def add(self,word):
        word=db.session.merge(word)
        db.session.commit()
        return word
    
    def update(self,word):
        word=db.session.merge(word)
        db.session.commit()
        return word
    
    def delete_by_id(self,id):
        db.session.query(Word).filter_by(id=id).delete()
        db.session.commit()

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