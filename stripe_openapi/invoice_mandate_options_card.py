from sqlalchemy import Column, Identity, Integer, String, Table

from . import metadata

InvoiceMandateOptionsCardJson = Table(
    "invoice_mandate_options_cardjson",
    metadata,
    Column(
        "amount",
        Integer,
        comment="Amount to be charged for future payments",
        nullable=True,
    ),
    Column(
        "amount_type",
        String,
        comment="One of `fixed` or `maximum`. If `fixed`, the `amount` param refers to the exact amount to be charged in future payments. If `maximum`, the amount charged can be up to the value passed for the `amount` param",
        nullable=True,
    ),
    Column(
        "description",
        String,
        comment="A description of the mandate or subscription that is meant to be displayed to the customer",
        nullable=True,
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["invoice_mandate_options_card.json"]
