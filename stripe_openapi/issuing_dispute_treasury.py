from sqlalchemy import Column, Identity, Integer, String, Table

from . import metadata

IssuingDisputeTreasury.Json = Table(
    "issuing_dispute_treasury.json",
    metadata,
    Column(
        "debit_reversal",
        String,
        comment="The Treasury [DebitReversal](https://stripe.com/docs/api/treasury/debit_reversals) representing this Issuing dispute",
        nullable=True,
    ),
    Column(
        "received_debit",
        String,
        comment="The Treasury [ReceivedDebit](https://stripe.com/docs/api/treasury/received_debits) that is being disputed",
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["issuing_dispute_treasury.json"]
