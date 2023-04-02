from sqlalchemy import Column, Identity, Integer, Table

from . import metadata

PaymentMethodPixJson = Table(
    "payment_method_pixjson",
    metadata,
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["payment_method_pix.json"]
