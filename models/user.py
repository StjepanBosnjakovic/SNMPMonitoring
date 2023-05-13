from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from flask_login import UserMixin
from flask_user import UserMixin as FlaskUserMixin
from your_project import db

class User(UserMixin, FlaskUserMixin, db.Model):
    id = Column(Integer, primary_key=True)
    username = Column(String(255), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    active = Column(Boolean(), nullable=False, default=True)
    tenant_id = Column(Integer, ForeignKey('tenant.id'))
    tenant = relationship('Tenant', back_populates='users')
    roles = relationship('Role', secondary='user_roles')
