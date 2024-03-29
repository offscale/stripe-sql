from sqlalchemy import Boolean, Column, Identity, Integer, Table

from . import metadata

PaymentLinksResourceAutomaticTaxJson = Table(
    "payment_links_resource_automatic_taxjson",
    metadata,
    Column(
        "enabled",
        Boolean,
        comment="If `true`, tax will be calculated automatically using the customer's location",
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["payment_links_resource_automatic_tax.json"]
