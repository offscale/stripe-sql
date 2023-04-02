from sqlalchemy import Column, Identity, Integer, Table

from . import metadata

PaymentMethodKonbiniJson = Table(
    "payment_method_konbinijson",
    metadata,
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["payment_method_konbini.json"]
