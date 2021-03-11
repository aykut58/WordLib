from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_utils import database_exists,create_database

db_url="mysql+mysqlconnector://root:password@db:3306/wordlib"
db=SQLAlchemy()
if not database_exists(db_url):
    create_database(db_url)