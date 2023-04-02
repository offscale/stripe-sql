from sqlalchemy import ARRAY, Column, Identity, Integer, String, Table

from . import metadata

PortalSubscriptionUpdateProductJson = Table(
    "portal_subscription_update_productjson",
    metadata,
    Column(
        "prices",
        ARRAY(String),
        comment="The list of price IDs which, when subscribed to, a subscription can be updated",
    ),
    Column("product", String, comment="The product ID"),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["portal_subscription_update_product.json"]
