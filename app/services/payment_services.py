import stripe
import os
from dotenv import load_dotenv

load_dotenv()
stripe.api_key = os.getenv("STRIPE_SECRET_KEY")


def create_checkout_session(booking_id: int, amount: float, currency: str):

    session = stripe.checkout.Session.create(
        payment_method_types=["card"],
        mode="payment",
        line_items=[
            {
                "price_data": {
                    "currency": currency,
                    "product_data": {
                        "name": f"Booking #{booking_id}",
                    },
                    "unit_amount": int(amount * 100),  # cents
                },
                "quantity": 1,
            }
        ],
        metadata={
            "booking_id": booking_id
        },
        success_url="http://127.0.0.1:8000/success",
        cancel_url="http://127.0.0.1:8000/cancel",
    )

    return session.url