from fastapi import APIRouter, Depends
from sqlmodel import Session
from app.database.connection import get_db
from app.services.itinerary_services import itinerary_service
from app.schemas.itinerary import GenerateItineraryRequest

router=APIRouter()

@router.post("/itinerary/generate")
def genrate_outputs(request:GenerateItineraryRequest,db:Session=Depends(get_db)):
    return itinerary_service(request.session_id,db)