from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from your_project import db

class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True, nullable=False)
    users = relationship('User', secondary='user_roles')