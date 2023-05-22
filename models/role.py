from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
print("_role before import db")
from extensions import db
print("_role after import db")

class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True, nullable=False)
    users = relationship('User', secondary='user_roles')

    def __repr__(self):
      return self._repr(id=self.id)