from sqlalchemy import Column, String, Table

from . import metadata

SourceTransactionGbpCreditTransferDataJson = Table(
    "source_transaction_gbp_credit_transfer_datajson",
    metadata,
    Column(
        "fingerprint",
        String,
        comment="Bank account fingerprint associated with the Stripe owned bank account receiving the transfer",
        nullable=True,
    ),
    Column(
        "funding_method",
        String,
        comment="The credit transfer rails the sender used to push this transfer. The possible rails are: Faster Payments, BACS, CHAPS, and wire transfers. Currently only Faster Payments is supported",
        nullable=True,
    ),
    Column(
        "last4",
        String,
        comment="Last 4 digits of sender account number associated with the transfer",
        nullable=True,
    ),
    Column(
        "reference",
        String,
        comment="Sender entered arbitrary information about the transfer",
        nullable=True,
    ),
    Column(
        "sender_account_number",
        String,
        comment="Sender account number associated with the transfer",
        nullable=True,
    ),
    Column(
        "sender_name",
        String,
        comment="Sender name associated with the transfer",
        nullable=True,
        primary_key=True,
    ),
    Column(
        "sender_sort_code",
        String,
        comment="Sender sort code associated with the transfer",
        nullable=True,
    ),
)
__all__ = ["source_transaction_gbp_credit_transfer_data.json"]
