from sqlalchemy import Column, ForeignKey, Identity, Integer, String, Table

from . import metadata

PaymentIntentProcessingJson = Table(
    "payment_intent_processingjson",
    metadata,
    Column(
        "card",
        PaymentIntentCardProcessing,
        ForeignKey("PaymentIntentCardProcessing"),
        nullable=True,
    ),
    Column(
        "type",
        String,
        comment="Type of the payment method for which payment is in `processing` state, one of `card`",
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["payment_intent_processing.json"]
