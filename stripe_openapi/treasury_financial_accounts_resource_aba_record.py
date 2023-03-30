from sqlalchemy import Column, Identity, Integer, String, Table

from . import metadata

TreasuryFinancialAccountsResourceAbaRecord.Json = Table(
    "treasury_financial_accounts_resource_aba_record.json",
    metadata,
    Column(
        "account_holder_name",
        String,
        comment="The name of the person or business that owns the bank account",
    ),
    Column("account_number", String, comment="The account number", nullable=True),
    Column(
        "account_number_last4",
        String,
        comment="The last four characters of the account number",
    ),
    Column("bank_name", String, comment="Name of the bank"),
    Column("routing_number", String, comment="Routing number for the account"),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["treasury_financial_accounts_resource_aba_record.json"]
