from pydantic import BaseModel

class user_input(BaseModel):
    user_id:int
    user_value:str
    
    class config:
        orm_mode=True