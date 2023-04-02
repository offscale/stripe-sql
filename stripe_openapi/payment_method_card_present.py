from sqlalchemy import Column, Identity, Integer, Table

from . import metadata

PaymentMethodCardPresentJson = Table(
    "payment_method_card_presentjson",
    metadata,
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["payment_method_card_present.json"]
