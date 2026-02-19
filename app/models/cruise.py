from sqlalchemy import Column, Integer, String, Text
from app.database.connection import Base

class Cruise(Base):
    __tablename__ = "cruises"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    destination = Column(String)
    duration = Column(String)
    ports_of_call = Column(Text)
    highlights = Column(Text)
    price_tier = Column(String)
    travel_style = Column(String)
