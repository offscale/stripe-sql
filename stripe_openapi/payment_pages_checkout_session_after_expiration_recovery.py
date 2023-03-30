from sqlalchemy import Boolean, Column, Identity, Integer, String, Table

from . import metadata

PaymentPagesCheckoutSessionAfterExpirationRecovery.Json = Table(
    "payment_pages_checkout_session_after_expiration_recovery.json",
    metadata,
    Column(
        "allow_promotion_codes",
        Boolean,
        comment="Enables user redeemable promotion codes on the recovered Checkout Sessions. Defaults to `false`",
    ),
    Column(
        "enabled",
        Boolean,
        comment="If `true`, a recovery url will be generated to recover this Checkout Session if it\nexpires before a transaction is completed. It will be attached to the\nCheckout Session object upon expiration",
    ),
    Column(
        "expires_at",
        Integer,
        comment="The timestamp at which the recovery URL will expire",
        nullable=True,
    ),
    Column(
        "url",
        String,
        comment="URL that creates a new Checkout Session when clicked that is a copy of this expired Checkout Session",
        nullable=True,
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["payment_pages_checkout_session_after_expiration_recovery.json"]
