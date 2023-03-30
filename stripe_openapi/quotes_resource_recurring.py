from sqlalchemy import Column, ForeignKey, Identity, Integer, String, Table

from . import metadata

QuotesResourceRecurring.Json = Table(
    "quotes_resource_recurring.json",
    metadata,
    Column(
        "amount_subtotal",
        Integer,
        comment="Total before any discounts or taxes are applied",
    ),
    Column(
        "amount_total", Integer, comment="Total after discounts and taxes are applied"
    ),
    Column(
        "interval",
        String,
        comment="The frequency at which a subscription is billed. One of `day`, `week`, `month` or `year`",
    ),
    Column(
        "interval_count",
        Integer,
        comment="The number of intervals (specified in the `interval` attribute) between subscription billings. For example, `interval=month` and `interval_count=3` bills every 3 months",
    ),
    Column(
        "total_details",
        QuotesResourceTotalDetails,
        ForeignKey("QuotesResourceTotalDetails"),
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["quotes_resource_recurring.json"]
