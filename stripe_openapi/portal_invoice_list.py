from sqlalchemy import Boolean, Column, Identity, Integer, Table

from . import metadata

PortalInvoiceListJson = Table(
    "portal_invoice_listjson",
    metadata,
    Column("enabled", Boolean, comment="Whether the feature is enabled"),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["portal_invoice_list.json"]
