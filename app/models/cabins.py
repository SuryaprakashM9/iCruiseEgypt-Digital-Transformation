from sqlalchemy import Column, Integer, String, Float, ForeignKey
from app.database.connection import Base

class Cabin(Base):
    __tablename__ = "cabins"

    id = Column(Integer, primary_key=True, index=True)
    sailing_id = Column(Integer, ForeignKey("sailings.id"))
    cabin_type = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    available_count = Column(Integer, nullable=False)