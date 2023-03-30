from sqlalchemy import Column, ForeignKey, Identity, Integer, Table

from . import metadata

InvoicesLineItemsProrationDetails.Json = Table(
    "invoices_line_items_proration_details.json",
    metadata,
    Column(
        "credited_items",
        InvoicesLineItemsCreditedItems,
        ForeignKey("InvoicesLineItemsCreditedItems"),
        comment="For a credit proration `line_item`, the original debit line_items to which the credit proration applies",
        nullable=True,
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["invoices_line_items_proration_details.json"]
