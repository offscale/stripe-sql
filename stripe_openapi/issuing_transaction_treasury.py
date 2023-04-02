from sqlalchemy import Column, Identity, Integer, String, Table

from . import metadata

IssuingTransactionTreasuryJson = Table(
    "issuing_transaction_treasuryjson",
    metadata,
    Column(
        "received_credit",
        String,
        comment="The Treasury [ReceivedCredit](https://stripe.com/docs/api/treasury/received_credits) representing this Issuing transaction if it is a refund",
        nullable=True,
    ),
    Column(
        "received_debit",
        String,
        comment="The Treasury [ReceivedDebit](https://stripe.com/docs/api/treasury/received_debits) representing this Issuing transaction if it is a capture",
        nullable=True,
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["issuing_transaction_treasury.json"]
