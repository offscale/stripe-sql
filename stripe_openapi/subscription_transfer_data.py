from sqlalchemy import Column, Float, ForeignKey, Identity, Integer, Table

from stripe_openapi.account import Account

from . import metadata

SubscriptionTransferData.Json = Table(
    "subscription_transfer_data.json",
    metadata,
    Column(
        "amount_percent",
        Float,
        comment="A non-negative decimal between 0 and 100, with at most two decimal places. This represents the percentage of the subscription invoice subtotal that will be transferred to the destination account. By default, the entire amount is transferred to the destination",
        nullable=True,
    ),
    Column(
        "destination",
        Account,
        ForeignKey("Account"),
        comment="The account where funds from the payment will be transferred to upon payment success",
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["subscription_transfer_data.json"]
