from sqlalchemy import Boolean, Column, Identity, Integer, Table

from . import metadata

SubscriptionBillingThresholdsJson = Table(
    "subscription_billing_thresholdsjson",
    metadata,
    Column(
        "amount_gte",
        Integer,
        comment="Monetary threshold that triggers the subscription to create an invoice",
        nullable=True,
    ),
    Column(
        "reset_billing_cycle_anchor",
        Boolean,
        comment="Indicates if the `billing_cycle_anchor` should be reset when a threshold is reached. If true, `billing_cycle_anchor` will be updated to the date/time the threshold was last reached; otherwise, the value will remain unchanged. This value may not be `true` if the subscription contains items with plans that have `aggregate_usage=last_ever`",
        nullable=True,
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["subscription_billing_thresholds.json"]
