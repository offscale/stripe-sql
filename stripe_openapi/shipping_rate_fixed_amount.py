from sqlalchemy import JSON, Column, Identity, Integer, String, Table

from . import metadata

ShippingRateFixedAmountJson = Table(
    "shipping_rate_fixed_amountjson",
    metadata,
    Column(
        "amount",
        Integer,
        comment="A non-negative integer in cents representing how much to charge",
    ),
    Column(
        "currency",
        String,
        comment="Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies)",
    ),
    Column(
        "currency_options",
        JSON,
        comment="Shipping rates defined in each available currency option. Each key must be a three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html) and a [supported currency](https://stripe.com/docs/currencies)",
        nullable=True,
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["shipping_rate_fixed_amount.json"]
