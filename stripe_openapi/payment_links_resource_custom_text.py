from sqlalchemy import Column, ForeignKey, Identity, Integer, Table

from . import metadata

PaymentLinksResourceCustomText.Json = Table(
    "payment_links_resource_custom_text.json",
    metadata,
    Column(
        "shipping_address",
        PaymentLinksResourceCustomTextPosition,
        ForeignKey("PaymentLinksResourceCustomTextPosition"),
        comment="Custom text that should be displayed alongside shipping address collection",
        nullable=True,
    ),
    Column(
        "submit",
        PaymentLinksResourceCustomTextPosition,
        ForeignKey("PaymentLinksResourceCustomTextPosition"),
        comment="Custom text that should be displayed alongside the payment confirmation button",
        nullable=True,
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["payment_links_resource_custom_text.json"]
