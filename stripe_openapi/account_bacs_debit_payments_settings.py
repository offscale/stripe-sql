from sqlalchemy import Column, String, Table

from . import metadata

AccountBacsDebitPaymentsSettings.Json = Table(
    "account_bacs_debit_payments_settings.json",
    metadata,
    Column(
        "display_name",
        String,
        comment="The Bacs Direct Debit Display Name for this account. For payments made with Bacs Direct Debit, this will appear on the mandate, and as the statement descriptor",
        nullable=True,
        primary_key=True,
    ),
)
__all__ = ["account_bacs_debit_payments_settings.json"]
