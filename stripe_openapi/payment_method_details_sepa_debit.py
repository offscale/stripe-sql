from sqlalchemy import Column, Identity, Integer, String, Table

from . import metadata

PaymentMethodDetailsSepaDebit.Json = Table(
    "payment_method_details_sepa_debit.json",
    metadata,
    Column(
        "bank_code",
        String,
        comment="Bank code of bank associated with the bank account",
        nullable=True,
    ),
    Column(
        "branch_code",
        String,
        comment="Branch code of bank associated with the bank account",
        nullable=True,
    ),
    Column(
        "country",
        String,
        comment="Two-letter ISO code representing the country the bank account is located in",
        nullable=True,
    ),
    Column(
        "fingerprint",
        String,
        comment="Uniquely identifies this particular bank account. You can use this attribute to check whether two bank accounts are the same",
        nullable=True,
    ),
    Column("last4", String, comment="Last four characters of the IBAN", nullable=True),
    Column(
        "mandate",
        String,
        comment="ID of the mandate used to make this payment",
        nullable=True,
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["payment_method_details_sepa_debit.json"]
