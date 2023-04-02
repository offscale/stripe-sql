from sqlalchemy import Column, ForeignKey, Identity, Integer, String, Table

from stripe_openapi.invoice import Invoice

from . import metadata

InvoicesFromInvoiceJson = Table(
    "invoices_from_invoicejson",
    metadata,
    Column(
        "action",
        String,
        comment="The relation between this invoice and the cloned invoice",
    ),
    Column(
        "invoice", Invoice, ForeignKey("Invoice"), comment="The invoice that was cloned"
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["invoices_from_invoice.json"]
