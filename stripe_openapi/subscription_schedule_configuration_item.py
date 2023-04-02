from sqlalchemy import JSON, Column, ForeignKey, Identity, Integer, Table, list

from stripe_openapi.plan import Plan
from stripe_openapi.price import Price

from . import metadata

SubscriptionScheduleConfigurationItemJson = Table(
    "subscription_schedule_configuration_itemjson",
    metadata,
    Column(
        "billing_thresholds",
        SubscriptionItemBillingThresholds,
        ForeignKey("SubscriptionItemBillingThresholds"),
        comment="Define thresholds at which an invoice will be sent, and the related subscription advanced to a new billing period",
        nullable=True,
    ),
    Column(
        "metadata",
        JSON,
        comment="Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an item. Metadata on this item will update the underlying subscription item's `metadata` when the phase is entered",
        nullable=True,
    ),
    Column(
        "plan",
        Plan,
        ForeignKey("DeletedPlan"),
        comment="ID of the plan to which the customer should be subscribed",
    ),
    Column(
        "price",
        Price,
        ForeignKey("DeletedPrice"),
        comment="ID of the price to which the customer should be subscribed",
    ),
    Column(
        "quantity",
        Integer,
        comment="Quantity of the plan to which the customer should be subscribed",
        nullable=True,
    ),
    Column(
        "tax_rates",
        list,
        comment="The tax rates which apply to this `phase_item`. When set, the `default_tax_rates` on the phase do not apply to this `phase_item`",
        nullable=True,
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["subscription_schedule_configuration_item.json"]
