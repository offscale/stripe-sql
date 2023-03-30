from sqlalchemy import Column, String, Table

from . import metadata

AccountSepaDebitPaymentsSettings.Json = Table(
    "account_sepa_debit_payments_settings.json",
    metadata,
    Column(
        "creditor_id",
        String,
        comment="SEPA creditor identifier that identifies the company making the payment",
        nullable=True,
        primary_key=True,
    ),
)
__all__ = ["account_sepa_debit_payments_settings.json"]
