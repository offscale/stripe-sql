from sqlalchemy import Column, Identity, Integer, Table

from . import metadata

PaymentIntentPaymentMethodOptionsMandateOptionsSepaDebit.Json = Table(
    "payment_intent_payment_method_options_mandate_options_sepa_debit.json",
    metadata,
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["payment_intent_payment_method_options_mandate_options_sepa_debit.json"]
