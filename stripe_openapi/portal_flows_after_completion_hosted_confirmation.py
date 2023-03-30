from sqlalchemy import Column, Identity, Integer, String, Table

from . import metadata

PortalFlowsAfterCompletionHostedConfirmation.Json = Table(
    "portal_flows_after_completion_hosted_confirmation.json",
    metadata,
    Column(
        "custom_message",
        String,
        comment="A custom message to display to the customer after the flow is completed",
        nullable=True,
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["portal_flows_after_completion_hosted_confirmation.json"]
