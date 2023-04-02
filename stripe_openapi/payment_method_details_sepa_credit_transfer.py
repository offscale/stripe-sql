from sqlalchemy import Column, String, Table

from . import metadata

PaymentMethodDetailsSepaCreditTransferJson = Table(
    "payment_method_details_sepa_credit_transferjson",
    metadata,
    Column(
        "bank_name",
        String,
        comment="Name of the bank associated with the bank account",
        nullable=True,
        primary_key=True,
    ),
    Column(
        "bic",
        String,
        comment="Bank Identifier Code of the bank associated with the bank account",
        nullable=True,
    ),
    Column(
        "iban",
        String,
        comment="IBAN of the bank account to transfer funds to",
        nullable=True,
    ),
)
__all__ = ["payment_method_details_sepa_credit_transfer.json"]
