from sqlalchemy import Column, Identity, Integer, String, Table

from . import metadata

PaymentIntentNextActionDisplayOxxoDetails.Json = Table(
    "payment_intent_next_action_display_oxxo_details.json",
    metadata,
    Column(
        "expires_after",
        Integer,
        comment="The timestamp after which the OXXO voucher expires",
        nullable=True,
    ),
    Column(
        "hosted_voucher_url",
        String,
        comment="The URL for the hosted OXXO voucher page, which allows customers to view and print an OXXO voucher",
        nullable=True,
    ),
    Column("number", String, comment="OXXO reference number", nullable=True),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["payment_intent_next_action_display_oxxo_details.json"]
