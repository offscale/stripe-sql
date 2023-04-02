from sqlalchemy import Column, Identity, Integer, String, Table

from . import metadata

TreasuryReceivedCreditsResourceReversalDetailsJson = Table(
    "treasury_received_credits_resource_reversal_detailsjson",
    metadata,
    Column(
        "deadline",
        Integer,
        comment="Time before which a ReceivedCredit can be reversed",
        nullable=True,
    ),
    Column(
        "restricted_reason",
        String,
        comment="Set if a ReceivedCredit cannot be reversed",
        nullable=True,
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["treasury_received_credits_resource_reversal_details.json"]
