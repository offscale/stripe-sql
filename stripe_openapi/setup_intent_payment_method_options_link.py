from sqlalchemy import Column, Identity, Integer, String, Table

from . import metadata

SetupIntentPaymentMethodOptionsLinkJson = Table(
    "setup_intent_payment_method_options_linkjson",
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
