from sqlalchemy import Column, Identity, Integer, String, Table

from . import metadata

PaymentMethodDetailsOxxo.Json = Table(
    "payment_method_details_oxxo.json",
    metadata,
    Column("number", String, comment="OXXO reference number", nullable=True),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["payment_method_details_oxxo.json"]
