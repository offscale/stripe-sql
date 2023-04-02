from sqlalchemy import Boolean, Column, Identity, Integer, Table

from . import metadata

PaymentPagesCheckoutSessionPhoneNumberCollectionJson = Table(
    "payment_pages_checkout_session_phone_number_collectionjson",
    metadata,
    Column(
        "enabled",
        Boolean,
        comment="Indicates whether phone number collection is enabled for the session",
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["payment_pages_checkout_session_phone_number_collection.json"]
