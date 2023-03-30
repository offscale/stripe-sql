from sqlalchemy import Column, Identity, Integer, String, Table

from . import metadata

PortalFlowsFlowSubscriptionCancel.Json = Table(
    "portal_flows_flow_subscription_cancel.json",
    metadata,
    Column("subscription", String, comment="The ID of the subscription to be canceled"),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["portal_flows_flow_subscription_cancel.json"]
