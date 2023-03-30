from sqlalchemy import Column, Identity, Integer, Table

from . import metadata

SetupAttemptPaymentMethodDetailsSepaDebit.Json = Table(
    "setup_attempt_payment_method_details_sepa_debit.json",
    metadata,
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["setup_attempt_payment_method_details_sepa_debit.json"]
