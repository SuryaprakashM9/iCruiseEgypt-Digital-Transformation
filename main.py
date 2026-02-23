from fastapi import FastAPI
from app.database.connection import Base, engine

# Import models so SQLAlchemy registers them
from app.models.ai_intent_model import ai_intents
from app.models.planner_session import PlannerSession
from app.models.cruise_metadata import CruiseMetadata
from app.models.cruises_models import cruises_table
from app.models.sailings import Sailing

# Routers
from app.routers import ai_routers
from app.routers import itinerary_routers 
from app.routers import booking_router, payment_router

# Create tables
Base.metadata.create_all(bind=engine)

# App instance
app = FastAPI()

app.include_router(ai_routers.router)
app.include_router(itinerary_routers.router)
app.include_router(booking_router.router)
app.include_router(payment_router.router)


@app.get("/success")
def payment_success():
    return {"message": "Payment completed successfully ✅"}

@app.get("/cancel")
def payment_cancel():
    return {"message": "Payment cancelled ❌"}