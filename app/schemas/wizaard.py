from datetime import date
from typing import Optional
from pydantic import BaseModel

class wizards(BaseModel):
    Destination:Optional[str]=None
    tavel_date:Optional[date]=None
    Duration:Optional[int]=None
    Budget:Optional[str]=None
    Trip:Optional[str]=None
    
    