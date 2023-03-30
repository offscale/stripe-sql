from sqlalchemy import Column, Identity, Integer, String, Table

from . import metadata

PaymentIntentNextActionKonbiniLawson.Json = Table(
    "payment_intent_next_action_konbini_lawson.json",
    metadata,
    Column(
        "confirmation_number", String, comment="The confirmation number", nullable=True
    ),
    Column("payment_code", String, comment="The payment code"),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["payment_intent_next_action_konbini_lawson.json"]
