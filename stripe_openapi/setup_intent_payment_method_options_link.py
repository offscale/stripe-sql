from sqlalchemy import Column, Identity, Integer, String, Table

from . import metadata

SetupIntentPaymentMethodOptionsLink.Json = Table(
    "setup_intent_payment_method_options_link.json",
    metadata,
    Column(
        "persistent_token",
        String,
        comment="Token used for persistent Link logins",
        nullable=True,
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["setup_intent_payment_method_options_link.json"]
