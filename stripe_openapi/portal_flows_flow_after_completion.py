from sqlalchemy import Column, ForeignKey, Identity, Integer, String, Table

from . import metadata

PortalFlowsFlowAfterCompletion.Json = Table(
    "portal_flows_flow_after_completion.json",
    metadata,
    Column(
        "hosted_confirmation",
        PortalFlowsAfterCompletionHostedConfirmation,
        ForeignKey("PortalFlowsAfterCompletionHostedConfirmation"),
        comment="Configuration when `after_completion.type=hosted_confirmation`",
        nullable=True,
    ),
    Column(
        "redirect",
        PortalFlowsAfterCompletionRedirect,
        ForeignKey("PortalFlowsAfterCompletionRedirect"),
        comment="Configuration when `after_completion.type=redirect`",
        nullable=True,
    ),
    Column(
        "type",
        String,
        comment="The specified type of behavior after the flow is completed",
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["portal_flows_flow_after_completion.json"]
