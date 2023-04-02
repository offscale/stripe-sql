from sqlalchemy import Column, ForeignKey, Identity, Integer, Table

from . import metadata

PaymentPagesCheckoutSessionAfterExpirationJson = Table(
    "payment_pages_checkout_session_after_expirationjson",
    metadata,
    Column(
        "recovery",
        PaymentPagesCheckoutSessionAfterExpirationRecovery,
        ForeignKey("PaymentPagesCheckoutSessionAfterExpirationRecovery"),
        comment="When set, configuration used to recover the Checkout Session on expiry",
        nullable=True,
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["payment_pages_checkout_session_after_expiration.json"]
