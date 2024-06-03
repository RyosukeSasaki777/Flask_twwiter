from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# import twwiter_app.views

app.config.from_object('twwiter_app.config')

db = SQLAlchemy(app)

from twwiter_app.views import entries, login