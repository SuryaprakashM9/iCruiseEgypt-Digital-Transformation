from sqlalchemy import Column, Integer, String, Boolean, DateTime
from datetime import datetime
from app.database.connection import Base


class PlannerSession(Base):
    __tablename__ = "planner_sessions"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, nullable=False)

    destination = Column(String, nullable=True)
    travel_date = Column(String, nullable=True)
    duration_nights = Column(Integer, nullable=True)
    budget_range = Column(String, nullable=True)
    trip_style = Column(String, nullable=True)

    current_step = Column(Integer, default=1)      # wizard start step
    is_completed = Column(Boolean, default=False)  # finished or not

    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
