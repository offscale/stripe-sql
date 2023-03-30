from sqlalchemy import Column, ForeignKey, Identity, Integer, String, Table

from . import metadata

SetupIntentPaymentMethodOptionsUsBankAccount.Json = Table(
    "setup_intent_payment_method_options_us_bank_account.json",
    metadata,
    Column(
        "financial_connections",
        LinkedAccountOptionsUsBankAccount,
        ForeignKey("LinkedAccountOptionsUsBankAccount"),
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
__all__ = ["setup_intent_payment_method_options_us_bank_account.json"]
