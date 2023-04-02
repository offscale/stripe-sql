from sqlalchemy import ARRAY, Boolean, Column, Identity, Integer, String, Table, list

from . import metadata

PortalSubscriptionUpdateJson = Table(
    "portal_subscription_updatejson",
    metadata,
    Column(
        "default_allowed_updates",
        ARRAY(String),
        comment="The types of subscription updates that are supported for items listed in the `products` attribute. When empty, subscriptions are not updateable",
    ),
    Column("enabled", Boolean, comment="Whether the feature is enabled"),
    Column(
        "products",
        list,
        comment="The list of products that support subscription updates",
        nullable=True,
    ),
    Column(
        "proration_behavior",
        String,
        comment="Determines how to handle prorations resulting from subscription updates. Valid values are `none`, `create_prorations`, and `always_invoice`",
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["portal_subscription_update.json"]
