from pydantic import BaseModel
from typing import Optional

class user_input(BaseModel):
    user_id:int
    user_value:str
    
    class config:
        orm_mode=True



class UserPreferences(BaseModel):
    user_id: int
    destination: Optional[str] = None
    travel_date: Optional[str] = None
    duration: Optional[str] = None
    budget: Optional[str] = None
    trip_style: Optional[str] = None