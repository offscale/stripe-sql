from sqlalchemy import JSON, Column, ForeignKey, Integer, String, Table, list

from stripe_openapi.plan import Plan
from stripe_openapi.price import Price

from . import metadata

SubscriptionItem.Json = Table(
    "subscription_item.json",
    metadata,
    Column(
        "billing_thresholds",
        SubscriptionItemBillingThresholds,
        ForeignKey("SubscriptionItemBillingThresholds"),
        comment="Define thresholds at which an invoice will be sent, and the related subscription advanced to a new billing period",
        nullable=True,
    ),
    Column(
        "created",
        Integer,
        comment="Time at which the object was created. Measured in seconds since the Unix epoch",
    ),
    Column("id", String, comment="Unique identifier for the object", primary_key=True),
    Column(
        "metadata",
        JSON,
        comment="Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format",
    ),
    Column(
        "object",
        String,
        comment="String representing the object's type. Objects of the same type share the same value",
    ),
    Column("plan", Plan, ForeignKey("Plan")),
    Column("price", Price, ForeignKey("Price")),
    Column(
        "quantity",
        Integer,
        comment="The [quantity](https://stripe.com/docs/subscriptions/quantities) of the plan to which the customer should be subscribed",
        nullable=True,
    ),
    Column(
        "subscription",
        String,
        comment="The `subscription` this `subscription_item` belongs to",
    ),
    Column(
        "tax_rates",
        list,
        comment="The tax rates which apply to this `subscription_item`. When set, the `default_tax_rates` on the subscription do not apply to this `subscription_item`",
        nullable=True,
    ),
)
__all__ = ["subscription_item.json"]
