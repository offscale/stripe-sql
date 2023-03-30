from sqlalchemy import Boolean, Column, String, Table

from . import metadata

DeletedInvoiceitem.Json = Table(
    "deleted_invoiceitem.json",
    metadata,
    Column("deleted", Boolean, comment="Always true for a deleted object"),
    Column("id", String, comment="Unique identifier for the object", primary_key=True),
    Column(
        "object",
        String,
        comment="String representing the object's type. Objects of the same type share the same value",
    ),
)
__all__ = ["deleted_invoiceitem.json"]
