from flask import Flask
from app.initialize import initialize_app

app=Flask(__name__)
initialize_app(app)

from app import api