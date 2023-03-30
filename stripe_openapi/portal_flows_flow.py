from sqlalchemy import Column, ForeignKey, Identity, Integer, String, Table

from . import metadata

PortalFlowsFlow.Json = Table(
    "portal_flows_flow.json",
    metadata,
    Column(
        "after_completion",
        PortalFlowsFlowAfterCompletion,
        ForeignKey("PortalFlowsFlowAfterCompletion"),
    ),
    Column(
        "subscription_cancel",
        PortalFlowsFlowSubscriptionCancel,
        ForeignKey("PortalFlowsFlowSubscriptionCancel"),
        comment="Configuration when `flow.type=subscription_cancel`",
        nullable=True,
    ),
    Column("type", String, comment="Type of flow that the customer will go through"),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["portal_flows_flow.json"]
