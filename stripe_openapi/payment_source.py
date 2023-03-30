from sqlalchemy import Column, Identity, Integer, Table

from . import metadata

PaymentSource.Json = Table(
    "payment_source.json",
    metadata,
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["payment_source.json"]
