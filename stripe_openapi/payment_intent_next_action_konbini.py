from sqlalchemy import Column, ForeignKey, Identity, Integer, String, Table

from . import metadata

PaymentIntentNextActionKonbiniJson = Table(
    "payment_intent_next_action_konbinijson",
    metadata,
    Column(
        "expires_at",
        Integer,
        comment="The timestamp at which the pending Konbini payment expires",
    ),
    Column(
        "hosted_voucher_url",
        String,
        comment="The URL for the Konbini payment instructions page, which allows customers to view and print a Konbini voucher",
        nullable=True,
    ),
    Column(
        "stores",
        PaymentIntentNextActionKonbiniStores,
        ForeignKey("PaymentIntentNextActionKonbiniStores"),
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["payment_intent_next_action_konbini.json"]
