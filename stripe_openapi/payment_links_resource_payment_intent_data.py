from sqlalchemy import Column, Identity, Integer, String, Table

from . import metadata

PaymentLinksResourcePaymentIntentData.Json = Table(
    "payment_links_resource_payment_intent_data.json",
    metadata,
    Column(
        "capture_method",
        String,
        comment="Indicates when the funds will be captured from the customer's account",
        nullable=True,
    ),
    Column(
        "setup_future_usage",
        String,
        comment="Indicates that you intend to make future payments with the payment method collected during checkout",
        nullable=True,
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["payment_links_resource_payment_intent_data.json"]
