from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class BloodGroup(Base):
    __tablename__ = 'blood_group'

    id = Column(Integer, primary_key=True)
    group_name = Column(String(10), unique=True)


class Donor(Base):
    __tablename__ = 'donor'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    blood_group_id = Column(Integer, ForeignKey('blood_group.id'))

    blood_group = relationship('BloodGroup')


class BloodVolume(Base):
    __tablename__ = 'blood_volume'

    id = Column(Integer, primary_key=True)
    blood_group_id = Column(Integer, ForeignKey('blood_group.id'))
    volume = Column(Integer)

    blood_group = relationship('BloodGroup')