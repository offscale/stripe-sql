from sqlalchemy import Column, Identity, Integer, Table

from . import metadata

PromotionCodeCurrencyOption.Json = Table(
    "promotion_code_currency_option.json",
    metadata,
    Column(
        "minimum_amount",
        Integer,
        comment="Minimum amount required to redeem this Promotion Code into a Coupon (e.g., a purchase must be $100 or more to work)",
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["promotion_code_currency_option.json"]
