from sqlalchemy import Column, Identity, Integer, Table

from . import metadata

PaymentMethodDetailsBlikJson = Table(
    "payment_method_details_blikjson",
    metadata,
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["payment_method_details_blik.json"]
