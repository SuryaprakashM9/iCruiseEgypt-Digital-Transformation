import stripe
import os
from fastapi import APIRouter, Request, HTTPException
from sqlalchemy.orm import Session
from app.database.connection import SessionLocal
from app.models.booking_models import Booking
from app.models.payments import Payment

router = APIRouter(tags=["Webhook"])

endpoint_secret = os.getenv("STRIPE_WEBHOOK_SECRET")

@router.post("/webhook/stripe")
async def stripe_webhook(request: Request):

    payload = await request.body()
    sig_header = request.headers.get("stripe-signature")

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, endpoint_secret
        )
    except Exception as e:
        print("❌ Webhook verification failed:", str(e))
        raise HTTPException(status_code=400, detail="Invalid webhook")

    print("\n====== WEBHOOK RECEIVED ======")
    print("EVENT TYPE:", event["type"])

    db: Session = SessionLocal()

    try:

        # ✅ 1. CHECKOUT COMPLETED (BEST EVENT FOR CHECKOUT FLOW)
        if event["type"] == "checkout.session.completed":

            session = event["data"]["object"]
            metadata = session.get("metadata", {})

            print("METADATA:", metadata)

            booking_id = int(metadata.get("booking_id", 0))

            if not booking_id:
                print("❌ No booking_id in metadata")
                return {"status": "ignored"}

            booking = db.query(Booking).filter(Booking.id == booking_id).first()

            if booking:
                print("✅ Booking found → CONFIRMED")
                booking.status = "CONFIRMED"
            else:
                print("❌ Booking NOT FOUND")

            payment = db.query(Payment).filter(
                Payment.booking_id == booking_id
            ).first()

            if payment:
                print("✅ Payment found → SUCCESS")
                payment.status = "SUCCESS"
            else:
                print("❌ Payment NOT FOUND")

            db.commit()

        # ✅ 2. PAYMENT FAILED
        elif event["type"] == "payment_intent.payment_failed":

            intent = event["data"]["object"]
            metadata = intent.get("metadata", {})

            booking_id = int(metadata.get("booking_id", 0))

            if not booking_id:
                print("❌ No booking_id → ignoring")
                return {"status": "ignored"}

            booking = db.query(Booking).filter(Booking.id == booking_id).first()
            if booking:
                booking.status = "FAILED"

            payment = db.query(Payment).filter(
                Payment.payment_intent_id == intent["id"]
            ).first()
            if payment:
                payment.status = "FAILED"

            db.commit()

        # ✅ 3. IGNORE ALL OTHER EVENTS
        else:
            print("Event ignored")

    finally:
        db.close()

    return {"status": "processed"}