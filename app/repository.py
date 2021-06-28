from app.database import db
from app.model import Admin, EnglishWord,TurkishWord,User,Category
from sqlalchemy.sql.expression import func

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

class TurkishWordRepository:
    def get_random_except(self,word_id,count):
        return db.session.query(TurkishWord).filter(TurkishWord.id!=word_id).order_by(func.random()).limit(count).all()

    def get_by_category_id(self,category_id):
        return db.session.query(TurkishWord).filter_by(category_id=category_id).all()

    def get_all(self):
        return db.session.query(TurkishWord).all()

    def get_random_by_category_id(self,category_id,count):
        return db.session.query(TurkishWord).filter_by(category_id=category_id).order_by(func.random()).limit(count).all()

    def get_random(self,count):
        return db.session.query(TurkishWord).order_by(func.random()).limit(count).all()

    def get_by_id(self,id):
        return db.session.query(TurkishWord).filter_by(id=id).one()
    
    def exists_by_id(self,id):
        return db.session.query(TurkishWord).filter_by(id=id).scalar() is not None
    
    def add(self,word):
        word=db.session.merge(word)
        db.session.commit()
        return word
    
    def update(self,word):
        word=db.session.merge(word)
        db.session.commit()
        return word
    
    def delete_by_id(self,id):
        db.session.query(TurkishWord).filter_by(id=id).delete()
        db.session.commit()

class EnglishWordRepository:
    def get_random_except(self,word_id,count):
        return db.session.query(EnglishWord).filter(EnglishWord.id!=word_id).order_by(func.random()).limit(count).all()

    def get_by_category_id(self,category_id):
        return db.session.query(EnglishWord).filter_by(category_id=category_id).all()

    def get_all(self):
        return db.session.query(EnglishWord).all()

    def get_random_by_category_id(self,category_id,count):
        return db.session.query(EnglishWord).filter_by(category_id=category_id).order_by(func.random()).limit(count).all()

    def get_random(self,count):
        return db.session.query(EnglishWord).order_by(func.random()).limit(count).all()
   
    def get_by_id(self,id):
        return db.session.query(EnglishWord).filter_by(id=id).one()
    
    def exists_by_id(self,id):
        return db.session.query(EnglishWord).filter_by(id=id).scalar() is not None
    
    def add(self,word):
        word=db.session.merge(word)
        db.session.commit()
        return word
    
    def update(self,word):
        word=db.session.merge(word)
        db.session.commit()
        return word
    
    def delete_by_id(self,id):
        db.session.query(EnglishWord).filter_by(id=id).delete()
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