from pydantic import BaseModel

class GenerateItineraryRequest(BaseModel):
    session_id:int