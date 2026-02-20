from pydantic import BaseModel
from typing import List, Optional

class BookingInitialize(BaseModel):
    sailing_id: int
    cabin_type: str


class GuestCreate(BaseModel):
    full_name: str
    age: int
    passport_id: str


class PaymentIntentCreate(BaseModel):
    booking_id: int
    amount: float
    currency: str = "usd"