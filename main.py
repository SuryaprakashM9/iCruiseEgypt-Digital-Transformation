from fastapi import FastAPI,APIRouter
from app.database.connection import get_db,Base,engine
from app.models.ai_intent_model import ai_intents
from app.models.planner_session import PlannerSession
from app.models.cruise_metadata import cruise_metadata
from app.models.cruises_models import cruises_table
from app.models.sailings import sailings
from app.routers import ai_routers
from app.routers import itinerary_routers



Base.metadata.create_all(bind=engine)


app=FastAPI()

app.include_router(ai_routers.router)
app.include_router(itinerary_routers.router)
