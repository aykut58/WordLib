from app.database import db
from app.model import Category

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