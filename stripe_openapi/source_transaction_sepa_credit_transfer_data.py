from sqlalchemy import Column, String, Table

from . import metadata

SourceTransactionSepaCreditTransferDataJson = Table(
    "source_transaction_sepa_credit_transfer_datajson",
    metadata,
    Column(
        "reference",
        String,
        comment="Reference associated with the transfer",
        nullable=True,
    ),
    Column("sender_iban", String, comment="Sender's bank account IBAN", nullable=True),
    Column(
        "sender_name", String, comment="Sender's name", nullable=True, primary_key=True
    ),
)
__all__ = ["source_transaction_sepa_credit_transfer_data.json"]
