from sqlalchemy import Column, ForeignKey, Identity, Integer, Table

from . import metadata

QuotesResourceTotalDetailsJson = Table(
    "quotes_resource_total_detailsjson",
    metadata,
    Column("amount_discount", Integer, comment="This is the sum of all the discounts"),
    Column(
        "amount_shipping",
        Integer,
        comment="This is the sum of all the shipping amounts",
        nullable=True,
    ),
    Column("amount_tax", Integer, comment="This is the sum of all the tax amounts"),
    Column(
        "breakdown",
        QuotesResourceTotalDetailsResourceBreakdown,
        ForeignKey("QuotesResourceTotalDetailsResourceBreakdown"),
        nullable=True,
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["quotes_resource_total_details.json"]
