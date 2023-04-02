from sqlalchemy import Column, Identity, Integer, Table

from . import metadata

PaymentMethodGiropayJson = Table(
    "payment_method_giropayjson",
    metadata,
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["payment_method_giropay.json"]
