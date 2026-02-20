from fastapi import APIRouter
from app.services.payment_services import create_checkout_session

router = APIRouter(prefix="/payment", tags=["Payment"])


@router.post("/checkout/{booking_id}")
def checkout(booking_id: int):

    checkout_url = create_checkout_session(
        booking_id=booking_id,
        amount=900,      # dynamic later
        currency="usd"
    )

    return {"checkout_url": checkout_url}