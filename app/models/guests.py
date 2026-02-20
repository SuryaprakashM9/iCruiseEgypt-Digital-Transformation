from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database.connection import Base

class Guest(Base):
    __tablename__ = "guests"

    id = Column(Integer, primary_key=True, index=True)
    booking_id = Column(Integer, ForeignKey("bookings.id"))
    full_name = Column(String)
    age = Column(Integer)
    passport_id = Column(String)

    # ✅ IMPORTANT
    booking = relationship("Booking", back_populates="guests")