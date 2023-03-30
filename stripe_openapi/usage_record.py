from sqlalchemy import Boolean, Column, Integer, String, Table

from . import metadata

UsageRecord.Json = Table(
    "usage_record.json",
    metadata,
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
    Column("quantity", Integer, comment="The usage quantity for the specified date"),
    Column(
        "subscription_item",
        String,
        comment="The ID of the subscription item this usage record contains data for",
    ),
    Column("timestamp", Integer, comment="The timestamp when this usage occurred"),
)
__all__ = ["usage_record.json"]
