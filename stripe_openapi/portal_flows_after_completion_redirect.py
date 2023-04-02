from sqlalchemy import Column, Identity, Integer, String, Table

from . import metadata

PortalFlowsAfterCompletionRedirectJson = Table(
    "portal_flows_after_completion_redirectjson",
    metadata,
    Column(
        "return_url",
        String,
        comment="The URL the customer will be redirected to after the flow is completed",
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["portal_flows_after_completion_redirect.json"]
