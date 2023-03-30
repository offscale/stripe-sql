from sqlalchemy import Column, Identity, Integer, String, Table

from . import metadata

TreasuryInboundTransfersResourceFailureDetails.Json = Table(
    "treasury_inbound_transfers_resource_failure_details.json",
    metadata,
    Column("code", String, comment="Reason for the failure"),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["treasury_inbound_transfers_resource_failure_details.json"]
