from sqlalchemy import Column, Identity, Integer, String, Table

from . import metadata

TreasuryInboundTransfersResourceInboundTransferResourceLinkedFlowsJson = Table(
    "treasury_inbound_transfers_resource_inbound_transfer_resource_linked_flowsjson",
    metadata,
    Column(
        "received_debit",
        String,
        comment="If funds for this flow were returned after the flow went to the `succeeded` state, this field contains a reference to the ReceivedDebit return",
        nullable=True,
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = [
    "treasury_inbound_transfers_resource_inbound_transfer_resource_linked_flows.json"
]
