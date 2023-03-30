from sqlalchemy import Column, ForeignKey, Identity, Integer, Table

from . import metadata

PaymentPagesCheckoutSessionCustomText.Json = Table(
    "payment_pages_checkout_session_custom_text.json",
    metadata,
    Column(
        "shipping_address",
        PaymentPagesCheckoutSessionCustomTextPosition,
        ForeignKey("PaymentPagesCheckoutSessionCustomTextPosition"),
        comment="Custom text that should be displayed alongside shipping address collection",
        nullable=True,
    ),
    Column(
        "submit",
        PaymentPagesCheckoutSessionCustomTextPosition,
        ForeignKey("PaymentPagesCheckoutSessionCustomTextPosition"),
        comment="Custom text that should be displayed alongside the payment confirmation button",
        nullable=True,
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["payment_pages_checkout_session_custom_text.json"]
