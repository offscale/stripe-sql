from sqlalchemy import Column, Identity, Integer, String, Table

from . import metadata

PaymentLinksResourceSubscriptionDataJson = Table(
    "payment_links_resource_subscription_datajson",
    metadata,
    Column(
        "description",
        String,
        comment="The subscription's description, meant to be displayable to the customer. Use this field to optionally store an explanation of the subscription",
        nullable=True,
    ),
    Column(
        "trial_period_days",
        Integer,
        comment="Integer representing the number of trial period days before the customer is charged for the first time",
        nullable=True,
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["payment_links_resource_subscription_data.json"]
