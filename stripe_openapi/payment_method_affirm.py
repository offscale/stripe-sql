from sqlalchemy import Column, Identity, Integer, Table

from . import metadata

PaymentMethodAffirmJson = Table(
    "payment_method_affirmjson",
    metadata,
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["payment_method_affirm.json"]
