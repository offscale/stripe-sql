from sqlalchemy import Column, Identity, Integer, String, Table

from . import metadata

PlanTier.Json = Table(
    "plan_tier.json",
    metadata,
    Column("flat_amount", Integer, comment="Price for the entire tier", nullable=True),
    Column(
        "flat_amount_decimal",
        String,
        comment="Same as `flat_amount`, but contains a decimal value with at most 12 decimal places",
        nullable=True,
    ),
    Column(
        "unit_amount",
        Integer,
        comment="Per unit price for units relevant to the tier",
        nullable=True,
    ),
    Column(
        "unit_amount_decimal",
        String,
        comment="Same as `unit_amount`, but contains a decimal value with at most 12 decimal places",
        nullable=True,
    ),
    Column(
        "up_to",
        Integer,
        comment="Up to and including to this quantity will be contained in the tier",
        nullable=True,
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["plan_tier.json"]
