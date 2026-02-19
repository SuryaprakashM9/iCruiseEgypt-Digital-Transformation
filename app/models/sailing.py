from sqlalchemy import Column, Integer, Date, ForeignKey, DECIMAL
from app.database.connection import Base

class Sailing(Base):
    __tablename__ = "sailings"

    id = Column(Integer, primary_key=True)
    cruise_id = Column(Integer, ForeignKey("cruises.id"))
    embarkation_date = Column(Date)
    availability = Column(Integer)
    price = Column(DECIMAL)
