from datetime import datetime
from app.models.booking_models import Booking
from app.models.cabins import Cabin


def release_expired_bookings(db):

    expired = db.query(Booking).filter(
        Booking.status == "PENDING",
        Booking.expires_at < datetime.utcnow()
    ).all()

    for booking in expired:

        cabin = db.query(Cabin).filter(
            Cabin.sailing_id == booking.sailing_id,
            Cabin.cabin_type == booking.cabin_type
        ).first()

        if cabin:
            cabin.available_count += 1

        booking.status = "EXPIRED"

    db.commit()