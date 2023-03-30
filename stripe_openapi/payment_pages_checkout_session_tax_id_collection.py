from sqlalchemy import Boolean, Column, Identity, Integer, Table

from . import metadata

PaymentPagesCheckoutSessionTaxIdCollection.Json = Table(
    "payment_pages_checkout_session_tax_id_collection.json",
    metadata,
    Column(
        "enabled",
        Boolean,
        comment="Indicates whether tax ID collection is enabled for the session",
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["payment_pages_checkout_session_tax_id_collection.json"]
