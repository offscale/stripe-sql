from sqlalchemy import Column, Identity, Integer, Table, list

from . import metadata

InvoiceThresholdReason.Json = Table(
    "invoice_threshold_reason.json",
    metadata,
    Column(
        "amount_gte",
        Integer,
        comment="The total invoice amount threshold boundary if it triggered the threshold invoice",
        nullable=True,
    ),
    Column(
        "item_reasons",
        list,
        comment="Indicates which line items triggered a threshold invoice",
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["invoice_threshold_reason.json"]
