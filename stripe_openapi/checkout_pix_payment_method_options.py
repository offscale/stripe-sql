from sqlalchemy import Column, Identity, Integer, Table

from . import metadata

CheckoutPixPaymentMethodOptions.Json = Table(
    "checkout_pix_payment_method_options.json",
    metadata,
    Column(
        "expires_after_seconds",
        Integer,
        comment="The number of seconds after which Pix payment will expire",
        nullable=True,
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["checkout_pix_payment_method_options.json"]
