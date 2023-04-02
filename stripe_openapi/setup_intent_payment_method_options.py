from sqlalchemy import Column, ForeignKey, Identity, Integer, Table

from . import metadata

SetupIntentPaymentMethodOptionsJson = Table(
    "setup_intent_payment_method_optionsjson",
    metadata,
    Column(
        "acss_debit",
        SetupIntentPaymentMethodOptionsAcssDebit,
        ForeignKey("SetupIntentPaymentMethodOptionsAcssDebit"),
        nullable=True,
    ),
    Column(
        "blik",
        SetupIntentPaymentMethodOptionsBlik,
        ForeignKey("SetupIntentPaymentMethodOptionsBlik"),
        nullable=True,
    ),
    Column(
        "card",
        SetupIntentPaymentMethodOptionsCard,
        ForeignKey("SetupIntentPaymentMethodOptionsCard"),
        nullable=True,
    ),
    Column(
        "link",
        SetupIntentPaymentMethodOptionsLink,
        ForeignKey("SetupIntentPaymentMethodOptionsLink"),
        nullable=True,
    ),
    Column(
        "sepa_debit",
        SetupIntentPaymentMethodOptionsSepaDebit,
        ForeignKey("SetupIntentPaymentMethodOptionsSepaDebit"),
        nullable=True,
    ),
    Column(
        "us_bank_account",
        SetupIntentPaymentMethodOptionsUsBankAccount,
        ForeignKey("SetupIntentPaymentMethodOptionsUsBankAccount"),
        nullable=True,
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["setup_intent_payment_method_options.json"]
