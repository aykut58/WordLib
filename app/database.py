from flask_sqlalchemy import SQLAlchemy
import sqlalchemy_utils

def create_database(db_url):
    if not sqlalchemy_utils.database_exists(db_url):
        sqlalchemy_utils.create_database(db_url)

db=SQLAlchemy()