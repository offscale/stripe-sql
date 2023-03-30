from sqlalchemy import JSON, Column, Identity, Integer, Table

from . import metadata

TreasuryFinancialAccountsResourceBalance.Json = Table(
    "treasury_financial_accounts_resource_balance.json",
    metadata,
    Column("cash", JSON, comment="Funds the user can spend right now"),
    Column(
        "inbound_pending",
        JSON,
        comment="Funds not spendable yet, but will become available at a later time",
    ),
    Column(
        "outbound_pending",
        JSON,
        comment="Funds in the account, but not spendable because they are being held for pending outbound flows",
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["treasury_financial_accounts_resource_balance.json"]
