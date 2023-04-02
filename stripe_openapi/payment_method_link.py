from sqlalchemy import Column, Identity, Integer, String, Table

from . import metadata

PaymentMethodLinkJson = Table(
    "payment_method_linkjson",
    metadata,
    Column(
        "country",
        String,
        comment="Two-letter ISO code representing the funding source (i.e. card, bank) country beneath the Link payment method.\nYou could use this attribute to get a sense of the international breakdown of funding sources you've collected",
        nullable=True,
    ),
    Column("email", String, comment="Account owner's email address", nullable=True),
    Column(
        "persistent_token",
        String,
        comment="Token used for persistent Link logins",
        nullable=True,
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["payment_method_link.json"]
