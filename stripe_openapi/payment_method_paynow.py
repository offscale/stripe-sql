from sqlalchemy import Column, Identity, Integer, Table

from . import metadata

PaymentMethodPaynowJson = Table(
    "payment_method_paynowjson",
    metadata,
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["payment_method_paynow.json"]
