from app.database.connection import Base
from sqlalchemy import DateTime, Numeric, String,Column,Integer,ForeignKey,Float,Date
from app.models.cruises_models import cruises_table
class Sailing(Base):
    __tablename__ = "sailings"

    id = Column(Integer, primary_key=True, index=True)
    cruise_id = Column(Integer, ForeignKey("cruises.id"))
    embarkation_date = Column(Date, nullable=False)
    availability = Column(Integer, nullable=False)
    price = Column(Numeric, nullable=False)

    