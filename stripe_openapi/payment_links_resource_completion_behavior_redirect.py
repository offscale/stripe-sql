from sqlalchemy import Column, Identity, Integer, String, Table

from . import metadata

PaymentLinksResourceCompletionBehaviorRedirectJson = Table(
    "payment_links_resource_completion_behavior_redirectjson",
    metadata,
    Column(
        "url",
        String,
        comment="The URL the customer will be redirected to after the purchase is complete",
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["payment_links_resource_completion_behavior_redirect.json"]
