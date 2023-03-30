from sqlalchemy import JSON, Column, ForeignKey, Identity, Integer, Table

from . import metadata

QuotesResourceUpfront.Json = Table(
    "quotes_resource_upfront.json",
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
        "line_items",
        JSON,
        comment="The line items that will appear on the next invoice after this quote is accepted. This does not include pending invoice items that exist on the customer but may still be included in the next invoice",
        nullable=True,
    ),
    Column(
        "total_details",
        QuotesResourceTotalDetails,
        ForeignKey("QuotesResourceTotalDetails"),
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["quotes_resource_upfront.json"]
