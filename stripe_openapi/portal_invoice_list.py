from sqlalchemy import Boolean, Column, Identity, Integer, Table

from . import metadata

PortalInvoiceList.Json = Table(
    "portal_invoice_list.json",
    metadata,
    Column("enabled", Boolean, comment="Whether the feature is enabled"),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["portal_invoice_list.json"]
