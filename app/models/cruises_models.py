from app.database.connection import Base
from sqlalchemy import Enum, String,Column,Integer,Text
from app.models.price_tire import price_tire
from app.models.travel_styles import travel_styles


class cruises_table(Base):
    __tablename__="cruises"
    
    id=Column(Integer,primary_key=True,nullable=False)
    cruises_name=Column(String,nullable=False)
    destination=Column(String,nullable=False)
    duration=Column(Integer,nullable=False)
    ports_of_call=Column(Text,nullable=False)
    highlights=Column(Text,nullable=False)
    price=Column(Enum(price_tire,name="price_tire_enum"),nullable=False)
    travel_style=Column(Enum(travel_styles,name="travel_style_enum"),nullable=False)