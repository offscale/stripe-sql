from sqlalchemy import Column, Identity, Integer, String, Table

from . import metadata

TreasuryInboundTransfersResourceFailureDetailsJson = Table(
    "treasury_inbound_transfers_resource_failure_detailsjson",
    metadata,
    Column("code", String, comment="Reason for the failure"),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["treasury_inbound_transfers_resource_failure_details.json"]
