from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.connection import get_db
from app.schemas.booking import BookingInitialize, GuestCreate
from app.services.booking_services import initialize_booking, add_guests
from app.models.booking_models import Booking

router = APIRouter(prefix="/booking", tags=["Booking"])

@router.post("/initialize")
def booking_initialize(data: BookingInitialize, db: Session = Depends(get_db)):
    booking = initialize_booking(db, data.sailing_id, data.cabin_type)
    return {"booking_id": booking.id, "expires_at": booking.expires_at}


@router.post("/{booking_id}/guests")
def booking_guests(booking_id: int, guests: list[GuestCreate], db: Session = Depends(get_db)):
    booking = db.query(Booking).filter(Booking.id == booking_id).first()

    if not booking:
        raise HTTPException(status_code=404, detail="Booking not found")

    add_guests(db, booking_id, guests)
    return {"message": "Guests added successfully"}


@router.get("/available-cabins/{sailing_id}")
def available_cabins(sailing_id: int):
    return {
        "sailing_id": sailing_id,
        "cabins": [
            {"type": "Interior", "price": 400},
            {"type": "Ocean View", "price": 600},
            {"type": "Suite", "price": 900},
        ]
    }


@router.get("/{booking_id}/summary")
def booking_summary(booking_id: int, db: Session = Depends(get_db)):
    booking = db.query(Booking).filter(Booking.id == booking_id).first()

    if not booking:
        raise HTTPException(status_code=404, detail="Booking not found")

    return {
        "booking_id": booking.id,
        "status": booking.status,
        "total_price": booking.total_price,
        "currency": booking.currency
    }


@router.get("/{booking_id}/status")
def booking_status(booking_id: int, db: Session = Depends(get_db)):
    booking = db.query(Booking).filter(Booking.id == booking_id).first()

    if not booking:
        raise HTTPException(status_code=404, detail="Booking not found")

    return {"status": booking.status}