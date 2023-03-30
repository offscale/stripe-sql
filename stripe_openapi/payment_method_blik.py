from sqlalchemy import Column, Identity, Integer, Table

from . import metadata

PaymentMethodBlik.Json = Table(
    "payment_method_blik.json",
    metadata,
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["payment_method_blik.json"]
