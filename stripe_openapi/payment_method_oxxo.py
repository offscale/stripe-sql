from sqlalchemy import Column, Identity, Integer, Table

from . import metadata

PaymentMethodOxxoJson = Table(
    "payment_method_oxxojson",
    metadata,
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["payment_method_oxxo.json"]
