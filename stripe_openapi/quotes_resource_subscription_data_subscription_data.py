from sqlalchemy import Column, Identity, Integer, String, Table

from . import metadata

QuotesResourceSubscriptionDataSubscriptionDataJson = Table(
    "quotes_resource_subscription_data_subscription_datajson",
    metadata,
    Column(
        "description",
        String,
        comment="The subscription's description, meant to be displayable to the customer. Use this field to optionally store an explanation of the subscription",
        nullable=True,
    ),
    Column(
        "effective_date",
        Integer,
        comment="When creating a new subscription, the date of which the subscription schedule will start after the quote is accepted. This date is ignored if it is in the past when the quote is accepted. Measured in seconds since the Unix epoch",
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
__all__ = ["quotes_resource_subscription_data_subscription_data.json"]
