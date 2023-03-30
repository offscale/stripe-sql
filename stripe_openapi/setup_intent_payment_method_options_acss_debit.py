from sqlalchemy import Column, ForeignKey, Identity, Integer, String, Table

from . import metadata

SetupIntentPaymentMethodOptionsAcssDebit.Json = Table(
    "setup_intent_payment_method_options_acss_debit.json",
    metadata,
    Column(
        "currency",
        String,
        comment="Currency supported by the bank account",
        nullable=True,
    ),
    Column(
        "mandate_options",
        SetupIntentPaymentMethodOptionsMandateOptionsAcssDebit,
        ForeignKey("SetupIntentPaymentMethodOptionsMandateOptionsAcssDebit"),
        nullable=True,
    ),
    Column(
        "verification_method",
        String,
        comment="Bank account verification method",
        nullable=True,
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["setup_intent_payment_method_options_acss_debit.json"]
