from sqlalchemy import Column, Identity, Integer, Table

from . import metadata

TreasuryReceivedCreditsResourceStatusTransitionsJson = Table(
    "treasury_received_credits_resource_status_transitionsjson",
    metadata,
    Column(
        "posted_at",
        Integer,
        comment="Timestamp describing when the CreditReversal changed status to `posted`",
        nullable=True,
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["treasury_received_credits_resource_status_transitions.json"]
