from sqlalchemy import Column, String, Table

from . import metadata

OutboundTransfersPaymentMethodDetailsUsBankAccount.Json = Table(
    "outbound_transfers_payment_method_details_us_bank_account.json",
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
        "last4",
        String,
        comment="Last four digits of the bank account number",
        nullable=True,
    ),
    Column("network", String, comment="The US bank account network used to send funds"),
    Column(
        "routing_number",
        String,
        comment="Routing number of the bank account",
        nullable=True,
    ),
)
__all__ = ["outbound_transfers_payment_method_details_us_bank_account.json"]
