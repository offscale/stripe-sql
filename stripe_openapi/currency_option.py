from sqlalchemy import Column, ForeignKey, Identity, Integer, String, Table, list

from . import metadata

CurrencyOptionJson = Table(
    "currency_optionjson",
    metadata,
    Column(
        "custom_unit_amount",
        CustomUnitAmount,
        ForeignKey("CustomUnitAmount"),
        comment="When set, provides configuration for the amount to be adjusted by the customer during Checkout Sessions and Payment Links",
        nullable=True,
    ),
    Column(
        "tax_behavior",
        String,
        comment="Specifies whether the price is considered inclusive of taxes or exclusive of taxes. One of `inclusive`, `exclusive`, or `unspecified`. Once specified as either `inclusive` or `exclusive`, it cannot be changed",
        nullable=True,
    ),
    Column(
        "tiers",
        list,
        comment="Each element represents a pricing tier. This parameter requires `billing_scheme` to be set to `tiered`. See also the documentation for `billing_scheme`",
        nullable=True,
    ),
    Column(
        "unit_amount",
        Integer,
        comment="The unit amount in %s to be charged, represented as a whole integer if possible. Only set if `billing_scheme=per_unit`",
        nullable=True,
    ),
    Column(
        "unit_amount_decimal",
        String,
        comment="The unit amount in %s to be charged, represented as a decimal string with at most 12 decimal places. Only set if `billing_scheme=per_unit`",
        nullable=True,
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["currency_option.json"]
