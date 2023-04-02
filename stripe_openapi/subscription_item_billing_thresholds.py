from sqlalchemy import Column, Identity, Integer, Table

from . import metadata

SubscriptionItemBillingThresholdsJson = Table(
    "subscription_item_billing_thresholdsjson",
    metadata,
    Column(
        "usage_gte",
        Integer,
        comment="Usage threshold that triggers the subscription to create an invoice",
        nullable=True,
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["subscription_item_billing_thresholds.json"]
