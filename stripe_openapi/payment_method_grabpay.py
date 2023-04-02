from sqlalchemy import Column, Identity, Integer, Table

from . import metadata

PaymentMethodGrabpayJson = Table(
    "payment_method_grabpayjson",
    metadata,
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["payment_method_grabpay.json"]
