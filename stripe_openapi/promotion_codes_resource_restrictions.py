from sqlalchemy import JSON, Boolean, Column, Identity, Integer, String, Table

from . import metadata

PromotionCodesResourceRestrictions.Json = Table(
    "promotion_codes_resource_restrictions.json",
    metadata,
    Column(
        "currency_options",
        JSON,
        comment="Promotion code restrictions defined in each available currency option. Each key must be a three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html) and a [supported currency](https://stripe.com/docs/currencies)",
        nullable=True,
    ),
    Column(
        "first_time_transaction",
        Boolean,
        comment="A Boolean indicating if the Promotion Code should only be redeemed for Customers without any successful payments or invoices",
    ),
    Column(
        "minimum_amount",
        Integer,
        comment="Minimum amount required to redeem this Promotion Code into a Coupon (e.g., a purchase must be $100 or more to work)",
        nullable=True,
    ),
    Column(
        "minimum_amount_currency",
        String,
        comment="Three-letter [ISO code](https://stripe.com/docs/currencies) for minimum_amount",
        nullable=True,
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["promotion_codes_resource_restrictions.json"]
