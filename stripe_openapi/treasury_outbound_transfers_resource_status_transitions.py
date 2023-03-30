from sqlalchemy import Column, Identity, Integer, Table

from . import metadata

TreasuryOutboundTransfersResourceStatusTransitions.Json = Table(
    "treasury_outbound_transfers_resource_status_transitions.json",
    metadata,
    Column(
        "canceled_at",
        Integer,
        comment="Timestamp describing when an OutboundTransfer changed status to `canceled`",
        nullable=True,
    ),
    Column(
        "failed_at",
        Integer,
        comment="Timestamp describing when an OutboundTransfer changed status to `failed`",
        nullable=True,
    ),
    Column(
        "posted_at",
        Integer,
        comment="Timestamp describing when an OutboundTransfer changed status to `posted`",
        nullable=True,
    ),
    Column(
        "returned_at",
        Integer,
        comment="Timestamp describing when an OutboundTransfer changed status to `returned`",
        nullable=True,
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["treasury_outbound_transfers_resource_status_transitions.json"]
