from sqlalchemy import Column, Identity, Integer, String, Table

from . import metadata

PaymentMethodPJson = Table(
    "payment_method_pjson",
    metadata,
    Column("bank", String, comment="The customer's bank, if provided", nullable=True),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["payment_method_p24.json"]
