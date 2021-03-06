import os

class Config:
    ENV=os.getenv("ENV","development")
    DEBUG=True if ENV=="development" else False
    JWT_KEY=os.getenv("JWT_KEY","key")
    SQLALCHEMY_DATABASE_URI=os.getenv("DB_URL","mysql://root:password@localhost:3306/wordlib")
    SQLALCHEMY_TRACK_MODIFICATIONS=True if ENV=="development" else False
    HOST="127.0.0.1" if ENV=="development" else "0.0.0.0"