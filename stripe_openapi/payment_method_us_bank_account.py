from sqlalchemy import Column, ForeignKey, String, Table

from . import metadata

PaymentMethodUsBankAccountJson = Table(
    "payment_method_us_bank_accountjson",
    metadata,
    Column(
        "account_holder_type",
        String,
        comment="Account holder type: individual or company",
        nullable=True,
    ),
    Column(
        "account_type",
        String,
        comment="Account type: checkings or savings. Defaults to checking if omitted",
        nullable=True,
    ),
    Column(
        "bank_name",
        String,
        comment="The name of the bank",
        nullable=True,
        primary_key=True,
    ),
    Column(
        "financial_connections_account",
        String,
        comment="The ID of the Financial Connections Account used to create the payment method",
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
        "networks",
        UsBankAccountNetworks,
        ForeignKey("UsBankAccountNetworks"),
        comment="Contains information about US bank account networks that can be used",
        nullable=True,
    ),
    Column(
        "routing_number",
        String,
        comment="Routing number of the bank account",
        nullable=True,
    ),
)
__all__ = ["payment_method_us_bank_account.json"]
