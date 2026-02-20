from datetime import datetime, timedelta
from app.models.booking_models import Booking
from app.models.guests import Guest
from app.models.cabins import Cabin

LOCK_HOURS = 3


def initialize_booking(db, sailing_id: int, cabin_type: str):

    cabin = db.query(Cabin).filter(
        Cabin.sailing_id == sailing_id,
        Cabin.cabin_type == cabin_type
    ).first()

    if not cabin:
        raise Exception("Cabin not found")

    if cabin.available_count <= 0:
        raise Exception("Cabin sold out")

    # ✅ Lock inventory
    cabin.available_count -= 1

    expires_at = datetime.utcnow() + timedelta(hours=LOCK_HOURS)

    booking = Booking(
        sailing_id=sailing_id,
        cabin_type=cabin_type,
        status="PENDING",
        total_price=cabin.price,
        currency="USD",
        expires_at=expires_at
    )

    db.add(booking)
    db.commit()
    db.refresh(booking)

    return booking


def add_guests(db, booking_id: int, guests: list):

    booking = db.query(Booking).filter(Booking.id == booking_id).first()

    if not booking:
        raise Exception("Booking not found")

    if booking.status != "PENDING":
        raise Exception("Cannot add guests")

    for guest_data in guests:
        guest = Guest(
            booking_id=booking_id,
            full_name=guest_data.full_name,
            age=guest_data.age,
            passport_id=guest_data.passport_id
        )
        db.add(guest)

    db.commit()

    return {"message": "Guests added successfully"}