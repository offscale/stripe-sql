from sqlalchemy import Column, Identity, Integer, String, Table

from . import metadata

Level3LineItems.Json = Table(
    "level3_line_items.json",
    metadata,
    Column("discount_amount", Integer, nullable=True),
    Column("product_code", String),
    Column("product_description", String),
    Column("quantity", Integer, nullable=True),
    Column("tax_amount", Integer, nullable=True),
    Column("unit_cost", Integer, nullable=True),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["level3_line_items.json"]
