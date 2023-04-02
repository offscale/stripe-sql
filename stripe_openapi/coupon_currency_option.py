from sqlalchemy import Column, Identity, Integer, Table

from . import metadata

CouponCurrencyOptionJson = Table(
    "coupon_currency_optionjson",
    metadata,
    Column(
        "amount_off",
        Integer,
        comment="Amount (in the `currency` specified) that will be taken off the subtotal of any invoices for this customer",
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["coupon_currency_option.json"]
