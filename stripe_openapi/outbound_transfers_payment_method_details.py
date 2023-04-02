from sqlalchemy import Column, ForeignKey, Identity, Integer, String, Table

from . import metadata

OutboundTransfersPaymentMethodDetailsJson = Table(
    "outbound_transfers_payment_method_detailsjson",
    metadata,
    Column(
        "billing_details",
        TreasurySharedResourceBillingDetails,
        ForeignKey("TreasurySharedResourceBillingDetails"),
    ),
    Column(
        "type",
        String,
        comment="The type of the payment method used in the OutboundTransfer",
    ),
    Column(
        "us_bank_account",
        OutboundTransfersPaymentMethodDetailsUsBankAccount,
        ForeignKey("OutboundTransfersPaymentMethodDetailsUsBankAccount"),
        nullable=True,
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["outbound_transfers_payment_method_details.json"]
