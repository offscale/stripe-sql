from sqlalchemy import Column, Identity, Integer, String, Table

from . import metadata

SourceRedirectFlow.Json = Table(
    "source_redirect_flow.json",
    metadata,
    Column(
        "failure_reason",
        String,
        comment="The failure reason for the redirect, either `user_abort` (the customer aborted or dropped out of the redirect flow), `declined` (the authentication failed or the transaction was declined), or `processing_error` (the redirect failed due to a technical error). Present only if the redirect status is `failed`",
        nullable=True,
    ),
    Column(
        "return_url",
        String,
        comment="The URL you provide to redirect the customer to after they authenticated their payment",
    ),
    Column(
        "status",
        String,
        comment="The status of the redirect, either `pending` (ready to be used by your customer to authenticate the transaction), `succeeded` (succesful authentication, cannot be reused) or `not_required` (redirect should not be used) or `failed` (failed authentication, cannot be reused)",
    ),
    Column(
        "url",
        String,
        comment="The URL provided to you to redirect a customer to as part of a `redirect` authentication flow",
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["source_redirect_flow.json"]
