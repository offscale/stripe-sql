from sqlalchemy import Boolean, Column, ForeignKey, Identity, Integer, Table

from . import metadata

CreditNoteTaxAmount.Json = Table(
    "credit_note_tax_amount.json",
    metadata,
    Column("amount", Integer, comment="The amount, in %s, of the tax"),
    Column(
        "inclusive",
        Boolean,
        comment="Whether this tax amount is inclusive or exclusive",
    ),
    Column(
        "tax_rate",
        TaxRate,
        ForeignKey("TaxRate"),
        comment="The tax rate that was applied to get this tax amount",
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["credit_note_tax_amount.json"]
