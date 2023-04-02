from sqlalchemy import Column, Identity, Integer, Table

from . import metadata

PaymentMethodAfterpayClearpayJson = Table(
    "payment_method_afterpay_clearpayjson",
    metadata,
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["payment_method_afterpay_clearpay.json"]
