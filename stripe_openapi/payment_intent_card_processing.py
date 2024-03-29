from sqlalchemy import Column, ForeignKey, Identity, Integer, Table

from . import metadata

PaymentIntentCardProcessingJson = Table(
    "payment_intent_card_processingjson",
    metadata,
    Column(
        "customer_notification",
        PaymentIntentProcessingCustomerNotification,
        ForeignKey("PaymentIntentProcessingCustomerNotification"),
        nullable=True,
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["payment_intent_card_processing.json"]
