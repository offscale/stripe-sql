from sqlalchemy import Column, Identity, Integer, Table

from . import metadata

SetupAttemptPaymentMethodDetailsAcssDebitJson = Table(
    "setup_attempt_payment_method_details_acss_debitjson",
    metadata,
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["setup_attempt_payment_method_details_acss_debit.json"]
