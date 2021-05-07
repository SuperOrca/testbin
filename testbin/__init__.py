import os

from easy_db import DataBase
from flask import Flask

app = Flask(__name__)
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

db = DataBase('data.db')
db.create_table('pastes', {"ID": str, "text": str}, False)

from .routes import *
