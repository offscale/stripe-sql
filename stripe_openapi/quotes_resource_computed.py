from sqlalchemy import Column, ForeignKey, Identity, Integer, Table

from . import metadata

QuotesResourceComputedJson = Table(
    "quotes_resource_computedjson",
    metadata,
    Column(
        "recurring",
        QuotesResourceRecurring,
        ForeignKey("QuotesResourceRecurring"),
        comment="The definitive totals and line items the customer will be charged on a recurring basis. Takes into account the line items with recurring prices and discounts with `duration=forever` coupons only. Defaults to `null` if no inputted line items with recurring prices",
        nullable=True,
    ),
    Column("upfront", QuotesResourceUpfront, ForeignKey("QuotesResourceUpfront")),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["quotes_resource_computed.json"]
