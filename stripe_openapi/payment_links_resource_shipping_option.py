from sqlalchemy import Column, ForeignKey, Identity, Integer, Table

from . import metadata

PaymentLinksResourceShippingOptionJson = Table(
    "payment_links_resource_shipping_optionjson",
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
        comment="The ID of the Shipping Rate to use for this shipping option",
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["payment_links_resource_shipping_option.json"]
