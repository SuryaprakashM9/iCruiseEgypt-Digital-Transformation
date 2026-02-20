from app.database.connection import Base
from sqlalchemy import DateTime, Numeric, String,Column,Integer,ForeignKey,Float
from app.models.cruises_models import cruises_table
class sailings(Base):
    __tablename__="sailings"
    
    id=Column(Integer,primary_key=True,nullable=False)
    cruises_id=Column(Integer,ForeignKey("cruises.id",ondelete="CASCADE"),nullable=False)
    embarkation_date=Column(DateTime(timezone=True))
    availability=Column(Integer,nullable=False)
    price=Column(Numeric(10,2),nullable=False)