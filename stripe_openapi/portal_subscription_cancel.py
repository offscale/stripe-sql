from sqlalchemy import Boolean, Column, ForeignKey, Identity, Integer, String, Table

from . import metadata

PortalSubscriptionCancel.Json = Table(
    "portal_subscription_cancel.json",
    metadata,
    Column(
        "cancellation_reason",
        PortalSubscriptionCancellationReason,
        ForeignKey("PortalSubscriptionCancellationReason"),
    ),
    Column("enabled", Boolean, comment="Whether the feature is enabled"),
    Column(
        "mode",
        String,
        comment="Whether to cancel subscriptions immediately or at the end of the billing period",
    ),
    Column(
        "proration_behavior",
        String,
        comment="Whether to create prorations when canceling subscriptions. Possible values are `none` and `create_prorations`",
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["portal_subscription_cancel.json"]
