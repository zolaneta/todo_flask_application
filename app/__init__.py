from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__, static_url_path='', static_folder="static")

app.config.from_object('config')

db = SQLAlchemy(app)

from app.main import views
from app import models
from models import Todo, Priority, Category
