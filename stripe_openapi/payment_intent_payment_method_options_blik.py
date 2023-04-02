from sqlalchemy import Column, Identity, Integer, Table

from . import metadata

PaymentIntentPaymentMethodOptionsBlikJson = Table(
    "payment_intent_payment_method_options_blikjson",
    metadata,
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["payment_intent_payment_method_options_blik.json"]
