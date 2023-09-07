from sqlalchemy import Column, Integer, String
from database import Base

class BloodGroup(Base):
    __tablename__ = 'blood_groups'

    id = Column(Integer, primary_key=True)
    group_name = Column(String(10), unique=True)

    def __init__(self, group_name):
        self.group_name = group_name
        
    @classmethod
    def all(cls):
        
        