from app.database.connection import engine, Base

# MUST import ALL model modules
import app.models.cruise_metadata
import app.models.sailings
import app.models.cabins
from app.models.booking_models import Booking
import app.models.guests
import app.models.payments

def init_db():
    Base.metadata.create_all(bind=engine)
    print("✅ All tables created")

if __name__ == "__main__":
    init_db()