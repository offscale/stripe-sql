from sqlalchemy import ARRAY, Column, Identity, Integer, String, Table

from . import metadata

CouponAppliesTo.Json = Table(
    "coupon_applies_to.json",
    metadata,
    Column(
        "products",
        ARRAY(String),
        comment="A list of product IDs this coupon applies to",
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["coupon_applies_to.json"]
