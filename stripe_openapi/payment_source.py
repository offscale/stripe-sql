from sqlalchemy import Column, Identity, Integer, Table

from . import metadata

PaymentSourceJson = Table(
    "payment_sourcejson",
    metadata,
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["payment_source.json"]
