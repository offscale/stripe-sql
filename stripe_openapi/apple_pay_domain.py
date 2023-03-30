from sqlalchemy import Boolean, Column, Identity, Integer, String, Table

from . import metadata

ApplePayDomain.Json = Table(
    "apple_pay_domain.json",
    metadata,
    Column(
        "created",
        Integer,
        comment="Time at which the object was created. Measured in seconds since the Unix epoch",
    ),
    Column("domain_name", String),
    Column("id", Integer, primary_key=True, server_default=Identity()),
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
)
__all__ = ["apple_pay_domain.json"]
