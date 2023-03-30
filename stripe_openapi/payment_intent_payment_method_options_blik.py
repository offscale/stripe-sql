from sqlalchemy import Column, Identity, Integer, Table

from . import metadata

PaymentIntentPaymentMethodOptionsBlik.Json = Table(
    "payment_intent_payment_method_options_blik.json",
    metadata,
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["payment_intent_payment_method_options_blik.json"]
