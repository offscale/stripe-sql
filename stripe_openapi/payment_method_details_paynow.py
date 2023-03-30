from sqlalchemy import Column, Identity, Integer, String, Table

from . import metadata

PaymentMethodDetailsPaynow.Json = Table(
    "payment_method_details_paynow.json",
    metadata,
    Column(
        "reference",
        String,
        comment="Reference number associated with this PayNow payment",
        nullable=True,
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["payment_method_details_paynow.json"]
