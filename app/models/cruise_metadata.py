from app.database.connection import Base
from sqlalchemy import Column, Integer, String

class CruiseMetadata(Base):
    __tablename__ = "cruise_metadata"
    
    id = Column(Integer, primary_key=True, nullable=False)
    key = Column(String, nullable=False)
    category = Column(String, nullable=False)
    label_en = Column(String, nullable=False)
    label_ar = Column(String, nullable=False)