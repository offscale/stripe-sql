from sqlalchemy import ARRAY, Column, Integer, String, Table

from . import metadata

InvoiceItemThresholdReason.Json = Table(
    "invoice_item_threshold_reason.json",
    metadata,
    Column(
        "line_item_ids",
        ARRAY(String),
        comment="The IDs of the line items that triggered the threshold invoice",
        primary_key=True,
    ),
    Column(
        "usage_gte",
        Integer,
        comment="The quantity threshold boundary that applied to the given line item",
    ),
)
__all__ = ["invoice_item_threshold_reason.json"]
