from sqlalchemy import ARRAY, Column, Identity, Integer, String, Table

from . import metadata

SetupIntentPaymentMethodOptionsMandateOptionsAcssDebitJson = Table(
    "setup_intent_payment_method_options_mandate_options_acss_debitjson",
    metadata,
    Column(
        "custom_mandate_url",
        String,
        comment="A URL for custom mandate text",
        nullable=True,
    ),
    Column(
        "default_for",
        ARRAY(String),
        comment="List of Stripe products where this mandate can be selected automatically",
        nullable=True,
    ),
    Column(
        "interval_description",
        String,
        comment="Description of the interval. Only required if the 'payment_schedule' parameter is 'interval' or 'combined'",
        nullable=True,
    ),
    Column(
        "payment_schedule",
        String,
        comment="Payment schedule for the mandate",
        nullable=True,
    ),
    Column(
        "transaction_type",
        String,
        comment="Transaction type of the mandate",
        nullable=True,
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["setup_intent_payment_method_options_mandate_options_acss_debit.json"]
