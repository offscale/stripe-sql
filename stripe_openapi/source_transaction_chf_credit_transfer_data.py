from sqlalchemy import Column, String, Table

from . import metadata

SourceTransactionChfCreditTransferData.Json = Table(
    "source_transaction_chf_credit_transfer_data.json",
    metadata,
    Column(
        "reference",
        String,
        comment="Reference associated with the transfer",
        nullable=True,
    ),
    Column(
        "sender_address_country",
        String,
        comment="Sender's country address",
        nullable=True,
    ),
    Column(
        "sender_address_line1", String, comment="Sender's line 1 address", nullable=True
    ),
    Column("sender_iban", String, comment="Sender's bank account IBAN", nullable=True),
    Column(
        "sender_name", String, comment="Sender's name", nullable=True, primary_key=True
    ),
)
__all__ = ["source_transaction_chf_credit_transfer_data.json"]
