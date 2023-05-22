from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from extensions import db

class Device(db.Model):
    id = Column(Integer, primary_key=True)
    tenant_id = Column(Integer, ForeignKey('tenant.id'))
    ip = Column(String(255), nullable=False)
    community = Column(String(255), nullable=False)
    version = Column(Integer, nullable=False)
    poll_interval = Column(Integer, nullable=False)
    oids = Column(String(255), nullable=False)

    tenant = relationship('Tenant', back_populates='devices')

    def __repr__(self):
      return self._repr(id=self.id)
