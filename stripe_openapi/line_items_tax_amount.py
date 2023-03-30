from sqlalchemy import Column, ForeignKey, Identity, Integer, Table

from . import metadata

LineItemsTaxAmount.Json = Table(
    "line_items_tax_amount.json",
    metadata,
    Column("amount", Integer, comment="Amount of tax applied for this rate"),
    Column("rate", TaxRate, ForeignKey("TaxRate")),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["line_items_tax_amount.json"]
