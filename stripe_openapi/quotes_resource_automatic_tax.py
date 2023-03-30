from sqlalchemy import Boolean, Column, Identity, Integer, String, Table

from . import metadata

QuotesResourceAutomaticTax.Json = Table(
    "quotes_resource_automatic_tax.json",
    metadata,
    Column("enabled", Boolean, comment="Automatically calculate taxes"),
    Column(
        "status",
        String,
        comment="The status of the most recent automated tax calculation for this quote",
        nullable=True,
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["quotes_resource_automatic_tax.json"]
