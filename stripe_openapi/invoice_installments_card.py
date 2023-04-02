from sqlalchemy import Boolean, Column, Identity, Integer, Table

from . import metadata

InvoiceInstallmentsCardJson = Table(
    "invoice_installments_cardjson",
    metadata,
    Column(
        "enabled",
        Boolean,
        comment="Whether Installments are enabled for this Invoice",
        nullable=True,
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["invoice_installments_card.json"]
