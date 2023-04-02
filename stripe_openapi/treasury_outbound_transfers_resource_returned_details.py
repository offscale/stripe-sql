from sqlalchemy import Column, ForeignKey, Identity, Integer, String, Table

from stripe_openapi.treasury__transaction import Treasury__Transaction

from . import metadata

TreasuryOutboundTransfersResourceReturnedDetailsJson = Table(
    "treasury_outbound_transfers_resource_returned_detailsjson",
    metadata,
    Column("code", String, comment="Reason for the return"),
    Column(
        "transaction",
        Treasury__Transaction,
        ForeignKey("Treasury__Transaction"),
        comment="The Transaction associated with this object",
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["treasury_outbound_transfers_resource_returned_details.json"]
