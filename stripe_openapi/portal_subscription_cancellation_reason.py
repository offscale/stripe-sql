from sqlalchemy import ARRAY, Boolean, Column, Identity, Integer, String, Table

from . import metadata

PortalSubscriptionCancellationReason.Json = Table(
    "portal_subscription_cancellation_reason.json",
    metadata,
    Column("enabled", Boolean, comment="Whether the feature is enabled"),
    Column(
        "options",
        ARRAY(String),
        comment="Which cancellation reasons will be given as options to the customer",
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["portal_subscription_cancellation_reason.json"]
