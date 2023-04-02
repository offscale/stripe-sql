from sqlalchemy import Column, Identity, Integer, Table

from . import metadata

TreasuryReceivedDebitsResourceStatusTransitionsJson = Table(
    "treasury_received_debits_resource_status_transitionsjson",
    metadata,
    Column(
        "completed_at",
        Integer,
        comment="Timestamp describing when the DebitReversal changed status to `completed`",
        nullable=True,
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["treasury_received_debits_resource_status_transitions.json"]
