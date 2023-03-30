from sqlalchemy import Column, Identity, Integer, String, Table

from . import metadata

AccountLink.Json = Table(
    "account_link.json",
    metadata,
    Column(
        "created",
        Integer,
        comment="Time at which the object was created. Measured in seconds since the Unix epoch",
    ),
    Column(
        "expires_at",
        Integer,
        comment="The timestamp at which this account link will expire",
    ),
    Column(
        "object",
        String,
        comment="String representing the object's type. Objects of the same type share the same value",
    ),
    Column("url", String, comment="The URL for the account link"),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["account_link.json"]
