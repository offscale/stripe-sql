from sqlalchemy import Column, Identity, Integer, Table

from . import metadata

PaymentMethodDetailsAffirmJson = Table(
    "payment_method_details_affirmjson",
    metadata,
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["payment_method_details_affirm.json"]
