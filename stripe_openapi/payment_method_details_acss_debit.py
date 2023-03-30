from sqlalchemy import Column, String, Table

from . import metadata

PaymentMethodDetailsAcssDebit.Json = Table(
    "payment_method_details_acss_debit.json",
    metadata,
    Column(
        "bank_name",
        String,
        comment="Name of the bank associated with the bank account",
        nullable=True,
        primary_key=True,
    ),
    Column(
        "fingerprint",
        String,
        comment="Uniquely identifies this particular bank account. You can use this attribute to check whether two bank accounts are the same",
        nullable=True,
    ),
    Column(
        "institution_number",
        String,
        comment="Institution number of the bank account",
        nullable=True,
    ),
    Column(
        "last4",
        String,
        comment="Last four digits of the bank account number",
        nullable=True,
    ),
    Column(
        "mandate",
        String,
        comment="ID of the mandate used to make this payment",
        nullable=True,
    ),
    Column(
        "transit_number",
        String,
        comment="Transit number of the bank account",
        nullable=True,
    ),
)
__all__ = ["payment_method_details_acss_debit.json"]
