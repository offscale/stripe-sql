from sqlalchemy import Column, Identity, Integer, String, Table

from . import metadata

TreasuryReceivedDebitsResourceReversalDetailsJson = Table(
    "treasury_received_debits_resource_reversal_detailsjson",
    metadata,
    Column(
        "deadline",
        Integer,
        comment="Time before which a ReceivedDebit can be reversed",
        nullable=True,
    ),
    Column(
        "restricted_reason",
        String,
        comment="Set if a ReceivedDebit can't be reversed",
        nullable=True,
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["treasury_received_debits_resource_reversal_details.json"]
