from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from your_project import db

class Tenant(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(255), unique=True, nullable=False)
    devices = relationship('Device', back_populates='tenant')
    users = relationship('User', back_populates='tenant')
