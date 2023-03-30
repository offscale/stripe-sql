from sqlalchemy import Column, Identity, Integer, Table

from . import metadata

SetupIntentPaymentMethodOptionsMandateOptionsSepaDebit.Json = Table(
    "setup_intent_payment_method_options_mandate_options_sepa_debit.json",
    metadata,
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["setup_intent_payment_method_options_mandate_options_sepa_debit.json"]
