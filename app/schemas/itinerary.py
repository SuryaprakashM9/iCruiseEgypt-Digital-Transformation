from pydantic import BaseModel
from typing import Optional

class ItineraryRequest(BaseModel):
    user_id: int
    regenerate: Optional[bool] = False




class ItineraryResponse(BaseModel):
    cruise_name: str
    duration: str
    ports_of_call: str
    highlights: str
    estimated_price: float
    ai_summary: str

