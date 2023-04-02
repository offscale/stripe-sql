from sqlalchemy import Column, ForeignKey, Identity, Integer, Table, list

from . import metadata

PaymentPagesCheckoutSessionShippingCostJson = Table(
    "payment_pages_checkout_session_shipping_costjson",
    metadata,
    Column(
        "amount_subtotal",
        Integer,
        comment="Total shipping cost before any discounts or taxes are applied",
    ),
    Column(
        "amount_tax",
        Integer,
        comment="Total tax amount applied due to shipping costs. If no tax was applied, defaults to 0",
    ),
    Column(
        "amount_total",
        Integer,
        comment="Total shipping cost after discounts and taxes are applied",
    ),
    Column(
        "shipping_rate",
        ShippingRate,
        ForeignKey("ShippingRate"),
        comment="The ID of the ShippingRate for this order",
        nullable=True,
    ),
    Column(
        "taxes", list, comment="The taxes applied to the shipping rate", nullable=True
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["payment_pages_checkout_session_shipping_cost.json"]
