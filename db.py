from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_utils import database_exists,create_database

db_url="mysql+mysqlconnector://root:28R35M5qyw7nBDsQ@wordlib.cllrqf9adx3k.us-east-1.rds.amazonaws.com:3306/wordlib"
db=SQLAlchemy()
if not database_exists(db_url):
    create_database(db_url)