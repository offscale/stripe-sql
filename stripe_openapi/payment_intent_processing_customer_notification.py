from sqlalchemy import Boolean, Column, Identity, Integer, Table

from . import metadata

PaymentIntentProcessingCustomerNotification.Json = Table(
    "payment_intent_processing_customer_notification.json",
    metadata,
    Column(
        "approval_requested",
        Boolean,
        comment="Whether customer approval has been requested for this payment. For payments greater than INR 15000 or mandate amount, the customer must provide explicit approval of the payment with their bank",
        nullable=True,
    ),
    Column(
        "completes_at",
        Integer,
        comment="If customer approval is required, they need to provide approval before this time",
        nullable=True,
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["payment_intent_processing_customer_notification.json"]
