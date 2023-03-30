from sqlalchemy import Column, Identity, Integer, Table

from . import metadata

SetupAttemptPaymentMethodDetailsUsBankAccount.Json = Table(
    "setup_attempt_payment_method_details_us_bank_account.json",
    metadata,
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["setup_attempt_payment_method_details_us_bank_account.json"]
