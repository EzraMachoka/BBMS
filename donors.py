from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Donor(Base):
    __tablename__ = 'donors'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    blood_group_id = Column(Integer, ForeignKey('blood_groups.id'))
    blood_group = relationship('BloodGroup', back_populates='donors')