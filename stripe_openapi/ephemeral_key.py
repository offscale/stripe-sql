from sqlalchemy import Boolean, Column, Integer, String, Table

from . import metadata

EphemeralKeyJson = Table(
    "ephemeral_keyjson",
    metadata,
    Column(
        "created",
        Integer,
        comment="Time at which the object was created. Measured in seconds since the Unix epoch",
    ),
    Column(
        "expires",
        Integer,
        comment="Time at which the key will expire. Measured in seconds since the Unix epoch",
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
        "secret",
        String,
        comment="The key's secret. You can use this value to make authorized requests to the Stripe API",
        nullable=True,
    ),
)
__all__ = ["ephemeral_key.json"]
