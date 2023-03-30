from sqlalchemy import Boolean, Column, Identity, Integer, Table

from . import metadata

PaymentIntentNextActionCardAwaitNotification.Json = Table(
    "payment_intent_next_action_card_await_notification.json",
    metadata,
    Column(
        "charge_attempt_at",
        Integer,
        comment="The time that payment will be attempted. If customer approval is required, they need to provide approval before this time",
        nullable=True,
    ),
    Column(
        "customer_approval_required",
        Boolean,
        comment="For payments greater than INR 15000, the customer must provide explicit approval of the payment with their bank. For payments of lower amount, no customer action is required",
        nullable=True,
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["payment_intent_next_action_card_await_notification.json"]
