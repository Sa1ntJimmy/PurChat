from dataclasses import dataclass
from flask_sqlalchemy import SQLAlchemy
import backend.main as main

db = main.app_db

@dataclass
class Users(db.Model):
    userid: int
    username: str

    userid = db.Column(db.Integer, nullable=False, primary_key=True, autoincrement=True)
    username = db.Column(db.Text, nullable=False)
    
    def __repr__(self) -> str:
        return '<User %r>' % self.username

class Messages(db.Model):
    time = db.Column(db.Text, nullable=False, primary_key=True)
    username = db.Column(db.Text, nullable=False)
    userid = db.Column(db.Integer, db.ForeignKey('users.userid'), nullable=False)

    def __repr__(self) -> str:
        return '<Message %r>' % self.time