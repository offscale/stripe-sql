from sqlalchemy import Column, Identity, Integer, String, Table

from . import metadata

SourceTransactionAchCreditTransferData.Json = Table(
    "source_transaction_ach_credit_transfer_data.json",
    metadata,
    Column(
        "customer_data",
        String,
        comment="Customer data associated with the transfer",
        nullable=True,
    ),
    Column(
        "fingerprint",
        String,
        comment="Bank account fingerprint associated with the transfer",
        nullable=True,
    ),
    Column(
        "last4",
        String,
        comment="Last 4 digits of the account number associated with the transfer",
        nullable=True,
    ),
    Column(
        "routing_number",
        String,
        comment="Routing number associated with the transfer",
        nullable=True,
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["source_transaction_ach_credit_transfer_data.json"]
