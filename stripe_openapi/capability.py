from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Table

from stripe_openapi.account import Account

from . import metadata

CapabilityJson = Table(
    "capabilityjson",
    metadata,
    Column(
        "account",
        Account,
        ForeignKey("Account"),
        comment="The account for which the capability enables functionality",
    ),
    Column(
        "future_requirements",
        AccountCapabilityFutureRequirements,
        ForeignKey("AccountCapabilityFutureRequirements"),
        nullable=True,
    ),
    Column("id", String, comment="The identifier for the capability", primary_key=True),
    Column(
        "object",
        String,
        comment="String representing the object's type. Objects of the same type share the same value",
    ),
    Column("requested", Boolean, comment="Whether the capability has been requested"),
    Column(
        "requested_at",
        Integer,
        comment="Time at which the capability was requested. Measured in seconds since the Unix epoch",
        nullable=True,
    ),
    Column(
        "requirements",
        AccountCapabilityRequirements,
        ForeignKey("AccountCapabilityRequirements"),
        nullable=True,
    ),
    Column(
        "status",
        String,
        comment="The status of the capability. Can be `active`, `inactive`, `pending`, or `unrequested`",
    ),
)
__all__ = ["capability.json"]
