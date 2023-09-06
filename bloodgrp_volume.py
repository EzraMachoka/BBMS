from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class BloodVolume(Base):
    __tablename__ = 'blood_volume'

    id = Column(Integer, primary_key=True)
    blood_group_id = Column(Integer, ForeignKey('blood_groups.id'))
    blood_group = relationship('BloodGroup', back_populates='blood_volumes')
    volume = Column(Integer)