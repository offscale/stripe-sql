from sqlalchemy import Column, Identity, Integer, Table

from . import metadata

SetupAttemptPaymentMethodDetailsAuBecsDebitJson = Table(
    "setup_attempt_payment_method_details_au_becs_debitjson",
    metadata,
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["setup_attempt_payment_method_details_au_becs_debit.json"]
