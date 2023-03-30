from sqlalchemy import Column, Integer, String, Table

from . import metadata

TaxDeductedAtSource.Json = Table(
    "tax_deducted_at_source.json",
    metadata,
    Column("id", String, comment="Unique identifier for the object", primary_key=True),
    Column(
        "object",
        String,
        comment="String representing the object's type. Objects of the same type share the same value",
    ),
    Column(
        "period_end",
        Integer,
        comment="The end of the invoicing period. This TDS applies to Stripe fees collected during this invoicing period",
    ),
    Column(
        "period_start",
        Integer,
        comment="The start of the invoicing period. This TDS applies to Stripe fees collected during this invoicing period",
    ),
    Column(
        "tax_deduction_account_number",
        String,
        comment="The TAN that was supplied to Stripe when TDS was assessed",
    ),
)
__all__ = ["tax_deducted_at_source.json"]
