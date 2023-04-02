from sqlalchemy import Column, Identity, Integer, String, Table

from . import metadata

PaymentPagesCheckoutSessionConsentJson = Table(
    "payment_pages_checkout_session_consentjson",
    metadata,
    Column(
        "promotions",
        String,
        comment="If `opt_in`, the customer consents to receiving promotional communications\nfrom the merchant about this Checkout Session",
        nullable=True,
    ),
    Column(
        "terms_of_service",
        String,
        comment="If `accepted`, the customer in this Checkout Session has agreed to the merchant's terms of service",
        nullable=True,
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["payment_pages_checkout_session_consent.json"]
