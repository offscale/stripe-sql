from sqlalchemy import Boolean, Column, Identity, Integer, String, Table

from . import metadata

PaymentPagesCheckoutSessionAutomaticTax.Json = Table(
    "payment_pages_checkout_session_automatic_tax.json",
    metadata,
    Column(
        "enabled",
        Boolean,
        comment="Indicates whether automatic tax is enabled for the session",
    ),
    Column(
        "status",
        String,
        comment="The status of the most recent automated tax calculation for this session",
        nullable=True,
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["payment_pages_checkout_session_automatic_tax.json"]
