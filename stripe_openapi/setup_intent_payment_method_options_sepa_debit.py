from sqlalchemy import Column, ForeignKey, Identity, Integer, Table

from . import metadata

SetupIntentPaymentMethodOptionsSepaDebitJson = Table(
    "setup_intent_payment_method_options_sepa_debitjson",
    metadata,
    Column(
        "mandate_options",
        SetupIntentPaymentMethodOptionsMandateOptionsSepaDebit,
        ForeignKey("SetupIntentPaymentMethodOptionsMandateOptionsSepaDebit"),
        nullable=True,
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["setup_intent_payment_method_options_sepa_debit.json"]
