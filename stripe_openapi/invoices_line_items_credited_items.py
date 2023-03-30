from sqlalchemy import ARRAY, Column, Identity, Integer, String, Table

from . import metadata

InvoicesLineItemsCreditedItems.Json = Table(
    "invoices_line_items_credited_items.json",
    metadata,
    Column(
        "invoice", String, comment="Invoice containing the credited invoice line items"
    ),
    Column("invoice_line_items", ARRAY(String), comment="Credited invoice line items"),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["invoices_line_items_credited_items.json"]
