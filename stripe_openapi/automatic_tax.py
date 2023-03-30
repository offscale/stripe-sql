from sqlalchemy import Boolean, Column, Identity, Integer, String, Table

from . import metadata

AutomaticTax.Json = Table(
    "automatic_tax.json",
    metadata,
    Column(
        "enabled",
        Boolean,
        comment="Whether Stripe automatically computes tax on this invoice. Note that incompatible invoice items (invoice items with manually specified [tax rates](https://stripe.com/docs/api/tax_rates), negative amounts, or `tax_behavior=unspecified`) cannot be added to automatic tax invoices",
    ),
    Column(
        "status",
        String,
        comment="The status of the most recent automated tax calculation for this invoice",
        nullable=True,
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["automatic_tax.json"]
