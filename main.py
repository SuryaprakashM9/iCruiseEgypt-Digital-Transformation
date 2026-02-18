from fastapi import FastAPI
from app.database.connection import get_db,Base,engine
from app.models.ai_intent_model import ai_intents
from app.models.planner_session import PlannerSession
from app.models.cruise_metadata import cruise_metadata
Base.metadata.create_all(bind=engine)
app=FastAPI()

@app.get("/")
def home():
    return {"message":"db connected sucess"}