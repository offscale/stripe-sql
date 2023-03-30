from sqlalchemy import Column, ForeignKey, Identity, Integer, Table

from stripe_openapi.discount import Discount

from . import metadata

DiscountsResourceDiscountAmount.Json = Table(
    "discounts_resource_discount_amount.json",
    metadata,
    Column("amount", Integer, comment="The amount, in %s, of the discount"),
    Column(
        "discount",
        Discount,
        ForeignKey("DeletedDiscount"),
        comment="The discount that was applied to get this discount amount",
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["discounts_resource_discount_amount.json"]
