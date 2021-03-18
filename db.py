from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_utils import database_exists,create_database
import sys

if len(sys.argv)>1:
    host=sys.argv[1]
    password=sys.argv[2]
else:
    host="localhost"
    password="password"
db_url="mysql+mysqlconnector://root:"+password+"@"+host+":3306/wordlib"
print(db_url)
db=SQLAlchemy()
if not database_exists(db_url):
    create_database(db_url)