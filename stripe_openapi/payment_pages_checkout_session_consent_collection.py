from sqlalchemy import Column, Identity, Integer, String, Table

from . import metadata

PaymentPagesCheckoutSessionConsentCollectionJson = Table(
    "payment_pages_checkout_session_consent_collectionjson",
    metadata,
    Column(
        "promotions",
        String,
        comment="If set to `auto`, enables the collection of customer consent for promotional communications. The Checkout\nSession will determine whether to display an option to opt into promotional communication\nfrom the merchant depending on the customer's locale. Only available to US merchants",
        nullable=True,
    ),
    Column(
        "terms_of_service",
        String,
        comment="If set to `required`, it requires customers to accept the terms of service before being able to pay",
        nullable=True,
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["payment_pages_checkout_session_consent_collection.json"]
