from sqlalchemy import Column, Identity, Integer, String, Table

from . import metadata

ShippingRateCurrencyOption.Json = Table(
    "shipping_rate_currency_option.json",
    metadata,
    Column(
        "amount",
        Integer,
        comment="A non-negative integer in cents representing how much to charge",
    ),
    Column(
        "tax_behavior",
        String,
        comment="Specifies whether the rate is considered inclusive of taxes or exclusive of taxes. One of `inclusive`, `exclusive`, or `unspecified`",
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["shipping_rate_currency_option.json"]
