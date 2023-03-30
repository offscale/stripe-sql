from sqlalchemy import Column, Identity, Integer, String, Table

from . import metadata

SourceOrderItem.Json = Table(
    "source_order_item.json",
    metadata,
    Column(
        "amount",
        Integer,
        comment="The amount (price) for this order item",
        nullable=True,
    ),
    Column(
        "currency",
        String,
        comment="This currency of this order item. Required when `amount` is present",
        nullable=True,
    ),
    Column(
        "description",
        String,
        comment="Human-readable description for this order item",
        nullable=True,
    ),
    Column(
        "parent",
        String,
        comment="The ID of the associated object for this line item. Expandable if not null (e.g., expandable to a SKU)",
        nullable=True,
    ),
    Column(
        "quantity",
        Integer,
        comment="The quantity of this order item. When type is `sku`, this is the number of instances of the SKU to be ordered",
        nullable=True,
    ),
    Column(
        "type",
        String,
        comment="The type of this order item. Must be `sku`, `tax`, or `shipping`",
        nullable=True,
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["source_order_item.json"]
