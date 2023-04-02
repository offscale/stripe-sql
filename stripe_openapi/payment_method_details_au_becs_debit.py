from sqlalchemy import Column, Identity, Integer, String, Table

from . import metadata

PaymentMethodDetailsAuBecsDebitJson = Table(
    "payment_method_details_au_becs_debitjson",
    metadata,
    Column(
        "bsb_number",
        String,
        comment="Bank-State-Branch number of the bank account",
        nullable=True,
    ),
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
        "mandate",
        String,
        comment="ID of the mandate used to make this payment",
        nullable=True,
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["payment_method_details_au_becs_debit.json"]
