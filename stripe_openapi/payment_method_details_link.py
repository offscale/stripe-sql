from sqlalchemy import Column, Identity, Integer, String, Table

from . import metadata

PaymentMethodDetailsLink.Json = Table(
    "payment_method_details_link.json",
    metadata,
    Column(
        "country",
        String,
        comment="Two-letter ISO code representing the funding source country beneath the Link payment.\nYou could use this attribute to get a sense of international fees",
        nullable=True,
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["payment_method_details_link.json"]
