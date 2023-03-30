from sqlalchemy import Column, Identity, Integer, Table

from . import metadata

TreasuryInboundTransfersResourceInboundTransferResourceStatusTransitions.Json = Table(
    "treasury_inbound_transfers_resource_inbound_transfer_resource_status_transitions.json",
    metadata,
    Column(
        "canceled_at",
        Integer,
        comment="Timestamp describing when an InboundTransfer changed status to `canceled`",
        nullable=True,
    ),
    Column(
        "failed_at",
        Integer,
        comment="Timestamp describing when an InboundTransfer changed status to `failed`",
        nullable=True,
    ),
    Column(
        "succeeded_at",
        Integer,
        comment="Timestamp describing when an InboundTransfer changed status to `succeeded`",
        nullable=True,
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = [
    "treasury_inbound_transfers_resource_inbound_transfer_resource_status_transitions.json"
]
