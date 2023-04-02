from sqlalchemy import Column, Identity, Integer, Table

from . import metadata

CustomUnitAmountJson = Table(
    "custom_unit_amountjson",
    metadata,
    Column(
        "maximum",
        Integer,
        comment="The maximum unit amount the customer can specify for this item",
        nullable=True,
    ),
    Column(
        "minimum",
        Integer,
        comment="The minimum unit amount the customer can specify for this item. Must be at least the minimum charge amount",
        nullable=True,
    ),
    Column(
        "preset",
        Integer,
        comment="The starting unit amount which can be updated by the customer",
        nullable=True,
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["custom_unit_amount.json"]
