import os

class Config:
    ENV=os.getenv("ENV","development")
    DEBUG=True if ENV=="development" else False
    SQLALCHEMY_DATABASE_URI="mysql+mysqlconnector://root:"+os.getenv("DB_PASSWORD","password")+"@"+os.getenv("DB_HOST","localhost")+":3306/social_media"
    SQLALCHEMY_TRACK_MODIFICATIONS=True if ENV=="development" else False
    HOST="127.0.0.1" if ENV=="development" else "0.0.0.0"