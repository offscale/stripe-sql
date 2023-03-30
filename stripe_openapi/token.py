from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Table

from stripe_openapi.card import Card

from . import metadata

Token.Json = Table(
    "token.json",
    metadata,
    Column("bank_account", BankAccount, ForeignKey("BankAccount"), nullable=True),
    Column("card", Card, ForeignKey("Card"), nullable=True),
    Column(
        "client_ip",
        String,
        comment="IP address of the client that generated the token",
        nullable=True,
    ),
    Column(
        "created",
        Integer,
        comment="Time at which the object was created. Measured in seconds since the Unix epoch",
    ),
    Column("id", String, comment="Unique identifier for the object", primary_key=True),
    Column(
        "livemode",
        Boolean,
        comment="Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode",
    ),
    Column(
        "object",
        String,
        comment="String representing the object's type. Objects of the same type share the same value",
    ),
    Column(
        "type",
        String,
        comment="Type of the token: `account`, `bank_account`, `card`, or `pii`",
    ),
    Column(
        "used",
        Boolean,
        comment="Whether this token has already been used (tokens can be used only once)",
    ),
)
__all__ = ["token.json"]
