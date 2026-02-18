from sqlalchemy import Enum, func
from sqlalchemy import Column,Integer,String,Float,DateTime
from app.database.connection import Base
from app.models.detect_fields import detect_fields

class ai_intents(Base):
    __tablename__="aitable"
    
    
    id=Column(Integer,primary_key=True,nullable=False)
    user_id=Column(Integer,nullable=False)
    raw_text=Column(String,nullable=False)
    detected_intent=Column(Enum(detect_fields))
    confidence_score=Column(Float,nullable=False)
    created_at=Column(DateTime(timezone=True),server_default=func.now())