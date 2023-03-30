from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Table

from stripe_openapi.period import Period

from . import metadata

UsageRecordSummary.Json = Table(
    "usage_record_summary.json",
    metadata,
    Column("id", String, comment="Unique identifier for the object", primary_key=True),
    Column(
        "invoice",
        String,
        comment="The invoice in which this usage period has been billed for",
        nullable=True,
    ),
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
    Column("period", Period, ForeignKey("Period")),
    Column(
        "subscription_item",
        String,
        comment="The ID of the subscription item this summary is describing",
    ),
    Column("total_usage", Integer, comment="The total usage within this usage period"),
)
__all__ = ["usage_record_summary.json"]
