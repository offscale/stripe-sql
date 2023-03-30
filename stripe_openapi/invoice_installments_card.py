from sqlalchemy import Boolean, Column, Identity, Integer, Table

from . import metadata

InvoiceInstallmentsCard.Json = Table(
    "invoice_installments_card.json",
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
