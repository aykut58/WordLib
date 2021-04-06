import os

class Config:
    SQLALCHEMY_DATABASE_URI="mysql+mysqlconnector://root:"+os.getenv("DB_PASSWORD","password")+"@"+os.getenv("DB_HOST","localhost")+":3306/wordlib"
    ENV=os.getenv("ENV","development")
    HOST=os.getenv("HOST","127.0.0.1")