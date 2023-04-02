from sqlalchemy import Column, Identity, Integer, Table

from . import metadata

PaymentMethodPromptpayJson = Table(
    "payment_method_promptpayjson",
    metadata,
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["payment_method_promptpay.json"]
