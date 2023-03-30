from sqlalchemy import Column, Identity, Integer, String, Table

from . import metadata

PaymentMethodBacsDebit.Json = Table(
    "payment_method_bacs_debit.json",
    metadata,
    Column(
        "fingerprint",
        String,
        comment="Uniquely identifies this particular bank account. You can use this attribute to check whether two bank accounts are the same",
        nullable=True,
    ),
    Column(
        "last4",
        String,
        comment="Last four digits of the bank account number",
        nullable=True,
    ),
    Column(
        "sort_code",
        String,
        comment="Sort code of the bank account. (e.g., `10-20-30`)",
        nullable=True,
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["payment_method_bacs_debit.json"]
