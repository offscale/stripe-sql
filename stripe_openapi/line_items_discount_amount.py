from sqlalchemy import Column, ForeignKey, Identity, Integer, Table

from stripe_openapi.discount import Discount

from . import metadata

LineItemsDiscountAmountJson = Table(
    "line_items_discount_amountjson",
    metadata,
    Column("amount", Integer, comment="The amount discounted"),
    Column("discount", Discount, ForeignKey("Discount")),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["line_items_discount_amount.json"]
