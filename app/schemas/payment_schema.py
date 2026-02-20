from pydantic import BaseModel

class PaymentCreate(BaseModel):
    booking_id: int
    amount: float
    currency: str