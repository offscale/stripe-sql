from sqlalchemy import Column, ForeignKey, Identity, Integer, Table

from . import metadata

PaymentPagesCheckoutSessionShippingOptionJson = Table(
    "payment_pages_checkout_session_shipping_optionjson",
    metadata,
    Column(
        "shipping_amount",
        Integer,
        comment="A non-negative integer in cents representing how much to charge",
    ),
    Column(
        "shipping_rate",
        ShippingRate,
        ForeignKey("ShippingRate"),
        comment="The shipping rate",
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["payment_pages_checkout_session_shipping_option.json"]
