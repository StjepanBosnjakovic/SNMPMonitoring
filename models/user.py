from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from flask_login import UserMixin
from extensions import db

class User(UserMixin, db.Model):
    id = Column(Integer, primary_key=True)
    username = Column(String(255), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    active = Column(Boolean(), nullable=False, default=True)
    tenant_id = Column(Integer, ForeignKey('tenant.id'))
    tenant = relationship('Tenant', back_populates='users')
    roles = relationship('Role', secondary='user_roles')

    def __repr__(self):
      return self._repr(id=self.id)
