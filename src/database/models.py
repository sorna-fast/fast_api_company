#human resources
from sqlalchemy import Column, String, Integer, ForeignKey, DateTime
from database.db import base
from sqlalchemy.orm import relationship

class Part(base):
    __tablename__ = "part"
    id = Column(Integer, primary_key=True, index=True)
    part_name = Column(String(50))

    human = relationship("Human_Resources",secondary="recruitment", back_populates="parts")
    recruitment=relationship("Recruitment",back_populates="part")

class Human_Resources(base):
    __tablename__ = "human_resources"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50))
    family = Column(String(50))
    parts = relationship("Part",secondary="recruitment", back_populates="human")
    recruitment=relationship("Recruitment",back_populates="human")
    
class Recruitment(base):
    __tablename__ = "recruitment"
    human_id = Column(Integer, ForeignKey('human_resources.id'), primary_key=True, index=True)
    part_id = Column(Integer,ForeignKey("part.id"), primary_key=True, index=True)
    date = Column(DateTime, nullable=True)
    human=relationship("Human_Resources",back_populates="recruitment")
    part=relationship("Part",back_populates="recruitment")
