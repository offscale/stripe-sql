from sqlalchemy import Column, String, Table

from . import metadata

PaymentMethodDetailsAchDebitJson = Table(
    "payment_method_details_ach_debitjson",
    metadata,
    Column(
        "account_holder_type",
        String,
        comment="Type of entity that holds the account. This can be either `individual` or `company`",
        nullable=True,
    ),
    Column(
        "bank_name",
        String,
        comment="Name of the bank associated with the bank account",
        nullable=True,
        primary_key=True,
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
    Column(
        "last4",
        String,
        comment="Last four digits of the bank account number",
        nullable=True,
    ),
    Column(
        "routing_number",
        String,
        comment="Routing transit number of the bank account",
        nullable=True,
    ),
)
__all__ = ["payment_method_details_ach_debit.json"]
