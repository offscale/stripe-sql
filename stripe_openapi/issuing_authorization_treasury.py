from sqlalchemy import ARRAY, Column, Identity, Integer, String, Table

from . import metadata

IssuingAuthorizationTreasuryJson = Table(
    "issuing_authorization_treasuryjson",
    metadata,
    Column(
        "received_credits",
        ARRAY(String),
        comment="The array of [ReceivedCredits](https://stripe.com/docs/api/treasury/received_credits) associated with this authorization",
    ),
    Column(
        "received_debits",
        ARRAY(String),
        comment="The array of [ReceivedDebits](https://stripe.com/docs/api/treasury/received_debits) associated with this authorization",
    ),
    Column(
        "transaction",
        String,
        comment="The Treasury [Transaction](https://stripe.com/docs/api/treasury/transactions) associated with this authorization",
        nullable=True,
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["issuing_authorization_treasury.json"]
