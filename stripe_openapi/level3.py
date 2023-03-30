from sqlalchemy import Column, Identity, Integer, String, Table, list

from . import metadata

Level3.Json = Table(
    "level3.json",
    metadata,
    Column("customer_reference", String, nullable=True),
    Column("line_items", list),
    Column("merchant_reference", String),
    Column("shipping_address_zip", String, nullable=True),
    Column("shipping_amount", Integer, nullable=True),
    Column("shipping_from_zip", String, nullable=True),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["level3.json"]
