from sqlalchemy import Column, ForeignKey, Identity, Integer, String, Table

from . import metadata

InboundTransfers.Json = Table(
    "inbound_transfers.json",
    metadata,
    Column(
        "billing_details",
        TreasurySharedResourceBillingDetails,
        ForeignKey("TreasurySharedResourceBillingDetails"),
    ),
    Column(
        "type",
        String,
        comment="The type of the payment method used in the InboundTransfer",
    ),
    Column(
        "us_bank_account",
        InboundTransfersPaymentMethodDetailsUsBankAccount,
        ForeignKey("InboundTransfersPaymentMethodDetailsUsBankAccount"),
        nullable=True,
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["inbound_transfers.json"]
