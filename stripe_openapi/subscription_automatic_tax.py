from sqlalchemy import Boolean, Column, Identity, Integer, Table

from . import metadata

SubscriptionAutomaticTaxJson = Table(
    "subscription_automatic_taxjson",
    metadata,
    Column(
        "enabled",
        Boolean,
        comment="Whether Stripe automatically computes tax on this subscription",
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["subscription_automatic_tax.json"]
