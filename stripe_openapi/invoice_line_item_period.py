from sqlalchemy import Column, Identity, Integer, Table

from . import metadata

InvoiceLineItemPeriodJson = Table(
    "invoice_line_item_periodjson",
    metadata,
    Column(
        "end",
        Integer,
        comment="The end of the period, which must be greater than or equal to the start. This value is inclusive",
    ),
    Column(
        "start", Integer, comment="The start of the period. This value is inclusive"
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["invoice_line_item_period.json"]
