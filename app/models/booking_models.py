from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.orm import relationship
from app.database.connection import Base

class Booking(Base):
    __tablename__ = "bookings"

    id = Column(Integer, primary_key=True, index=True)
    sailing_id = Column(Integer)
    cabin_type = Column(String)
    status = Column(String)
    total_price = Column(Float)
    currency = Column(String)
    expires_at = Column(DateTime)

    # ✅ IMPORTANT
    guests = relationship("Guest", back_populates="booking")
    payments = relationship("Payment", back_populates="booking")