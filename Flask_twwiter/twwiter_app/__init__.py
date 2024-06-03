from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config.from_object('twwiter_app.config')

db = SQLAlchemy(app)

# import holi_master.views

# from holi_master.views import views, entries