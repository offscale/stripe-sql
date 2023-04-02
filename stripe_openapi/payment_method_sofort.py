from sqlalchemy import Column, Identity, Integer, String, Table

from . import metadata

PaymentMethodSofortJson = Table(
    "payment_method_sofortjson",
    metadata,
    Column(
        "country",
        String,
        comment="Two-letter ISO code representing the country the bank account is located in",
        nullable=True,
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["payment_method_sofort.json"]
