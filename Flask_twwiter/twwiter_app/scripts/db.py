from flask_script import Command
from twwiter_app import db
from twwiter_app.models.entries import User_Table
from twwiter_app.models.entries import Post_Table
from twwiter_app.models.entries import Comm_Table

class InitDB(Command):
    "create datbase"
    
    def run(self):
        db.create_all()