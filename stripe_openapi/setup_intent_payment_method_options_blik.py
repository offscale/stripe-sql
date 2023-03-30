from sqlalchemy import Column, ForeignKey, Identity, Integer, Table

from . import metadata

SetupIntentPaymentMethodOptionsBlik.Json = Table(
    "setup_intent_payment_method_options_blik.json",
    metadata,
    Column(
        "mandate_options",
        SetupIntentPaymentMethodOptionsMandateOptionsBlik,
        ForeignKey("SetupIntentPaymentMethodOptionsMandateOptionsBlik"),
        nullable=True,
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["setup_intent_payment_method_options_blik.json"]
