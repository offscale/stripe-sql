from sqlalchemy import Column, Identity, Integer, String, Table

from . import metadata

PaymentPagesCheckoutSessionCustomTextPosition.Json = Table(
    "payment_pages_checkout_session_custom_text_position.json",
    metadata,
    Column("message", String, comment="Text may be up to 1000 characters in length"),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["payment_pages_checkout_session_custom_text_position.json"]
